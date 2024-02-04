from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


def open_and_sign_in(driver, website_url):
    try:
        driver.get(website_url)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/main/div[1]/div/div[2]/form/div[4]/div/div[2]/button"))).click()

        enter_login_details(driver,login_username,login_password)

    except Exception as e:
        print(f"An error occurred while opening the website and signing in: {e}")

def enter_login_details(driver, username, password):
    global login_page
    try:
        main_page = driver.current_window_handle

        for handle in driver.window_handles:
            if handle != main_page:
                login_page = handle

        driver.switch_to.window(login_page)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div"))
        )

        username_field = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/section/form/fieldset/label[1]/span[2]/input"))
        )

        password_field = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/section/form/fieldset/label[2]/span[2]/input"))
        )

        username_field.send_keys(username)

        password_field.send_keys(password)

        password_field.send_keys(Keys.RETURN)

        iframe_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/iframe"))
        )

        driver.switch_to.frame(iframe_element)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div/div/div[1]/div/form/div[2]/div/label/input"))).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[1]/div/form/div[1]/fieldset/div[1]/button"))
        ).click()

        driver.switch_to.default_content()

        time.sleep(10)
        driver.switch_to.window(main_page)







    except Exception as e:
        print(f"An error occurred while entering login details: {e}")

# Example usage
website_url = "https://cab.brown.edu/"

login_username = "sgsaab"
login_password = "Simba19Pepper47?"

# Start a new instance of Chrome web browser
driver = webdriver.Chrome()

# try:
#     # Call the function to open the website and sign in
#     open_and_sign_in(driver, "https://cab.brown.edu/")
#
#     # Call the function to enter login details
#
#     # Keep the browser open for inspection
#     input("Press Enter to quit.")
#
# finally:
#     # Close the browser
#     driver.quit()

