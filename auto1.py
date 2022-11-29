from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import time
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import numpy as np

class Automation_101():
    def locate_by_regex(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        df = pd.read_excel('Automation_demo_1.xlsx')
        #for i in range(2):
        link = df['Source'][0]
        driver.get(link)
        driver.maximize_window()
        # driver.find_element(By.LINK_TEXT,"Yatra for Business").click()
        # driver.find_element(By.XPATH,"(//input[contains(@class,'wd100 ng-pristine ng-valid-email ng-invalid ng-invalid-required ng-valid-pattern ng-touched')])[1]").send_keys("demo@test.com")
        # driver.find_element(By.XPATH,"//span[normalize-space()='Investor Relations']").click()
        # tx = driver.find_element(By.XPATH,"//a[@class='dropdown-toggle eventTrackable list-dropdownNull ytBusinessTrack']").text
        # print(tx)
        
        page_source = driver.page_source
        email_regex = r'''(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])'''
        list_of_emails = []
        
        # attr_value = driver.find_element(By.XPATH,"//input[@id='login_button']").is_enabled()
        # print(attr_value)
        # driver.find_element(By.XPATH,"//input[@id='user_name']").send_keys("testing")
        # driver.find_element(By.XPATH,"//input[@id='user_pass']").send_keys("testing12")
        # check = driver.find_element(By.XPATH,"//input[@id='login_button']").is_enabled()
        # print(check)
        # display_check = driver.find_element(By.XPATH,"//div[@id='myDIV']").is_displayed()
        # print(display_check)
        # driver.find_element(By.XPATH,"//button[normalize-space()='Toggle Hide and Show']").click()
        # d_c1= driver.find_element(By.XPATH,"//div[@id='myDIV']").is_displayed()
        # print(d_c1)
        # driver.find_element(By.XPATH,"//a[normalize-space()='Non Stop Flights']").click()
        
        for re_match in re.finditer(email_regex, page_source):
            list_of_emails.append(re_match.group())

        for email in enumerate(list_of_emails):
            print(email)
            
        # print(driver.find_element(By.XPATH,"//a[normalize-space()='Non Stop Flights']").is_selected())
        # time.sleep(2)
        # print(driver.find_element(By.XPATH,"//a[normalize-space()='Student Fare']").is_selected())
        # driver.find_element(By.XPATH,"//a[normalize-space()='Student Fare']").click()
        # driver.find_element(By.LINK_TEXT, "info@savvsenergi.se")
        
        arr = np.array([list_of_emails])
        arr1 = np.transpose(arr)
        arr2 = np.unique(arr1)
        pd.DataFrame(arr2).to_excel('scrape_data.xlsx') 
        time.sleep(2)


scraper1 = Automation_101()
for i in range(1):
    scraper1.locate_by_regex()