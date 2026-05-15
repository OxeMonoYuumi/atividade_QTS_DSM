from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Teste modo incorreto com time.sleep
def test_create_user_e2e():
    options = Options()

    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    driver.get("http://localhost:5000")

    input_name = driver.find_element(By.ID, "name")
    input_name.send_keys("Pedro")

    button = driver.find_element(By.ID, "submit")
    button.click()

    from selenium.webdriver.support.ui import WebDriverWait

    wait = WebDriverWait(driver, 5)

    wait.until(
        lambda d: any("Pedro" in el.text for el in d.find_elements(By.TAG_NAME, "li"))
    )

    users = driver.find_elements(By.TAG_NAME, "li")

    assert any("Pedro" in user.text for user in users)

    driver.quit()