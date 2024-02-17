from EpicGames_FreeGames_Bot.EpicGamesConnect import EpicGamesConnect
from EpicGames_FreeGames_Bot.WebDriverHelper import WebDriverHelper
class EpicGamesAutomationApp:
    @staticmethod
    def run():
        profiler_directory=input("Which profile to log in with?(e.g. Profile 1): ")
        print("EpicGamesAutomation start...")
        driver = WebDriverHelper.create_chrome_driver(profiler_directory)

        url = 'https://www.epicgames.com/id/login?lang=en-US&noHostRedirect=true&redirectUrl=https%3A%2F%2Fstore.epicgames.com%2Fen-US%2F&client_id=875a3b57d3a640a6b7f9b4e883463ab4'
        expected_redirect_url = 'https://store.epicgames.com/en-US/'
        driver.get(url)

        EpicGamesConnect.login(driver, expected_redirect_url)

        input("Press a key to close the browser")

        driver.quit()

if __name__ == "__main__":
    EpicGamesAutomationApp.run()



















































