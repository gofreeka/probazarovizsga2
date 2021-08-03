from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    # Oldal betöltése

    URL = 'https://witty-hill-0acfceb03.azurestaticapps.net/film_register.html'
    driver.get(URL)
    time.sleep(4)

    # TC001 - 24 film betoltesenek ellenorzese

    # movie_title_list = driver.find_elements_by_xpath("//div/img[@alt]")
    # print(len(movie_title_list))
    movie_title_list = driver.find_elements_by_tag_name("h2")
    assert len(movie_title_list) == 24

    # TC002 - Film felvetele

    # Test data

    movie_test_data = ["Black widow",
                       2021,
                       2020,
                       "https://www.youtube.com/watch?v=Fp9pNPdNwjI",
                       "https://m.media-amazon.com/images/I/914MHuDfMSL._AC_UY327_FMwebp_QL65_.jpg",
                       "https://www.imdb.com/title/tt3480822/"
                       ]
    # Register form elements

    film_title = driver.find_element_by_id("nomeFilme")
    release_year = driver.find_element_by_id("anoLancamentoFilme")
    chrono_year = driver.find_element_by_id("anoCronologiaFilme")
    trailer_url = driver.find_element_by_id("linkTrailerFilme")
    image_url = driver.find_element_by_id("linkImagemFilme")
    file_sum = driver.find_element_by_id("linkImdbFilme")

    reg_film_bt = driver.find_element_by_xpath("//div/button")
    reg_form = driver.find_element_by_xpath("//div/div/fieldset")
    save_bt = driver.find_element_by_xpath("//div[2]/div[2]/fieldset/button[1]")

    # Register form actions

    reg_film_bt.click()
    time.sleep(3)
    assert reg_form.is_displayed()

    # Fill out form with test data

    film_title.send_keys(movie_test_data[0])
    release_year.send_keys(movie_test_data[1])
    chrono_year.send_keys(movie_test_data[2])
    trailer_url.send_keys(movie_test_data[3])
    image_url.send_keys(movie_test_data[4])
    file_sum.send_keys(movie_test_data[5])

    save_bt.click()
    time.sleep(3)

    # Check the number of movie titles

    # print(len(movie_title_list))
    assert len(movie_title_list) == 25
    time.sleep(5)

finally:
    driver.quit()
