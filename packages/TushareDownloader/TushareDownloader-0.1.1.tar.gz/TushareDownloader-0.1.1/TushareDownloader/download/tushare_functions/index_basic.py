"""
Tushare original API for index basic data

Author: Yanzhong Huang
Email: yanzhong.huang@outlook.com
Website: https://bagelquant.com

- index_list
"""

from pandas import DataFrame
from tushare.pro.client import DataApi  # type: ignore


def index_list(pro: DataApi,
               ts_code: str = '',
               market: str = '',
               publisher: str = '',
               category: str = '',
               name: str = '') -> DataFrame:
    """
    index list
    
    :param pro: tushare pro api
    :param ts_code: ts_code
    :param market: market
    :param publisher: publisher
    :param category: category
    :param name: name

    """
    return pro.index_basic(**{
        "ts_code": "",
        "market": "",
        "publisher": "",
        "category": "",
        "name": "",
        "limit": "",
        "offset": ""
    }, fields=[
        "ts_code",
        "name",
        "market",
        "publisher",
        "category",
        "base_date",
        "base_point",
        "list_date",
        "fullname",
        "index_type",
        "weight_rule",
        "desc",
        "exp_date"
    ])  # type: ignore
