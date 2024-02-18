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


    def test_get_player_winrate(self):
        account_link = "https://leetify.com/app/profile/76561199506785320"
        winrate = self.scraper.get_player_winrate(account_link)
        self.assertIsNotNone(winrate)


    def test_get_player_teammates(self):
        account_link = "https://leetify.com/app/profile/76561199506785320"
        teammates = self.scraper.get_player_teammates(account_link)
        self.assertIsNotNone(teammates)
        print(teammates)

    def test_get_steam_profile_link(self):
        account_link = "https://leetify.com/app/profile/76561199506785320"
        steamlink = self.scraper.get_steam_profile_link(account_link)
    
        if steamlink:
            print(f"Steam Profile Link: {steamlink}")
        else:
            print("Failed to retrieve Steam Profile Link.")
    def test_get_steam_profile_link(self):
        account_link = self.scraper.get_steam_profile_link("https://leetify.com/app/profile/76561199506785320")
        steamlevel = self.scraper.get_player_steam_level(account_link)
    
        if steamlevel:
            print(f"Steam Profile Link: {steamlevel}")
        else:
            print("Failed to retrieve Steam Profile Link.")

    def test_get_player_banned(self):
        account_link = "https://leetify.com/app/profile/76561199506785320"
        banned = self.scraper.get_banned(account_link)
        self.assertIsNotNone(banned)
        print(banned)

if __name__ == "__main__":
    unittest.main()
