"""
Tushare original api for stock basic

Author: Yanzhong Huang
Email: yanzhong.huang@outlook.com
Website: https://bagelquant.com

Stock basic
- stock_list
- trading_calendar
"""

from pandas import DataFrame
from tushare.pro.client import DataApi  # type: ignore


def stock_list(pro: DataApi,
               ts_code: str = '',
               name: str = '',
               exchange: str = '',
               market: str = '',
               is_hs: str = '',
               list_status: str = '') -> DataFrame:
    """
    stock list
    :param pro: tushare pro api
    :param ts_code: ts_code
    :param name: name
    :param exchange: exchange, option: SSE上交所 SZSE深交所 HKEX港交所
    :param market: market
    :param is_hs: is_hs, option:
    :param list_status: list_status

    """
    return pro.stock_basic(**{
        "ts_code": ts_code,
        "name": name,
        "exchange": exchange,
        "market": market,
        "is_hs": is_hs,
        "list_status": list_status,
        "limit": "",
        "offset": ""
    }, fields=[
        "ts_code",
        "symbol",
        "name",
        "area",
        "industry",
        "market",
        "list_date",
        "fullname",
        "enname",
        "cnspell",
        "exchange",
        "curr_type",
        "list_status",
        "delist_date",
        "is_hs",
        "act_name",
        "act_ent_type"
    ])  # type: ignore


def trading_calendar(pro: DataApi,
                     exchange: str = '',
                     start_date: str = '',
                     end_date: str = '') -> DataFrame:
    """
    trading calendar
    :param pro: tushare pro api
    :param exchange: exchange, option: SSE上交所 SZSE深交所 HKEX港交所
    :param start_date: start date
    :param end_date: end date
    """
    return pro.trade_cal(**{
        "exchange": exchange,
        "start_date": start_date,
        "end_date": end_date
    }, fields=[
        "exchange",
        "cal_date",
        "is_open",
        "pretrade_date"
    ])  # type: ignore
