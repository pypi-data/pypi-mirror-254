"""
initialize_db

This module is used to initialize the database.

Methods:

- get_db_config
- update_db_config
- get_db_engine
- create_all_tables
"""

import os
from sqlalchemy import text
from TushareDownloader.database import get_db_engine
from TushareDownloader.database import get_db_config as _get_db_config
from TushareDownloader.database import update_db_config as _update_db_config

SQL_FILE_DIRECTORY = 'TushareDownloader/initialize_db/table_structures'


def create_all_tables() -> None:
    """
    create all tables in the database, using the SQL files in the directory 
    """
    sqls: list[str] = []
    for file_name in os.listdir(SQL_FILE_DIRECTORY):
        if file_name.endswith('.sql'):
            with open(os.path.join(SQL_FILE_DIRECTORY, file_name), 'r') as f:
                sql: str = f.read()
                single_file_sqls: list[str] = sql.split(';')
                for sql in single_file_sqls:
                    if sql != '' and sql != '\n':
                        sqls.append(sql)

    if len(sqls) == 0:
        return

    with get_db_engine().begin() as conn:
        for sql in sqls:
            conn.execute(text(sql))


def get_db_config() -> dict[str, str | int]:
    """
    get the database configuration
    """
    return _get_db_config()


def update_username(user: str) -> None:
    """
    update the username in the database configuration
    """
    db_config: dict[str, str | int] = get_db_config()
    db_config['user'] = user
    _update_db_config(db_config)


def update_password(password: str) -> None:
    """
    update the password in the database configuration
    """
    db_config: dict[str, str | int] = get_db_config()
    db_config['password'] = password
    _update_db_config(db_config)


def update_host(host: str) -> None:
    """
    update the host in the database configuration
    """
    db_config: dict[str, str | int] = get_db_config()
    db_config['host'] = host
    _update_db_config(db_config)


def update_port(port: int) -> None:
    """
    update the port in the database configuration
    """
    db_config: dict[str, str | int] = get_db_config()
    db_config['port'] = port
    _update_db_config(db_config)


def update_db_name(db_name: str) -> None:
    """
    update the database name in the database configuration
    """
    db_config: dict[str, str | int] = get_db_config()
    db_config['db_name'] = db_name
    _update_db_config(db_config)
