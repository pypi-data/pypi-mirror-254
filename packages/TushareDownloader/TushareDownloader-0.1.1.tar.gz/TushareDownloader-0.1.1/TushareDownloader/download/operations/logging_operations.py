"""
logging operations

"""

from pandas import DataFrame

from TushareDownloader.database import get_db_engine


def logging(table_name: str, update_status: str) -> None:
    """
    logging

    """
    log_df = DataFrame({
        'table_name': table_name,
        'update_status': update_status,
    }, index=[0])
    with get_db_engine().connect() as conn:
        log_df.to_sql('update_log', con=conn, if_exists='append', index=False)
        