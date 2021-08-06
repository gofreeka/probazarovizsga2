from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = 'https://witty-hill-0acfceb03.azurestaticapps.net/guess_the_number.html'

try:
    # Oldal betöltése

    driver.get(URL)
    time.sleep(4)

    guess_input = driver.find_element_by_xpath("//div/input[@placeholder='Guess']")
    guess_button = driver.find_element_by_xpath("//span/button[contains(text(), 'Guess')]")
    result = driver.find_element_by_xpath("/html/body/div/p[5]")
    nbr_guess_badge = driver.find_element_by_xpath("/html/body/div/div[3]/p/span")
    restart_bt = driver.find_element_by_xpath("//div/button[contains(text(), 'Restart')]")
    g_higher = driver.find_element_by_xpath("//div/p[contains(text(), 'Guess higher.')]")
    g_lower = driver.find_element_by_xpath("//div/p[contains(text(), 'Guess lower.')]")

    def restart():
        restart_bt.click()

    # Range 1-100
    def tc001():
        x = 1
        while x <= 100:
            guess_input.send_keys(x)
            guess_button.click()
            print(x)
            guess_input.clear()
            x = x + 1

            # Ellenorzes: szukseges lepesek szama az applikacio szerint vs. sajat, belso szamlalo
            if result.is_displayed():
                assert nbr_guess_badge.text == str(x-1)
                break

    tc001()
    restart()
    time.sleep(3)

    # Range -19-1
    def tc002():
        x = -19
        while x < 1:
            guess_input.send_keys(x)
            guess_button.click()
            print(x)
            assert g_higher.is_displayed()
            guess_input.clear()
            x = x + 1

    tc002()
    restart()
    time.sleep(3)

    # Range 255-100
    def tc003():
        x = 255
        while x > 100:
            guess_input.send_keys(x)
            guess_button.click()
            print(x)
            assert g_lower.is_displayed()
            guess_input.clear()
            x = x - 1

    tc003()
    time.sleep(3)

finally:
    driver.quit()
