import pytest
import random
from random import choice
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from string import ascii_letters
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_registration(driver):
    driver.get("http://localhost/litecart/en/")
    driver.find_element_by_css_selector("table td > a").click()

    #регистрация
    driver.find_element_by_css_selector("[name=firstname]").send_keys("name")
    driver.find_element_by_css_selector("[name=lastname]").send_keys("lastname")
    driver.find_element_by_css_selector("[name=address1]").send_keys("adress")
    driver.find_element_by_css_selector("[name=postcode]").send_keys(random.randint(10000,99999))
    driver.find_element_by_css_selector("[name=city]").send_keys("city")
    Select(driver.find_element_by_css_selector("[name=country_code]")).select_by_visible_text("United States")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"[name=zone_code]:enabled [value=AL]")))
    driver.find_element_by_css_selector("select [value=NY]").click()
    email=''.join(choice(ascii_letters) for x in range(16))+"@mmail.com"
    driver.find_element_by_css_selector("[type=email]").send_keys(email)
    driver.find_element_by_css_selector("[name=phone]").send_keys(random.randint(0000000000,9999999999))
    password=random.randint(1234567,9876543)
    driver.find_element_by_css_selector("[name=password]").send_keys(password)
    driver.find_element_by_css_selector("[name=confirmed_password]").send_keys(password)
    driver.find_element_by_css_selector("[name=create_account]").click()
    driver.find_element_by_css_selector("#box-account > div > ul > li:nth-child(4) > a").click()

    #логин
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"[name=email]")))
    driver.find_element_by_css_selector("[name=email]").send_keys(email)
    driver.find_element_by_css_selector("[name=password]").send_keys(password)
    driver.find_element_by_css_selector("[name=login]").click()
    driver.find_element_by_xpath("//*[.='Logout']").click()