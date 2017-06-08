import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def are_elements_present(driver, *args):
    return len(driver.find_elements(*args))>0

def test_click_menu(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    items = driver.find_elements_by_css_selector("li#app-")
    lenght = len(items)
    for i in range(lenght):
        items = driver.find_elements_by_css_selector("li#app-")
        items[i].click()
        points = driver.find_elements_by_css_selector(".selected > .docs > li")
        lenght1 = len(points)
        for j in range (lenght1):
            points = driver.find_elements_by_css_selector(".selected > .docs > li")
            points[j].click()
            are_elements_present(driver, By.TAG_NAME, "h1")
            print(driver.find_element_by_tag_name("h1").text)


