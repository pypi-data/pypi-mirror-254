from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class WebScraper:
    def __init__(self):
        options = Options()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)  # Use appropriate webdriver for your browser
        self.wait = WebDriverWait(self.driver, 10)  # Adjust the timeout as needed

    def get_player_name(self, account_link):
        self.driver.get(account_link)
        try:
            rank_and_name = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, 'rank-and-name'))
            )
            player_name = rank_and_name.find_element(By.CLASS_NAME, 'text-truncate').text
            return player_name
        except Exception as e:
            print(f"Error getting player name: {str(e)}")
            return None

    def get_player_winrate(self, account_link):
        self.driver.get(account_link)
        try:
            win_rate = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, 'win-rate'))
            )
            WebDriverWait(win_rate, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'score-text')))
            winrate_percentage = win_rate.find_element(By.CLASS_NAME, 'score-text').text
            return winrate_percentage
        except Exception as e:
            print(f"Error getting player winrate: {str(e)}")
            return None

    def get_player_teammates(self, account_link):
        self.driver.get(account_link)
        teammates_dict = {}
        try:
            teammates_section = self.wait.until(
                EC.presence_of_element_located((By.ID, 'teammates'))
            )
            player_meta_elements = teammates_section.find_elements(By.CLASS_NAME, 'player-meta')

            for player_meta in player_meta_elements:
                player_name_element = player_meta.find_element(By.CLASS_NAME, 'name')
                player_name = player_name_element.text

                teammate_parent = player_meta.find_element(By.XPATH, '../..')
                teammate_link = teammate_parent.get_attribute('href')

                teammates_dict[player_name] = teammate_link

            return teammates_dict
        except Exception as e:
            print(f"Error getting player teammates: {str(e)}")
            return {}

    def close_browser(self):
        self.driver.quit()
