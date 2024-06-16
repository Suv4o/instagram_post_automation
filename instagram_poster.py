import time, pyperclip, platform
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import dotenv_values

env = dotenv_values(".env")


def post_on_instagram(image_path, caption):
    # Configuration
    username = env["INSTAGRAM_USER_NAME"]
    password = env["INSTAGRAM_PASSWORD"]

    # Initialize WebDriver
    webdriver_service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=webdriver_service)
    wait = WebDriverWait(driver, 10)

    # Set window size
    driver.set_window_size(1500, 900)  # width, height

    # Navigate to Instagram
    driver.get("https://www.instagram.com")

    # Log in
    wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(
        username
    )
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)

    time.sleep(10)
    driver.find_element(By.XPATH, '//div[text()="Not now"]').click()

    time.sleep(5)
    driver.find_element(By.XPATH, '//button[text()="Not Now"]').click()

    time.sleep(5)
    driver.find_element(By.XPATH, '//span[text()="Create"]').click()

    time.sleep(5)
    driver.find_element(By.XPATH, '//span[text()="Post"]').click()

    time.sleep(5)
    driver.find_element(By.XPATH, '//input[@type="file"]').send_keys(image_path)

    time.sleep(10)
    driver.find_element(By.XPATH, '//div[text()="Next"]').click()

    time.sleep(5)
    driver.find_element(By.XPATH, '//div[text()="Next"]').click()

    time.sleep(5)
    caption_element = driver.find_element(
        By.XPATH, '//div[@aria-label="Write a caption..."]'
    )

    pyperclip.copy(caption)
    act = ActionChains(driver)
    caption_element.click()

    # Check the operating system
    if platform.system() == "Darwin":  # Darwin stands for Mac OS
        paste_key = Keys.COMMAND
    else:
        paste_key = Keys.CONTROL

    # Perform the paste operation
    act.key_down(paste_key).send_keys("v").key_up(paste_key).perform()

    time.sleep(5)
    driver.find_element(By.XPATH, '//div[text()="Share"]').click()

    # Wait for post to upload
    time.sleep(20)

    # Close WebDriver
    driver.quit()
