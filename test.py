from eventfilter import process
from pathlib import Path
import unittest


class TestProcess(unittest.TestCase):

    def setUp(self):
        self.df = process(
            Path(__file__).parent / 'reports.csv',
            Path(__file__).parent / 'reports.json',
            Path(__file__).parent / 'reports.xml',
        )

    def test_filter(self):
        df = self.df
        self.assertEqual(0, len(df[df['packets-serviced'] == 0]))
        self.assertEqual(12, len(df[df['packets-serviced'] == 1]))

    def test_sort(self):
        df = self.df.reset_index()
        for i in range(1, len(df)):
            self.assertTrue(df.at[i-1, 'request-time'] <= df.at[i, 'request-time'])
