from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# Set up the webdriver
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

# Navigate to the login page
driver.get("https://www.saucedemo.com/")

# Enter login details
username_input = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
username_input.send_keys("standard_user")

password_input = wait.until(EC.presence_of_element_located((By.ID, "password")))
password_input.send_keys("secret_sauce")

# Click login button
login_button = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
login_button.click()

# Find the first 4 "ADD TO CART" buttons and click them
for i in range(4):
    add_to_cart_button = driver.find_element(By.CSS_SELECTOR, "button[class='btn btn_primary btn_small btn_inventory']")
    add_to_cart_button.click()

# Go to cart page
cart_icon = driver.find_element(By.CSS_SELECTOR, "a[class='shopping_cart_link']")
cart_icon.click()

# checkout_button = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
checkout_button = driver.find_element(By.ID, "checkout")
checkout_button.click()


# Fill in checkout information
first_name_input = driver.find_element(By.ID, "first-name")
first_name_input.send_keys("Luis")

last_name_input = driver.find_element(By.ID, "last-name")
last_name_input.send_keys("Test")

postal_code_input = driver.find_element(By.ID, "postal-code")
postal_code_input.send_keys("12345")

continue_button = driver.find_element(By.ID, "continue")
continue_button.click()

# Complete purchase
finish_button = driver.find_element(By.ID, "finish")
finish_button.click()

# Verify successful purchase
complete_header = driver.find_element(By.CSS_SELECTOR, "h2[class='complete-header']")
print (complete_header.text)


# Log out
menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
menu_button.click()

#Added this little pause due to it being the only way I found to wait for the element to load, I know theres better ways but I found this one very efficient
time.sleep(0.5)
logout_button = driver.find_element(By.ID, "logout_sidebar_link")
logout_button.click()






# Check if element is present and print message to console
try:
    element = driver.find_element(By.ID, "login_credentials")
    print("You're back in the login page")
except NoSuchElementException:
    print("Something went wrong")
 
