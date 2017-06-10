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

def test_country_zone_sort(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"li#app-")))
    driver.find_element_by_xpath("//*[@id='app-']/a/span[2][contains(text(),'Countries')]").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Countries')]")))
    country_names=driver.find_elements_by_css_selector("td:nth-child(5) > a")
    lenght=len(country_names)
    for i in range(lenght-1):       #проверяем, что страны расположены в алфавитном порядке
        assert(country_names[i].text < country_names[i+1].text)
    count_zones=driver.find_elements_by_css_selector("td:nth-child(6)")
    for j in range(lenght):
        if (count_zones[j].get_attribute("innerText")!="0"): #находим страны, у которых количество зон отлично от нуля
            country_names[j].click()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Edit Country')]")))
            zones=driver.find_elements_by_css_selector(".dataTable td:nth-child(3)")
            lenght1=len(zones)-2
            for k in range(lenght1): #проверяем, что зоны расположены в алфавитном порядке
                assert(zones[k].get_attribute("innerText") < zones[k+1].get_attribute("innerText"))
            driver.back()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Countries')]")))
            country_names=driver.find_elements_by_css_selector("td:nth-child(5) > a")
            count_zones=driver.find_elements_by_css_selector("td:nth-child(6)")



