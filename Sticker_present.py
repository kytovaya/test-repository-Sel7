import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def are_elements_present(a, *args):
    return len(a.find_elements(*args))>0

def test_example(driver):
    driver.get("http://localhost/litecart/en/")
    images = driver.find_elements_by_css_selector("div.image-wrapper")
    quantity = len(images)
    n=0
    for i in range(quantity):
        if (len(images[i].find_elements_by_css_selector("div.sticker")) > 0):
            if (len(images[i].find_elements_by_css_selector("div.sticker")) > 1):
                print("images: ", i, images[i], "stickers: ", images[i].find_elements_by_css_selector("div.sticker"))
                n=1
        else:
            print("No image sticker: ", i, images[i])
            n=1
    if n==0:
        print("Only one sticker for each image on the page!")
