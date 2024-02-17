from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from EpicGames_FreeGames_Bot.WaitHelper import WaitHelper

class EpicGamesConnect:

    GOOGLE_LOGIN_PATH= '//*[@id="login-with-google"]'
    LOGIN_BTN_PATH='//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[1]/div'
    PROFILE_SELECT_MAIN_PATH='//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul'
    PROFILE_CHILD_PATH='//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[1]'
    FREE_NOW_COST_ELEMENT_PATH='//*[@id="dieselReactWrapper"]/div/div[4]/main/div[2]/div/div/div/div[2]/div[2]/span[4]/div/div/section/div/div[1]/div/div/a/div/div/div[1]/div[2]'
    FREE_BUY_BUTTON_PATH='//*[@id="dieselReactWrapper"]/div/div[4]/main/div[2]/div/div/div/div[2]/div[3]/div/aside/div/div/div[6]/div/button'
    @staticmethod
    def login(driver, expected_url):
        WaitHelper.random_sleep(3, 5)
        if driver.current_url == expected_url:
            print("Correct URL.")
            EpicGamesConnect.free_games_cost(driver)
        else:
            print(f"Different URL: {driver.current_url}")
            EpicGamesConnect.logins_started(driver)
            return

    @staticmethod
    def logins_started(driver):
        print("Logging in with Google...")
        # next-step
        next_step = WaitHelper.wait_for_element(driver, By.XPATH, EpicGamesConnect.GOOGLE_LOGIN_PATH)
        next_step.click()
        new_window_handle = driver.window_handles[-1]  # Son eklenen pencerenin tanımlayıcısını al
        driver.switch_to.window(new_window_handle)
        profile_select_main=WaitHelper.wait_for_element(driver, By.XPATH,EpicGamesConnect.PROFILE_SELECT_MAIN_PATH)
        profile_children=WaitHelper.wait_for_elements(profile_select_main,By.XPATH,EpicGamesConnect.PROFILE_CHILD_PATH)
        profile_index=int(input("Index the user account you want to log in to(e.g. 0 - ):"))
        profile_children[profile_index].click()
        WaitHelper.random_sleep(4, 6)
        EpicGamesConnect.free_games_cost(driver)

    @staticmethod
    def free_games_cost(driver):
        print("Purchasing process started...")
        # get last added window
        driver.switch_to.window(driver.window_handles[0])
        WaitHelper.random_sleep(3, 4)
        epic_html_content = driver.page_source
        epic_window_soup = BeautifulSoup(epic_html_content, 'html.parser')
        free_games_window = epic_window_soup.find('div', {'class': 'css-1vu10h2'})
        free_game_child = free_games_window.find('div', {'class': 'css-1myhtyb'})
        free_now_cost = free_game_child.find('div', {'class': 'css-1magkk1'})

        # Free Now Cost element
        if free_now_cost:
            free_now_cost_element = WaitHelper.wait_for_element(driver, By.XPATH,EpicGamesConnect.FREE_NOW_COST_ELEMENT_PATH)
            free_now_cost_element.click()
            print("Free cost clicked")
            WaitHelper.random_sleep(2, 3)
            free_buy_button = WaitHelper.wait_for_element(driver, By.XPATH,EpicGamesConnect.FREE_BUY_BUTTON_PATH)
            free_buy_button.click()
            WaitHelper.random_sleep(2,3)

            place_order_html = driver.page_source
            place_order_html_soup = BeautifulSoup(place_order_html, 'html.parser')

            #iframe
            web_purchase_container = place_order_html_soup.find('div', {'class': 'webPurchaseContainer'})
            iframe_content=web_purchase_container.find('iframe')
            iframe_url = iframe_content['src']  # iframe'in src özelliği ile URL alınır

            driver.get(f'https://store.epicgames.com{iframe_url}')
            iframe_html = driver.page_source
            iframe_soup = BeautifulSoup(iframe_html, 'html.parser')
            if iframe_soup:
                WaitHelper.random_sleep(1,2)
                place_btn=WaitHelper.wait_for_element(driver,By.XPATH,'//*[@id="purchase-app"]/div/div/div/div[2]/div[2]/div')
                place_btn.click()
                print("Place_order clicked")

            print("Purchase completed...")
        else:
            print("Element not found")

