"""
database base module

Author: Yanzhong Huang
Email: yanzhong.huang@outlook.com
"""

import os
import json
from sqlalchemy import create_engine

from sqlalchemy import Engine

# Get the path of the directory of the current script
dir_path = os.path.dirname(os.path.realpath(__file__))

# Use os.path.join to create a path
CONFIG_PATH = os.path.join(dir_path, 'database_config.json')


def get_db_config() -> dict[str, str|int]:
    """
    get database configuration
    :return: database configuration
    """
    with open(CONFIG_PATH, 'r') as f:
        config = json.load(f)
    return config 


def update_db_config(config: dict[str, str|int]) -> None:
    """
    update database configuration
    :param config: database configuration
    :return: None
    """
    with open(CONFIG_PATH, 'w') as f:
        json.dump(config, f)


def get_db_engine() -> Engine:
    """
    :return: database engine
    """
    config = get_db_config()
    engine = create_engine(
        f"mysql+pymysql://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['database']}",
        echo=False
    )
    return engine


if __name__ == '__main__':
    print(get_db_config())
