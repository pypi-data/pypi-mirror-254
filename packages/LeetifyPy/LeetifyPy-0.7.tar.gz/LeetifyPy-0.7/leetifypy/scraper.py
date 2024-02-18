from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class WebScraper:
    def __init__(self):
        options = Options()
        self.driver = webdriver.Chrome(options=options)  # Use appropriate webdriver for your browser
        self.wait = WebDriverWait(self.driver, 10)  # Adjust the timeout as needed

    def navigate_to_url(self, url):
        try:
            self.driver.get(url)
            return True
        except Exception as e:
            print(f"Error navigating to URL {url}: {str(e)}")
            return False

    def get_player_name(self, account_link):
        if not self.navigate_to_url(account_link):
            return None

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
        if not self.navigate_to_url(account_link):
            return None

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
        if not self.navigate_to_url(account_link):
            return {}

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
    def get_steam_profile_link(self, account_link):
        if not self.navigate_to_url(account_link):
            return None
    
        try:
            steam_profile_link = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'div.profiles a[ngbtooltip="Steam Profile"]'))
            )
            return steam_profile_link.get_attribute('href')
        except Exception as e:
            print(f"Error getting Steam Profile link: {str(e)}")
            return None



    def get_player_steam_level(self, steam_profile_link):
        if not self.navigate_to_url(steam_profile_link):
            return None
    
        try:
            persona_info = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'div.persona_name.persona_level'))
            )
    
            level_element = persona_info.find_element(By.CLASS_NAME, 'friendPlayerLevelNum')
            steam_level = level_element.text
            return steam_level
        except Exception as e:
            print(e)


            
    def get_banned(self, leetify_profile_link):
        if not self.navigate_to_url(leetify_profile_link):
            return None
    
        try:
            profiles_section = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, 'profiles'))
            )
    
            ban_badge = profiles_section.find_elements(By.CLASS_NAME, 'ban-badge')
            return len(ban_badge) > 0
        except Exception as e:
            print(f"Error checking if player is banned: {str(e)}")
            return None



    def close_browser(self):
        self.driver.quit()
