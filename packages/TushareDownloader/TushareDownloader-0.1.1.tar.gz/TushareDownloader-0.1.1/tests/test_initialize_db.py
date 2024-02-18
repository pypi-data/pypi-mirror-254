import unittest

from TushareDownloader import create_all_tables
from TushareDownloader import get_db_config
from TushareDownloader import update_username
from TushareDownloader import update_password
from TushareDownloader import update_host
from TushareDownloader import update_port


class TestInitializeDB(unittest.TestCase):

    def test_get_db_config(self) -> None:
        db_config: dict[str, str | int] = get_db_config()
        self.assertIsInstance(db_config, dict)
        self.assertEqual(len(db_config), 5)
        self.assertIn('user', db_config)
        self.assertIn('password', db_config)
        self.assertIn('host', db_config)
        self.assertIn('port', db_config)
        self.assertIn('database', db_config)

    def test_update_user_name(self) -> None:
        user: str = 'test_user'
        update_username(user)
        db_config: dict[str, str | int] = get_db_config()
        self.assertEqual(db_config['user'], user)

    def test_update_password(self) -> None:
        password: str = 'test_password'
        update_password(password)
        db_config: dict[str, str | int] = get_db_config()
        self.assertEqual(db_config['password'], password)

    def test_update_host(self) -> None:
        host: str = 'test_host'
        update_host(host)
        db_config: dict[str, str | int] = get_db_config()
        self.assertEqual(db_config['host'], host)

    def test_update_port(self) -> None:
        port: int = 3306
        update_port(port)
        db_config: dict[str, str | int] = get_db_config()
        self.assertEqual(db_config['port'], port)

    def test_update_all(selfs) -> None:
        update_username('root')
        update_password('Hyz.js180518')
        update_host('localhost')
        update_port(3306)

    def test_create_all_tables(self) -> None:
        create_all_tables()
        pass


if __name__ == '__main__':
    unittest.main()
