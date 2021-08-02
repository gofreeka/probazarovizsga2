from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(ChromeDriverManager().install())
# URL = ''
# driver.get(URL)

try:
    # Oldal betöltése
    driver.get('https://witty-hill-0acfceb03.azurestaticapps.net/mutant_teams.html')
    time.sleep(2)

    original_team = driver.find_element_by_xpath("/html/body/div/label[1]")
    x_force_team = driver.find_element_by_xpath("/html/body/div/label[2]")
    x_factor_team = driver.find_element_by_xpath("/html/body/div/label[3]")
    hellfire_club_team = driver.find_element_by_xpath("/html/body/div/label[4]")

    assert original_team.is_displayed()
    assert x_force_team.is_displayed()
    assert x_factor_team.is_displayed()
    assert hellfire_club_team.is_displayed()


finally:
    driver.quit()
