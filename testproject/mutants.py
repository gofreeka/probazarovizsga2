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


    # Original Team:


    def og_team():
        original_team.click()
        time.sleep(1)

        # Team members list
        team_members_id = driver.find_elements_by_xpath("//li[@id]/h2")
        print(">>> Original X-men Team members: ")
        for cr in team_members_id:

            # Print if displayed
            if cr.is_displayed():
                print(cr.text)


    # X-Force Team:


    def force_team():
        x_force_team.click()
        time.sleep(1)

        # Team members list
        team_members_id = driver.find_elements_by_xpath("//li[@id]/h2")
        print(">>> X-Force Team members: ")
        for cr in team_members_id:

            # Print if displayed
            if cr.is_displayed():
                print(cr.text)


    # X-Factor Team:


    def factor_team():
        x_factor_team.click()
        time.sleep(1)

        # Team members list
        team_members_id = driver.find_elements_by_xpath("//li[@id]/h2")
        print(">>> X-Factor Team members: ")
        for cr in team_members_id:

            # Print if displayed
            if cr.is_displayed():
                print(cr.text)


    # Hellfire Team:


    def hellfire_team():
        hellfire_club_team.click()
        time.sleep(1)

        # Team members list
        team_members_id = driver.find_elements_by_xpath("//li[@id]/h2")
        print(">>> Hellfire Club members: ")
        for cr in team_members_id:

            # Print if displayed
            if cr.is_displayed():
                print(cr.text)


    og_team()
    force_team()
    factor_team()
    hellfire_team()

    # A tagok csapatban valo ellenorzeset a data-teams attributummal oldanam meg,
    # abban az iranyban a keresem a megoldast

    # d_teams = driver.find_elements_by_xpath("//li[@data-teams]")

finally:
    driver.quit()
