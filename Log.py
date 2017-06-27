import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def test_log(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")
    list = driver.find_elements_by_xpath("//td[3]/a")
    for i in range(len(list)-1):
        list = driver.find_elements_by_xpath("//td[3]/a")
        list[i+1].click()
        assert(len(driver.get_log("browser")) == 0)
        driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")

