"""
Tests for tushare original APIs

Module path: TushareDownloader/download/tushare_functions/__init__.py

Author: Yanzhong Huang
Email: yanzhong.huang@outlook.com
Website: https://bagelquant.com

## tushare basic

- get_token
- update_token
- get_tushare_pro

## stock basic
- stock_list
- trading_calendar

## stock pv
- stock_daily
- stock_weekly
- stock_monthly

## stock fundamental
- income_statement
- balance_sheet
- cash_flow

## index basic
- index_list

## index pv
- index_daily
- index_weekly
- index_monthly
"""

from cgi import test
from unittest import TestCase

from pandas import DataFrame
from tushare.pro.client import DataApi  # type: ignore

from TushareDownloader.download.tushare_functions import *

TOKEN = 'f7ad1328a17b49b5b7d126cb3ef4ae00565cba3adc28eeeecabbeb78'


class TestTushareFunctions(TestCase):

    def setUp(self):
        self.pro = DataApi(TOKEN)

    def test_get_token(self):
        token = get_token()
        self.assertEqual(token, TOKEN)

    def test_update_token(self):
        test_token = 'test_token'
        update_token(test_token)
        token = get_token()
        self.assertEqual(token, test_token)

        # change back to original token
        update_token(TOKEN)

    def test_get_tushare_pro(self):
        pro = get_tushare_pro()
        self.assertIsInstance(pro, DataApi)

    def test_stock_list(self):
        df = stock_list(self.pro)
        self.assertIsInstance(df, DataFrame)
        print(df)

    def test_trading_calendar(self):
        df = trading_calendar(self.pro)
        self.assertIsInstance(df, DataFrame)
        print(df)

    def test_stock_daily(self):
        df = stock_daily(self.pro)
        self.assertIsInstance(df, DataFrame)
        print(df)

    def test_stock_weekly(self):
        df = stock_weekly(self.pro,
                          ts_code='000001.SZ')
        self.assertIsInstance(df, DataFrame)
        print(df)

    def test_stock_monthly(self):
        df = stock_monthly(self.pro,
                           ts_code='000001.SZ')
        self.assertIsInstance(df, DataFrame)
        print(df)

    def test_income_statement(self):
        df = income_statement(self.pro,
                              ts_code='000001.SZ')
        self.assertIsInstance(df, DataFrame)
        print(df)

    def test_balance_sheet(self):
        df = balance_sheet(self.pro,
                           ts_code='000001.SZ')
        self.assertIsInstance(df, DataFrame)
        print(df)

    def test_cash_flow(self):
        df = cash_flow(self.pro,
                       ts_code='000001.SZ')
        self.assertIsInstance(df, DataFrame)
        print(df)

    def test_index_list(self):
        df = index_list(self.pro)
        self.assertIsInstance(df, DataFrame)
        print(df)

    def test_index_daily(self):
        df = index_daily(self.pro,
                         ts_code='000300.SH')
        self.assertIsInstance(df, DataFrame)

    def test_index_weekly(self):
        df = index_weekly(self.pro,
                          ts_code='000300.SH')
        self.assertIsInstance(df, DataFrame)
        print(df)

    def test_index_monthly(self):
        df = index_monthly(self.pro,
                           ts_code='000300.SH')
        self.assertIsInstance(df, DataFrame)
        print(df)
        