import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    #wd = webdriver.Ie()
    #wd = webdriver.Firefox()
    request.addfinalizer(wd.quit)
    return wd

def is_element_present(driver, *args):
    try:
        driver.implicitly_wait(5)
        return len(driver.find_elements(*args))>0
    finally:
        driver.implicitly_wait(0)

def test_basket(driver):
    driver.get("http://localhost/litecart/en/")
    count=3    #количество товаров, добавляемых в корзину
    pcs=1      #количество единиц каждого товара, добавляемого в корзину
    for i in range (count):
        images = driver.find_elements_by_css_selector("div.image-wrapper")
        images[0].click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name=add_cart_product]")))
        #выбираем размер, если присутствует данное поле
        if is_element_present(driver, By.TAG_NAME, "select"):
            driver.find_element_by_css_selector("[value=Medium]").click()
        #указываем количество единиц товара
        driver.find_element_by_css_selector("[name=quantity]").clear()
        driver.find_element_by_css_selector("[name=quantity]").send_keys(pcs)
        #перед тем, как добавить товар в корзину, сохраняем текущее количество товаров в корзине
        cart_item1=driver.find_element_by_css_selector("span.quantity")
        driver.find_element_by_css_selector("[name=add_cart_product]").click()
        #проверяем, что количество товаров в корзине увеличилось
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "span.quantity"), str(int(cart_item1.text) + pcs)))
        driver.find_element_by_css_selector("div#logotype-wrapper").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='box-most-popular']/h3")))

    #открываем корзину и удаляем все товары в ней
    driver.find_element_by_xpath("//*[@id='cart']/a[3]").click()
    while is_element_present(driver, By.CSS_SELECTOR, "[value='Remove']"):
        items1 = driver.find_elements_by_css_selector("td.item")
        driver.find_element_by_css_selector("[value='Remove']").click()
        WebDriverWait(driver, 10).until(lambda driver: len(driver.find_elements_by_css_selector("td.item")) < len(items1))
    is_element_present(driver, By.CSS_SELECTOR, "em")      #дополнительно проверяем, что появилоась надпись "There are no items in your cart"