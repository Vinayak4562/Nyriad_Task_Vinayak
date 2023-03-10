import unittest
import os.path
from DataBase_connection import create_table, insert_email, get_emails
import sqlite3

class TestEmailFetcher(unittest.TestCase):
    
    def setUp(self):
        self.db_filename = 'emails.db'
        if os.path.isfile(self.db_filename):
            os.remove(self.db_filename)
    
    def test_create_table(self):
        create_table()
        conn = sqlite3.connect(self.db_filename)
        c = conn.cursor()
        c.execute('SELECT name FROM sqlite_master WHERE type=\'table\' AND name=\'emails\'')
        self.assertIsNotNone(c.fetchone())
        conn.close()
    
    def test_insert_email(self):
        from_email = 'promod456@gmail.com'
        subject = 'test cases'
        date = 'Fri, 10 Mar 2023 17:23:38 +0530W'
        insert_email(from_email, subject, date)
        conn = sqlite3.connect(self.db_filename)
        c = conn.cursor()
        c.execute('SELECT * FROM emails WHERE from_email=? AND subject=? AND date=?', (from_email, subject, date))
        self.assertIsNotNone(c.fetchone())
        conn.close()
    
    def test_get_emails_by_name(self):
        name = 'pramod havannavar'
        create_table()
        insert_email(name, 'test cases', 'Fri, 10 Mar 2023 17:23:38 +0530W')
        insert_email('promod456@gmail.com', 'Fri, 10 Mar 2023 17:23:38 +0530W')
        emails = get_emails(name, None)
        self.assertEqual(len(emails), 2)
        self.assertEqual(emails[0]['From'], name)

         
    
    def test_get_emails_by_duration(self):
        name = 'pramod havannavar'
        create_table()
        insert_email(name, 'test cases', 'Fri, 10 Mar 2023 17:23:38 +0530W')
        insert_email('promod456@gmail.com', 'test cases', 'Fri, 10 Mar 2023 17:23:38 +0530W')
        emails = get_emails(None, 1)
        self.assertEqual(len(emails), 11)
        self.assertEqual(emails[0]['Subject'], 'test cases')
    
    def tearDown(self):
        if os.path.isfile(self.db_filename):
            os.remove(self.db_filename)

if __name__ == '__main__':
    unittest.main()
