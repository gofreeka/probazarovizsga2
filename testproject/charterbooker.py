from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
URL = 'https://witty-hill-0acfceb03.azurestaticapps.net/charterbooker.html'

try:

    # Oldal betöltése
    driver.get(URL)
    time.sleep(3)

    # Collect elements
    total_guests_element = driver.find_element_by_xpath("//div[@id='step1']/ul/li[1]/select")
    next_button = driver.find_element_by_xpath("//button[contains(text(), 'Next')]")

    # Step 2 elements
    second_step = driver.find_element_by_xpath("//div[@id='step2']")
    second_step_bar = driver.find_element_by_xpath("//*[@id='booking-form']/div[2]/div/ul/li[2]")
    datepicker = driver.find_element_by_xpath("//li/input[@name='bf_date']")
    timepicker = driver.find_element_by_xpath("//li/select[@name='bf_time']")
    hourspicker = driver.find_element_by_xpath("//li/select[@name='bf_hours']")
    step_2_next_btn = driver.find_element_by_xpath("//div[@id='step2']/ul/li/button")

    # Step 3 elements
    third_step = driver.find_element_by_xpath("//div[@id='step3']")
    fullname_element = driver.find_element_by_xpath("//li/input[@name='bf_fullname']")
    email_element = driver.find_element_by_xpath("//li/input[@name='bf_email']")
    message_element = driver.find_element_by_xpath("//li/textarea[@name='bf_message']")
    request_bt = driver.find_element_by_xpath("//div[@id='step3']/ul/li/button")
    third_step_bar = driver.find_element_by_xpath("//*[@id='booking-form']/div[2]/div/ul/li[3]")

    # Success elements
    success_form = driver.find_element_by_xpath("//form[@id='booking-form']")

    assert total_guests_element.is_displayed()

    guest_nbr_test_data = [0, 1, 2, 12, 13, "More", "x"]
    datepicker_test_data = ["06-05-21"]
    timepicker_test_data = ["Select", "Morning", "Midday", "Late afternoon, ending with a sunset"]
    hourspicker_testdata = ["Select", 3, 4, 5, 6, 7, 8, "Overnight (24 hours)"]
    fullname_element_test_data = ["Balázs Pro"]
    email_element_test_data = ["vali@dal.ok"]

    # Tobboldalas mukodes
    total_guests_element.click()
    total_guests_element.send_keys(guest_nbr_test_data[1])
    next_button.click()
    time.sleep(2)

    # Step 2
    assert second_step.is_displayed()
    assert "progressbar-dots active" == second_step_bar.get_attribute("class")
    time.sleep(1)
    datepicker.send_keys(datepicker_test_data[0])
    timepicker.send_keys(timepicker_test_data[1])
    hourspicker.send_keys(hourspicker_testdata[1])
    step_2_next_btn.click()
    time.sleep(3)

    # Step 3
    assert third_step.is_displayed()
    assert "progressbar-dots active" == third_step_bar.get_attribute("class")
    fullname_element.send_keys(fullname_element_test_data[0])
    email_element.send_keys(email_element_test_data[0])
    request_bt.click()
    time.sleep(3)

    # Successful fill out
    scs_msg = "Your message was sent successfully. Thanks! " \
              "We'll be in touch as soon as we can, which is usually like lightning " \
              "(Unless we're sailing or eating tacos!)."
    assert success_form.is_displayed()
    success_msg = driver.find_element_by_xpath("//form/descendant::h2")
    assert scs_msg == success_msg.text

    # E-mail validation
    # Ezen még dolgozom.

    def e_mail_validation():
        assert "" == email_element.text
        # return

finally:
    driver.quit()
