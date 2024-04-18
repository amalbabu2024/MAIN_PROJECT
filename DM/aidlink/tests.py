# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException, NoSuchElementException

# # Create a new instance of the Chrome driver
# driver = webdriver.Chrome()

# try:
#     # Navigate to the login page
#     driver.get("http://127.0.0.1:8000/accounts/login/")  # Update with the actual URL of the login page

#     # Wait for the login form to appear
#     username_elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
#     password_elem = driver.find_element(By.ID, "password")

#     # Enter username and password
#     username_elem.send_keys("milton")
#     password_elem.send_keys("Milton@123")

#     print("username and password entered successful!")

#     # Submit the login form
#     password_elem.send_keys(Keys.RETURN)

#     print("Login Button Clicked Successfully")

#     # Wait for the logout button to appear
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "logout-button")))

#     print("Login successful!")

# except TimeoutException:
#     print("Login form elements not found within the specified time.")
# except NoSuchElementException:
#     print("Login form elements not found.")
# except Exception as e:
#     print(f"An error occurred: {e}")

# finally:
#     # Close the browser
#     driver.quit()





# 1. login testing


import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_successful_login(self):
        self.driver.get('http://127.0.0.1:8000/accounts/login/')
        username_input = self.driver.find_element(By.ID, 'username')
        password_input = self.driver.find_element(By.ID, 'password')

        # Replace 'valid_username' and 'valid_password' with actual credentials
        username_input.send_keys('milton')
        password_input.send_keys('Milton@123')

        print("Entered username and password Successfully.")

        login_button = self.driver.find_element(By.ID, 'login')
        login_button.click()

        time.sleep(2)  # Adjust the time as needed

        print("Clicked on login button Successfully.")

        # Check if redirected to the ownerpage
        self.assertIn('http://127.0.0.1:8000/teamleaderdashboard/', self.driver.current_url.lower())
        print("Successfully logged in.")






# 2. Add Organization Resouces By the Team Leader

# import time
# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

# class LoginTest(unittest.TestCase):

#     def setUp(self):
#         self.driver = webdriver.Chrome()


#     def test_successful_login(self):
#         self.driver.get('http://127.0.0.1:8000/accounts/login/')
#         username_input = self.driver.find_element(By.ID, 'username')
#         password_input = self.driver.find_element(By.ID, 'password')

#         # Replace 'valid_username' and 'valid_password' with actual credentials
#         username_input.send_keys('milton')
#         password_input.send_keys('Milton@123')

#         login_button = self.driver.find_element(By.ID, 'login')
#         login_button.click()

#         time.sleep(2)  # Adjust the time as needed

#         # Check if redirected to the dashboard
#         self.assertIn('http://127.0.0.1:8000/teamleaderdashboard/', self.driver.current_url.lower())
#         print("Successfully logged in.")

#         # Navigate to the "Add resources" page
#         add_resources_link = self.driver.find_element(By.XPATH, "//a[contains(@href, '/add_organization_resources')]")
#         add_resources_link.click()

#         time.sleep(2)  # Adjust the time as needed

#         # Check if redirected to the "Add resources" page
#         self.assertIn('http://127.0.0.1:8000/add_organization_resources/', self.driver.current_url.lower())
#         print("Successfully navigated to the 'Add resources' page.")

#         # Fill out the form and submit it
#         resource_name_input = self.driver.find_element(By.ID, 'ResourceName')
#         description_input = self.driver.find_element(By.ID, 'Description')
#         quantity_input = self.driver.find_element(By.ID, 'Quantity')
#         resource_type_select = self.driver.find_element(By.ID, 'ResourceType')

#         # Fill out the form fields
#         resource_name_input.send_keys('Sample Resource')
#         description_input.send_keys('This is a sample resource description.')
#         quantity_input.send_keys('10')
#         resource_type_select.send_keys('Equipment')

#         # Submit the form
#         submit_button = self.driver.find_element(By.XPATH, "//input[@type='submit']")
#         submit_button.click()

#         time.sleep(2)  # Adjust the time as needed

#         # Check if redirected to the dashboard or a success page
#         self.assertIn('http://127.0.0.1:8000/view_organization_resources/', self.driver.current_url.lower())
#         print("Successfully added the resource.")
