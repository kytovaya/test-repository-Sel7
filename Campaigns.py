import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    #wd = webdriver.Firefox()
    #wd = webdriver.Ie()
    request.addfinalizer(wd.quit)
    return wd

#проверяем, что цвет цены - серый и цена перечеркнута
def grey_line_through(price):
    color=price.value_of_css_property("color")
    canal=color[5:-2].split(', ')     #для теста в Chrome, Ie
    #canal=color[4:-1].split(', ')    #для теста в Firefox
    if (canal[0]!=canal[1] or canal[1]!=canal[2] or canal[0]=='0' or canal[0]=='255'):
        print("Color isn't grey!")
    if price.value_of_css_property("text-decoration-line")!='line-through':
    #if price.value_of_css_property("text-decoration")!='line-through':    #для теста в Ie
        print("Regular price isn't line-through")

#проверяем, что цвет цены - красный и цена выделена жирным
def red_bold(price):
    color=price.value_of_css_property("color")
    canal=color[5:-2].split(', ')   #для теста в Chrome, Ie
    #canal=color[4:-1].split(', ')  #для теста в Firefox
    if canal[0]=='0' or canal[1]!='0'or canal[2]!='0':
        print("Color isn't red!")
    if price.value_of_css_property("font-weight")!='bold':
    #if price.value_of_css_property("font-weight")<'700':      #для теста в Firefox, Ie
        print("Campaign price isn't bold!")

def test_campaigns(driver):
    driver.get("http://localhost/litecart/en/")
    regular_price=driver.find_element_by_css_selector("div#box-campaigns li:first-of-type .regular-price")
    campaign_price=driver.find_element_by_css_selector("div#box-campaigns li:first-of-type .campaign-price")
    print("Основная страница")
    grey_line_through(regular_price) #проверяем, что цвет основной цены - серый и цена перечеркнута
    red_bold(campaign_price)         #проверяем, что цвет акционной цены - красный и цена выделена жирным

    #прверяем, что акционная цена крупнее, чем обычная
    if ((regular_price.value_of_css_property('font-size') >= campaign_price.value_of_css_property('font-size'))):
        print("Campaign price isn't large!")

    #перед тем, как уйти со страницы, сохраняем текст названия товара и цены в переменные
    name=driver.find_element_by_css_selector("div#box-campaigns li:first-of-type .name")
    nametext=name.text
    reg_pricetext=regular_price.text
    camp_pricetext=campaign_price.text
    name.click();

    #проверяем, что на главной странице и на странице товара совпадает текст названия товара и цены
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='box-product']")))
    regular_price=driver.find_element_by_css_selector(".regular-price")
    campaign_price=driver.find_element_by_css_selector(".campaign-price")
    if driver.find_element_by_css_selector("h1.title").text!=nametext:
        print("Names isn't equals!")
    if regular_price.text!=reg_pricetext:
        print("Regular price isn't equals!")
    if campaign_price.text!=camp_pricetext:
        print("Campaign price isn't equals!")

    print("Страница товара")
    grey_line_through(regular_price) #проверяем, что цвет основной цены - серый и цена перечеркнута
    red_bold(campaign_price)         #проверяем, что цвет акционной цены - красный и цена выделена жирным

    #прверяем, что акционная цена крупнее, чем обычная
    if ((regular_price.value_of_css_property('font-size') >= campaign_price.value_of_css_property('font-size'))):
        print("Campaign price isn't large!")



