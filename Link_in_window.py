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

def test_link_in_window(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.find_element_by_xpath("//*[contains(text(),'Countries')]").click()
    driver.find_element_by_css_selector(".button").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//h1[contains(text(),'Add New Country')]")))

    links=driver.find_elements_by_css_selector(".fa-external-link")
    for i in range(len(links)):
        main_window = driver.current_window_handle
        old_windows = driver.window_handles
        links[i].click()
        new_window = WebDriverWait(driver, 10).until(lambda driver: list(set(driver.window_handles) - set(old_windows))[0])
        driver.switch_to_window(new_window)
        driver.close()
        driver.switch_to_window(main_window)
