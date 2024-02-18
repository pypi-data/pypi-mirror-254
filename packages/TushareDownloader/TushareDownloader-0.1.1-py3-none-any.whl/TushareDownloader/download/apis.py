"""
Download module apis

## APIs
### Download
The Download methods are designed to:
1. Download the corresponding table data.
2. Replace all existing data in the table.
   For Example: `download_stock_list` method will delete all data in the `stock_list` table
   and save the newly downloaded data.

Methods:
- download_stock_list
- download_trading_calendar

### Update
The Update methods are designed to:
1. Retrieve the latest trade date from the corresponding table.
2. Download data from the latest trade date to 'today'.
3. Append the newly downloaded data to the existing data in the table.

Methods:

Stocks:
- update_stock_daily
- update_stock_weekly
- update_stock_monthly
- update_adj_factor
- update_income_statement
- update_balance_sheet
- update_cash_flow
"""

import pandas as pd

from .operations import download_operation, update_operation, update_operation_by_ts_code
from .tushare_functions import get_tushare_pro
from .tushare_functions import (stock_list,
                                trading_calendar)
from .tushare_functions import stock_daily, stock_weekly, stock_monthly, adj_factor
from .tushare_functions import income_statement, balance_sheet, cash_flow

pro = get_tushare_pro()


def download_stock_list() -> None:
    """download stock list"""

    def all_stock_list() -> pd.DataFrame:
        """
        combine delisted and listed stock list
        """
        delisted = stock_list(pro, list_status='D')
        listed = stock_list(pro, list_status='L')
        return pd.concat([listed, delisted])  # type: ignore

    download_operation(table_name='stock_list', tushare_function=all_stock_list)


def download_trading_calendar() -> None:
    """download """
    download_operation(table_name='trading_calendar', tushare_function=lambda: trading_calendar(pro))


def update_stock_daily(max_workers: int = 9) -> None:
    """update stock daily to today"""
    update_operation(table_name='stock_daily', tushare_function=stock_daily, max_workers=max_workers)


def update_stock_weekly(max_workers: int = 9) -> None:
    """update stock weekly to today"""
    update_operation(table_name='stock_weekly', tushare_function=stock_weekly, max_workers=max_workers)


def update_stock_monthly(max_workers: int = 9) -> None:
    """update stock monthly to today"""
    update_operation(table_name='stock_monthly', tushare_function=stock_monthly, max_workers=max_workers)


def update_adj_factor(max_workers: int = 9) -> None:
    """update adj factor to today"""
    update_operation(table_name='adj_factor', tushare_function=adj_factor, max_workers=max_workers)


def update_income_statement(max_workers: int = 9) -> None:
    """update income statement to today"""
    update_operation_by_ts_code(table_name='income_statement', tushare_function=income_statement, max_workers=max_workers)


def update_balance_sheet(max_workers: int = 9) -> None:
    """update balance sheet to today"""
    update_operation_by_ts_code(table_name='balance_sheet', tushare_function=balance_sheet, max_workers=max_workers)


def update_cash_flow(max_workers: int = 9) -> None:
    """update cash flow to today"""
    update_operation_by_ts_code(table_name='cash_flow', tushare_function=cash_flow, max_workers=max_workers)
