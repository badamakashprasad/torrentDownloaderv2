import unittest
from torrents.Eztv import EzTvClient
import logging

class TestEzTvClient(unittest.TestCase):
    def setUp(self):
        self.client = EzTvClient()

    def test_get_torrents(self):
        self.assertIsNotNone(self.client.get_torrents())

    def test_get_total(self):
        self.assertIsInstance(self.client.get_total(), int)

    def test_get_total_pages(self):
        self.assertIsInstance(self.client.get_total_pages(), int)

    def runAll(self):
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger(__name__)
        logger.info("Running all tests")
        unittest.main()
        