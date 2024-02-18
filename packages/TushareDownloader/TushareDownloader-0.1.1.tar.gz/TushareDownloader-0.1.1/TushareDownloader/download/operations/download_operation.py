"""
download operatation

all operation in this module should replace the data in the table
"""
from pandas import DataFrame 
from sqlalchemy import text
from typing import Callable

from TushareDownloader.database import get_db_engine
from .logging_operations import logging


def replacing(table_name: str, df: DataFrame) -> str:
    """
    replacing data to database
    :param table_name: table name
    :param df: New data
    :return: update_status str: Success replacing
    """
    # delete all data in the table
    try:
        engine = get_db_engine()
        conn = engine.connect()
        conn.execute(
                text(f'UPDATE {table_name} SET delete_flag = TRUE;')
            )
        engine.dispose()
    except Exception as e:
        return f'Failure in deleting, error: {str(e)}'[:300]

    # saving to datbase
    try:
        engine = get_db_engine()
        conn = engine.connect()
        df.to_sql(table_name, con=conn, if_exists='append', index=False)
        engine.dispose()
        return 'Success in replacing'
    except Exception as e:
        return f'Failure in replacing, error: {str(e)}'[:300]


TUSHARE_FUNCTION = Callable[..., DataFrame]


def download_operation(table_name: str,
                       tushare_function: TUSHARE_FUNCTION) -> None:
    """
    download operation
    :param table_name: table name
    :param tushare_function: a function that return DataFrame, match the table structure
    :return: None

    1. Download DataFrame
    2. Save
    3. Log
    """
    # downloading
    try:
        downloaded_df = tushare_function()

        # saving
        update_status: str = replacing(table_name, downloaded_df)
    except Exception as e:
        update_status: str = f'Failure in downloading, error: {str(e)}'[:300]

    # logging
    logging(table_name, update_status)
