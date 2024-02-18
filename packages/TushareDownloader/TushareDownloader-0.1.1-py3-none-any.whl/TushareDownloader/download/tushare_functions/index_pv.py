"""
Tushare original API for index price and volume data

Author: Yanzhong Huang
Email: yanzhong.huang@outlook.com
Website: https://bagelquant.com

- index_daily
- index_weekly
- index_monthly
"""

from pandas import DataFrame
from tushare.pro.client import DataApi  # type: ignore


def index_daily(pro: DataApi,
                ts_code: str,
                trade_date: str = '',
                start_date: str = '',
                end_date: str = '') -> DataFrame:
    """
    index daily

    :param pro: tushare pro api
    :param ts_code: ts_code
    :param trade_date: trade_date
    :param start_date: start_date
    :param end_date: end_date
    """
    return pro.index_daily(ts_code=ts_code,
                           trade_date=trade_date,
                           start_date=start_date,
                           end_date=end_date,
                           fields=[
                               "ts_code",
                               "trade_date",
                               "open",
                               "high",
                               "low",
                               "close",
                               "pre_close",
                               "change",
                               "pct_chg",
                               "vol",
                               "amount"
                           ])  # type: ignore


def index_weekly(pro: DataApi,
                 ts_code: str,
                 trade_date: str = '',
                 start_date: str = '',
                 end_date: str = '') -> DataFrame:
    """
    index weekly

    :param pro: tushare pro api
    :param ts_code: ts_code
    :param trade_date: trade_date
    :param start_date: start_date
    :param end_date: end_date
    """
    return pro.index_weekly(ts_code=ts_code,
                            trade_date=trade_date,
                            start_date=start_date,
                            end_date=end_date,
                            fields=[
                                "ts_code",
                                "trade_date",
                                "open",
                                "high",
                                "low",
                                "close",
                                "pre_close",
                                "change",
                                "pct_chg",
                                "vol",
                                "amount"
                            ])  # type: ignore


def index_monthly(pro: DataApi,
                  ts_code: str,
                  trade_date: str = '',
                  start_date: str = '',
                  end_date: str = '') -> DataFrame:
    """
    index monthly

    :param pro: tushare pro api
    :param ts_code: ts_code
    :param trade_date: trade_date
    :param start_date: start_date
    :param end_date: end_date
    """
    return pro.index_monthly(ts_code=ts_code,
                             trade_date=trade_date,
                             start_date=start_date,
                             end_date=end_date,
                             fields=[
                                 "ts_code",
                                 "trade_date",
                                 "open",
                                 "high",
                                 "low",
                                 "close",
                                 "pre_close",
                                 "change",
                                 "pct_chg",
                                 "vol",
                                 "amount"
                             ])  # type: ignore
