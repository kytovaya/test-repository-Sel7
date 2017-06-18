import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def test_add_new_product(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.find_element_by_xpath("//*[contains(text(),'Catalog')]").click()
    driver.find_element_by_xpath("//*[contains(text(),'Add New Product')]").click()

    #вкладка General
    driver.find_element_by_css_selector("label>[value='1']").click()
    driver.find_element_by_name("name[en]").send_keys("Duck123")
    driver.find_element_by_name("code").send_keys("123")
    driver.find_element_by_css_selector("div#tab-general tr:nth-child(4) tr:nth-child(1) td:nth-child(1)").click()
    driver.find_element_by_css_selector("div#tab-general tr:nth-child(4) tr:nth-child(2) td:nth-child(1)").click()
    driver.find_element_by_css_selector("div#tab-general tr:nth-child(7) tr:nth-child(2) td:nth-child(1)").click()
    driver.find_element_by_name("quantity").clear()
    driver.find_element_by_name("quantity").send_keys("50")
    driver.find_element_by_name("new_images[]").send_keys(os.getcwd() + "/duck123.jpg")
    driver.find_element_by_name("date_valid_from").send_keys("18062017")
    driver.find_element_by_name("date_valid_to").send_keys("18062018")

    #вкладка Informarion
    driver.find_element_by_css_selector(".index li:nth-child(2)").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//*[contains(text(),'Description')]")))
    driver.find_element_by_css_selector("select[name=manufacturer_id] [value='1']").click()
    driver.find_element_by_name("keywords").send_keys("duck123")
    driver.find_element_by_name("short_description[en]").send_keys("Short description about duck123")
    driver.find_element_by_css_selector(".trumbowyg-editor").send_keys("Description about duck123")
    driver.find_element_by_name("head_title[en]").send_keys("Head title for duck123")
    driver.find_element_by_name("meta_description[en]").send_keys("Meta description for duck123")

    #вкладка Prices
    driver.find_element_by_css_selector(".index li:nth-child(4)").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div#tab-prices")))
    driver.find_element_by_name("purchase_price").clear()
    driver.find_element_by_name("purchase_price").send_keys("60")
    driver.find_element_by_css_selector("select[name=purchase_price_currency_code] [value=USD]").click()
    driver.find_element_by_name("gross_prices[USD]").clear()
    driver.find_element_by_name("gross_prices[USD]").send_keys("80")
    driver.find_element_by_name("gross_prices[EUR]").clear()
    driver.find_element_by_name("gross_prices[EUR]").send_keys("100")

    driver.find_element_by_name("save").click()