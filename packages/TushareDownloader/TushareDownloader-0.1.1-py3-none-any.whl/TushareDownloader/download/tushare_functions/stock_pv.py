"""
Tushare original api for stock price and volume data

Author: Yanzhong Huang
Email: yanzhong.huang@outlook.com
Website: https://bagelquant.com

- stock_daily
- stock_weekly
- stock_monthly
"""

from pandas import DataFrame
from tushare.pro.client import DataApi  # type: ignore


def stock_daily(pro: DataApi,
                ts_code: str = '',
                trade_date: str = '',
                start_date: str = '',
                end_date: str = '') -> DataFrame:
    """
    stock daily
    :param pro: tushare pro api
    :param ts_code: ts_code
    :param trade_date: trade_date
    :param start_date: start_date
    :param end_date: end_date
    """
    return pro.daily(**{
        "ts_code": ts_code,
        "trade_date": trade_date,
        "start_date": start_date,
        "end_date": end_date,
        "offset": "",
        "limit": ""
    }, fields=[
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
    ])


def stock_weekly(pro: DataApi,
                 ts_code: str = '',
                 trade_date: str = '',
                 start_date: str = '',
                 end_date: str = '') -> DataFrame:
    """
    stock weekly, 
    ATTENTION: ts_code, trade_date cannot be None at the same time!

    :param pro: tushare pro api
    :param ts_code: ts_code
    :param trade_date: trade_date
    :param start_date: start_date
    :param end_date: end_date
    """
    return pro.weekly(**{
        "ts_code": ts_code,
        "trade_date": trade_date,
        "start_date": start_date,
        "end_date": end_date,
        "offset": "",
        "limit": ""
    }, fields=[
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
    ])


def stock_monthly(pro: DataApi,
                  ts_code: str = '',
                  trade_date: str = '',
                  start_date: str = '',
                  end_date: str = '') -> DataFrame:
    """
    stock monthly
    :param pro: tushare pro api
    :param ts_code: ts_code
    :param trade_date: trade_date
    :param start_date: start_date
    :param end_date: end_date
    """
    return pro.monthly(**{
        "ts_code": ts_code,
        "trade_date": trade_date,
        "start_date": start_date,
        "end_date": end_date,
        "offset": "",
        "limit": ""
    }, fields=[
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
    ])


def adj_factor(pro: DataApi,
               ts_code: str = '',
               trade_date: str = '',
               start_date: str = '',
               end_date: str = '') -> DataFrame:
    """
    adjust factor
    """
    return pro.adj_factor(**{
        "ts_code": ts_code,
        "trade_date": trade_date,
        "start_date": start_date,
        "end_date": end_date,
        "limit": "",
        "offset": ""
    }, fields=[
        "ts_code",
        "trade_date",
        "adj_factor"
    ])
