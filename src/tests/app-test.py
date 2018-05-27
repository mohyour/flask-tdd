import sys
import os
sys.path.append("src")

from app import app
import unittest


class BasicTestCase(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 404)

    def test_database(self):
        db_path_exist = os.path.exists("flaskr.db")
        self.assertTrue(db_path_exist)


if __name__ == '__main__':
    unittest.main()
