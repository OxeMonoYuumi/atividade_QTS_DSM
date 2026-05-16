from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


def test_create_product_e2e():

    options = Options()

    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    driver.get("http://localhost:5000/products/page")

    input_name = driver.find_element(By.ID, "name")
    input_quantity = driver.find_element(By.ID, "quantity")

    input_name.send_keys("Notebook")
    input_quantity.send_keys("10")

    button = driver.find_element(By.ID, "submit")
    button.click()

    wait = WebDriverWait(driver, 5)

    wait.until(
        lambda d: any(
            "Notebook" in el.text for el in d.find_elements(By.TAG_NAME, "li")
        )
    )

    products = driver.find_elements(By.TAG_NAME, "li")

    assert any("Notebook" in product.text for product in products)

    driver.quit()


def test_create_multiple_products_e2e():

    options = Options()

    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    driver.get("http://localhost:5000/products/page")

    input_name = driver.find_element(By.ID, "name")
    input_quantity = driver.find_element(By.ID, "quantity")

    input_name.send_keys("Mouse")
    input_quantity.send_keys("20")

    button = driver.find_element(By.ID, "submit")
    button.click()

    wait = WebDriverWait(driver, 5)

    wait.until(lambda d: "Mouse" in d.page_source)

    products = driver.find_elements(By.TAG_NAME, "li")

    assert any("Mouse" in product.text for product in products)

    input_name = driver.find_element(By.ID, "name")
    input_quantity = driver.find_element(By.ID, "quantity")

    input_name.clear()
    input_quantity.clear()

    input_name.send_keys("Teclado")
    input_quantity.send_keys("15")

    button = driver.find_element(By.ID, "submit")
    button.click()

    wait.until(lambda d: "Teclado" in d.page_source)

    products = driver.find_elements(By.TAG_NAME, "li")

    assert any("Teclado" in product.text for product in products)

    driver.quit()


def test_create_products_and_validate_stock():

    options = Options()

    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    driver.get("http://localhost:5000/products/page")

    input_name = driver.find_element(By.ID, "name")
    input_quantity = driver.find_element(By.ID, "quantity")

    input_name.send_keys("Monitor")
    input_quantity.send_keys("8")

    button = driver.find_element(By.ID, "submit")
    button.click()

    wait = WebDriverWait(driver, 5)

    wait.until(lambda d: "Monitor" in d.page_source)

    products = driver.find_elements(By.TAG_NAME, "li")

    assert any("Monitor" in product.text for product in products)

    input_name = driver.find_element(By.ID, "name")
    input_quantity = driver.find_element(By.ID, "quantity")

    input_name.clear()
    input_quantity.clear()

    input_name.send_keys("Headset")
    input_quantity.send_keys("12")

    button = driver.find_element(By.ID, "submit")
    button.click()

    wait.until(lambda d: "Headset" in d.page_source)

    products = driver.find_elements(By.TAG_NAME, "li")

    assert any("Monitor" in product.text for product in products)
    assert any("Headset" in product.text for product in products)

    driver.quit()
