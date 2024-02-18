"""
update operation

all operation in this module should use multiprocess download, and append to table
"""
import time
from datetime import date, timedelta
from pandas import DataFrame, Timestamp
from sqlalchemy import text
from typing import Callable
from concurrent.futures import ProcessPoolExecutor

from TushareDownloader.database import get_db_engine

from TushareDownloader.download.tushare_functions import get_tushare_pro
from TushareDownloader.download.operations.logging_operations import logging


def appendding(table_name: str, df: DataFrame) -> str:
    """
    appending data to database
    :param table_name: table name
    :param df: New data
    :return: update_status str: Success appending
    """
    try:
        engine = get_db_engine()
        df.to_sql(table_name, con=engine.connect(), if_exists='append', index=False)
        engine.dispose()

        # check if df is empty
        if df.empty:
            return 'Success in appending, but dataframe is empty'
        else:
            return 'Success in appending'
    except Exception as e:
        return f'Failure in appending, error: {str(e)}'[:300]


TUSHARE_FUNCTION = Callable[..., DataFrame]


def _single_download_operation(trade_date: str,
                               tushare_function: TUSHARE_FUNCTION,
                               table_name: str) -> str:
    """
    single download operation

    1. download stock data from tushare
    2. append data to database
    3. log
    """
    # download
    pro = get_tushare_pro()
    try:
        df = tushare_function(pro, trade_date=trade_date)
        # save
        update_status = appendding(table_name, df)
    except Exception as e:
        update_status = f'Failure in download, error: {str(e)}'[:300]
        # wait 60 seconds
        time.sleep(60)
        _single_download_operation(trade_date, tushare_function, table_name)

    # log
    logging(table_name, update_status)
    return f'{tushare_function.__name__} {trade_date}: {update_status}'


def _single_download_operation_by_ts_code(ts_code: str,
                                          tushare_function: TUSHARE_FUNCTION,
                                          table_name: str,
                                          start_date: str,
                                          end_date: str) -> str:
    """
    single download operation

    1. download stock data from tushare
    2. append data to database
    3. log
    """
    # download
    pro = get_tushare_pro()
    try:
        df = tushare_function(pro, ts_code=ts_code, start_date=start_date, end_date=end_date)
        # save
        update_status = appendding(table_name, df)
    except Exception as e:
        update_status = f'Failure in download, error: {str(e)}'[:300]
        # wait 60 seconds
        time.sleep(60)
        _single_download_operation_by_ts_code(ts_code, tushare_function, table_name, start_date, end_date)

    # log
    logging(table_name, update_status)
    return f'{tushare_function.__name__} {ts_code}: {update_status}'


def update_operation(table_name: str,
                     tushare_function: TUSHARE_FUNCTION,
                     max_workers: int = 9) -> None:
    """
    update operation
    :param table_name: table name
    :param tushare_function: a function that return DataFrame
    :param max_workers: maximum number of multiprocessing workers
    :return: None

    1. retrieve the latest trade_date from <table_name>
    2. get download trade_dates
    4. download data
    5. append data
    6. log
    """
    # retrieve latest trade_date
    latest_trade_date: date | None = retrieve_latest_trade_date(table_name=table_name)
    # download trade_dates
    download_trade_dates: list[str] = retrieve_download_trade_date(latest_trade_date=latest_trade_date)
    if not download_trade_dates:
        return
    else:
        with ProcessPoolExecutor(max_workers=max_workers) as executor:
            results = executor.map(_single_download_operation,
                                   download_trade_dates,
                                   [tushare_function for _ in download_trade_dates],
                                   [table_name for _ in download_trade_dates]
                                   )
            for result in results:
                del result


def update_operation_by_ts_code(table_name: str,
                                tushare_function: TUSHARE_FUNCTION,
                                max_workers: int = 9) -> None:
    """
    update operation by ts_code
    :param table_name: table name
    :param tushare_function: a function that return DataFrame
    :param max_workers: maximum number of multiprocessing workers
    :return: None

    1. retrieve stock_list
    2. retrieve latest trade_date, and set start date to latest trade_date
    3. download data
    """
    # retrieve stock_lisst
    stock_list: list[str] = retrieve_stock_list()
    # retrieve latest update log date
    latest_update_date: date | None = retrieve_latest_update_date(table_name=table_name)
    end_date = date.today()

    if latest_update_date:
        if latest_update_date >= end_date:
            return

        start_date: date = latest_update_date + timedelta(days=1)
        start_date_str: str = start_date.strftime("%Y%m%d")
    else:
        start_date_str: str = ''

    end_date_str: str = end_date.strftime("%Y%m%d")

    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        results = executor.map(_single_download_operation_by_ts_code,
                               stock_list,
                               [tushare_function for _ in stock_list],
                               [table_name for _ in stock_list],
                               [start_date_str for _ in stock_list],
                               [end_date_str for _ in stock_list]
                               )
        for result in results:
            del result


def retrieve_latest_update_date(table_name: str) -> date | None:
    """
    retrieve latest update date from update_log table
    :param table_name: table name
    :return: latest update, date
    """
    with get_db_engine().begin() as conn:
        sql = (f'SELECT MAX(update_time) FROM update_log '
               f'WHERE table_name = "{table_name}"'
               f'AND delete_flag = 0 '
               f'AND update_status LIKE "%Success%"')

        latest_update_date = conn.execute(text(sql)).fetchone()[0]  # type: ignore
    if latest_update_date:
        return latest_update_date.date()  # type: ignore
    else:
        return None


def retrieve_stock_list() -> list[str]:
    """
    retrieve stock list
    """
    with get_db_engine().begin() as conn:
        sql = f'SELECT ts_code FROM stock_list WHERE delete_flag = 0'
        stock_list: list[str] = conn.execute(text(sql)).fetchall()  # type: ignore
    return [_[0] for _ in stock_list]


def retrieve_download_trade_date(latest_trade_date: date | None) -> list[str]:
    """
    get all trade_date from latest trade_date to today, from trading_calendar table
    :param latest_trade_date: latest trade_date
    :return: list of trade_date from latest trade_date to today in %Y-%m-%d
    """
    today: date = date.today()
    if latest_trade_date is None:
        sql = f"""select cal_date from trading_calendar 
        where cal_date <= '{today.strftime("%Y-%m-%d")}' and delete_flag = 0"""
    else:
        if latest_trade_date >= today:
            return []
        latest_trade_date = latest_trade_date + timedelta(days=1)
        sql = (f"""select cal_date from trading_calendar where cal_date 
        between '{latest_trade_date.strftime("%Y-%m-%d")}' and '{today.strftime("%Y-%m-%d")}'
        and delete_flag = 0
        and is_open = 1""")

    with get_db_engine().begin() as conn:
        download_trade_date_list = conn.execute(text(sql)).fetchall()
        download_trade_date_list = [_[0] for _ in download_trade_date_list]
        download_trade_date_list = sorted(download_trade_date_list)
        download_trade_date_list = [_.strftime("%Y%m%d") for _ in download_trade_date_list]
    return download_trade_date_list


def retrieve_latest_trade_date(table_name: str) -> date | None:
    """
    retrieve latest trade date from <table_name>
    :param table_name: table
    :return: latest trade_date timestamp
    """
    sql = f"select max(trade_date) from {table_name} where delete_flag = 0"
    with get_db_engine().begin() as conn:
        latest_trade_date = conn.execute(text(sql)).fetchone()[0]  # type: ignore
    if latest_trade_date is None:
        return None
    else:
        return Timestamp(latest_trade_date).date()
