import time
from selenium import webdriver
from csv import reader
from selenium.webdriver.common.by import By

with open('exsample.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    list_of_rows = list(csv_reader)
def Connecting_To_driver(email, password):
    if email != "" and password != "":
        try:

            c = webdriver.ChromeOptions()
            c.add_argument("--incognito")
            driver = webdriver.Chrome(options=c)
            driver.get('https://www.exsample.com')
            time.sleep(4)
            driver.find_element(By.XPATH,"email").send_keys(email)
            time.sleep(1)
            driver.find_element(By.XPATH,"password").send_keys(password)
            time.sleep(1)
            driver.find_element(By.XPATH, "/button").click()
            time.sleep(5)

        except Exception as e:
            print(f"Error occurred while logging in with ID: {email}")
            print(e)
            driver.delete_all_cookies()
            driver.quit()
            return False

    else:
        print("Either ID or PASSWORD is null")
        return False


