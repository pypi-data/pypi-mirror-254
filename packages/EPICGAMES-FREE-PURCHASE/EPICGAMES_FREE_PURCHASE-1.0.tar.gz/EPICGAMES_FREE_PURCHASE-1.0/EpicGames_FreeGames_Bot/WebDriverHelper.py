import os

from selenium import webdriver
class WebDriverHelper:
    @staticmethod
    def create_chrome_driver(profiler_directory):
        options = webdriver.ChromeOptions()

        options.add_argument(f'--profile-directory={profiler_directory}')
        user_data_dir = os.path.join(os.environ['LOCALAPPDATA'], 'Google', 'Chrome', 'User Data')
        options.add_argument(f"user-data-dir={user_data_dir}")

        options.add_argument('--no-first-run')
        options.add_argument('--no-default-browser-check')
        return webdriver.Chrome(options=options)