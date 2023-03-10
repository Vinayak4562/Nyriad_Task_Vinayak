import unittest
import sqlite3
from datetime import datetime, timedelta
from DataBase_connection import create_table, insert_email, get_emails


class TestEmailFetcher(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # create a test database and table
        cls.conn = sqlite3.connect(':memory:')
        cls.c = cls.conn.cursor()
        cls.c.execute('''CREATE TABLE emails (id INTEGER PRIMARY KEY AUTOINCREMENT,from_email TEXT, subject TEXT, date TEXT)''')
        cls.conn.commit()

    @classmethod
    def tearDownClass(cls):
        # close the test database connection
        cls.conn.close()

    def setUp(self):
        # insert test emails into the database
        insert_email('pramod havannavar ', 'test cases', (datetime.now() - timedelta(days=2)).strftime('%a, %d %b %Y %H:%M:%S %z'))
        insert_email('pramod havannavar ', 'test cases2', (datetime.now() - timedelta(days=1)).strftime('%a, %d %b %Y %H:%M:%S %z'))
        insert_email('Vishal Hirandagi', 'Test2', datetime.now().strftime('%a, %d %b %Y %H:%M:%S %z'))
        self.conn.commit()

    def tearDown(self):
        # delete all test emails from the database
        self.c.execute('DELETE FROM emails')
        self.conn.commit()

    def test_fetch_by_name(self):
        # fetch emails by sender name and validate the results
        emails = get_emails('vinz223665@gmail.com', None)
        self.assertEqual(len(emails), 1)
        self.assertEqual(emails[0]['From'], 'promod456@gmail.com')
        self.assertEqual(emails[0]['Subject'], 'vishalhirandagi33@gmail.com')

    def test_fetch_by_duration(self):
        # fetch emails by time duration and validate the results
        emails = get_emails(None, 2)
        self.assertEqual(len(emails), 2)
        self.assertEqual(emails[0]['From'], 'promod456@gmail.com')
        self.assertEqual(emails[0]['Subject'], 'test cases2')
        self.assertEqual(emails[1]['From'], 'promod456@gmail.com')
        self.assertEqual(emails[1]['Subject'], 'test cases')


if __name__ == '__main__':
    unittest.main()
