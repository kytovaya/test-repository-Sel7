import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get("http://www.google.com/")
    driver.find_element_by_name("q").send_keys("гисметео симферополь")
    driver.find_element_by_name("btnG").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='rso']/div/div/div[1]/div/div/h3/a")))
    driver.find_element_by_partial_link_text("GISMETEO: погода в Симферополе").click()