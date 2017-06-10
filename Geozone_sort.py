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

def test_geozone_sort(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"li#app-")))
    driver.find_element_by_xpath("//*[@id='app-']/a/span[2][contains(text(),'Geo Zones')]").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Geo Zones')]")))
    country_names=driver.find_elements_by_css_selector("td:nth-child(3) > a") #получаем список стран
    lenght=len(country_names)
    for i in range(lenght):
        country_names[i].click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Edit Geo Zone')]")))
        zones=driver.find_elements_by_css_selector("td:nth-child(3) > select > [selected=selected]")
        lenght1=len(zones)-1
        for k in range(lenght1): #проверяем, что зоны расположены в алфавитном порядке
            print(zones[k].text)
            assert(zones[k].get_attribute("innerText") < zones[k+1].get_attribute("innerText"))
        driver.back()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Geo Zones')]")))
        country_names=driver.find_elements_by_css_selector("td:nth-child(3) > a")

