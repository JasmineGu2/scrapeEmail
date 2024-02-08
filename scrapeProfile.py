#Find the profile of people
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from collections import defaultdict
from selenium.webdriver.chrome.service import Service

from readCompany import comp

s=Service('./chromedriver')
driver = webdriver.Chrome(service=s)
url='https://www.google.com'
driver.get(url)


list = ["software engineer"]

company = comp()
driver.implicitly_wait(5)


f = open('profile.csv', 'a')

# create the csv writer
writer = csv.writer(f)

count = 0
start = time.time()
#launch URL
time.sleep(2)
for j in range(len(company)):
    for i in range(len(list)):
        end = time.time()
        difference = end - start
        print(difference)
        #identify search box
        m = driver.find_element(By.NAME,"q")
        #enter search text
        m.send_keys(list[i] + ' "Linkedin.com" profile at '+ company[j] + ' Toronto')
        
        #perform Google search with Keys.ENTER
        #m.send_keys(Keys.ENTER)
        driver.implicitly_wait(0.5)
        #time.sleep(2)
        count = 1
        count2 = 0
        m.send_keys(Keys.ENTER)
        time.sleep(2)
        while True:
            print("iteration " + str(count2))
            # Find all elements matching the specified XPath
            elements = driver.find_elements(By.XPATH, "//*[@class='RVQdVd']")

            # Check if any elements are found
            if not elements:
                break  # Exit the loop if no elements are found

            # Iterate through the elements and click each one
            for element in elements:
                count2 +=1 
                try: # Wait for the element to be clickable (adjust timeout as needed)
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[@class='RVQdVd']")))
                    element.click()
                    count -= 1
                except:
                    print("cant click")
                    count += 1
            if count >= 8:
                break
            
            element = None
            time.sleep(1)
        
        
        time.sleep(2)
        name = driver.find_elements(By.XPATH,"//*[@class='LC20lb MBeuO DKV0Md']")
   
        for element in name:
            print(element.text)
            # Write this into a file called profileContent
            # Info is an array [company name, and the text ]
            info = [company[j],element.txt]
            writer.writerows(info)
    
        
driver.close()



