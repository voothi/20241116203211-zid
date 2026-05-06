import unittest
from unittest.mock import patch
import datetime
import io
import sys
import os

# Add parent directory to path to import zid
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from zid import generate_zid, get_config, main

class TestZid(unittest.TestCase):
    """
    Tests for ZID generation and configuration.
    """

    def test_default_zid_format(self):
        # Default format should be 14 digits
        zid = generate_zid()
        self.assertEqual(len(zid), 14)
        self.assertTrue(zid.isdigit())

    def test_custom_format(self):
        # Test custom format via config
        cfg = {
            'format': '%Y-%m-%d',
            'prefix': '',
            'suffix': ''
        }
        zid = generate_zid(cfg)
        # 2026-01-06 is 10 chars
        self.assertEqual(len(zid), 10)
        self.assertEqual(zid[4], '-')
        self.assertEqual(zid[7], '-')

    def test_prefix_and_suffix(self):
        # Test prefix and suffix via config
        cfg = {
            'format': '%Y',
            'prefix': 'ZID-',
            'suffix': '-test'
        }
        zid = generate_zid(cfg)
        # Expected: ZID-2026-test
        current_year = str(datetime.datetime.now().year)
        self.assertEqual(zid, f"ZID-{current_year}-test")

    @patch('os.path.exists')
    @patch('configparser.ConfigParser.read')
    @patch('configparser.ConfigParser.get')
    def test_get_config_fallback(self, mock_get, mock_read, mock_exists):
        # Test that get_config falls back to defaults if file missing
        mock_exists.return_value = False
        cfg = get_config()
        self.assertEqual(cfg['format'], '%Y%m%d%H%M%S')
        self.assertEqual(cfg['prefix'], '')
        self.assertEqual(cfg['suffix'], '')

    def test_main_default_copies_to_clipboard(self):
        with patch('zid.generate_zid', return_value='20260506091212'), \
             patch('zid.pyperclip.copy') as mock_copy, \
             patch('sys.stdout', new_callable=io.StringIO) as mock_stdout, \
             patch.object(sys, 'argv', ['zid.py']):
            main()

        self.assertEqual(mock_stdout.getvalue().strip(), '20260506091212')
        mock_copy.assert_called_once_with('20260506091212')

    def test_main_no_clipboard_does_not_copy(self):
        with patch('zid.generate_zid', return_value='20260506091212'), \
             patch('zid.pyperclip.copy') as mock_copy, \
             patch('sys.stdout', new_callable=io.StringIO) as mock_stdout, \
             patch.object(sys, 'argv', ['zid.py', '--no-clipboard']):
            main()

        self.assertEqual(mock_stdout.getvalue().strip(), '20260506091212')
        mock_copy.assert_not_called()

if __name__ == '__main__':
    unittest.main()
