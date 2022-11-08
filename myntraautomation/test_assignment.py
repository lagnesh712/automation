from selenium import webdriver
import pytest

home_button_xpath= '//*[@id="desktop-header-cnt"]/div[2]/div[1]/a'
search_bar_class="desktop-searchBar"
search_button_xpath= '//*[@id="desktop-header-cnt"]/div[2]/div[3]/a'
select_element_xpath='//*[@id="desktopSearchResults"]/div[2]/section/ul/li[1]/a/div[1]/div/div/div/picture/img'
select_price_xpath='//*[@id="mountRoot"]/div/div/div/main/div[2]/div[2]/div[1]/p[1]/span[1]/strong'




driver = webdriver.Chrome(executable_path='./chromedriver')


def test_title():
    driver.get("https://myntra.com")
    print(driver.title)
    title=driver.title
    # driver.close()
    assert title=="Online Shopping for Women, Men, Kids Fashion & Lifestyle - Myntra"


def test_shirt_price():
    driver.get("https://myntra.com")
    print("Url done")
    driver.maximize_window()
    print("maximize done")
    driver.refresh()
    print("refresh done")
    driver.find_element_by_xpath(home_button_xpath).click()
    print("home button done")
    driver.find_element_by_class_name(search_bar_class).send_keys("men shirts")
    print("item searched")
    driver.find_element_by_xpath(search_button_xpath).click()
    print("item searched")
    driver.find_element_by_xpath(select_element_xpath).click()
    print("item selected")

    child=driver.window_handles[1]
    print("child window")
    driver.switch_to.window(child)
    print("window switched")
    driver.refresh()
    print("Refresh done")
    price=driver.find_element_by_xpath(select_price_xpath).text
    print(price)
    assert price=="Rs. 824"
