import unittest
from leetifypy.scraper import WebScraper

class TestWebScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = WebScraper()

    def tearDown(self):
        self.scraper.close_browser()

    def test_get_player_name(self):
        account_link = "https://leetify.com/app/profile/76561199506785320"
        player_name = self.scraper.get_player_name(account_link)
        self.assertIsNotNone(player_name)
        # Add more specific assertions based on the expected behavior

    def test_get_player_winrate(self):
        account_link = "https://leetify.com/app/profile/76561199506785320"
        winrate = self.scraper.get_player_winrate(account_link)
        self.assertIsNotNone(winrate)
        # Add more specific assertions based on the expected behavior

    def test_get_player_teammates(self):
        account_link = "https://leetify.com/app/profile/76561199506785320"
        teammates = self.scraper.get_player_teammates(account_link)
        self.assertIsNotNone(teammates)
        print(teammates)
        # Add more specific assertions based on the expected behavior

if __name__ == "__main__":
    unittest.main()
