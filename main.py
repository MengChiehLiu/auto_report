'''
TSMC daily temperature automatically report
Author: Meng-Chieh, Liu
Date: 2022/7/13
'''

# import packages
from selenium import webdriver
import time
from datetime import date 
from random import randint 


# config
today = date.today().strftime("%m/%d/%Y")
temperature = '36.'+str(randint(3,8))
idx = '135163'

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
opt = webdriver.ChromeOptions()
opt.add_argument('--user-agent=%s' % user_agent)
browser = webdriver.Chrome(executable_path="chromedriver.exe")

url = 'https://zh.surveymonkey.com/r/EmployeeHealthCheck'
browser.get(url) 
time.sleep(randint(1,3))

agree = browser.find_elements_by_xpath('//*[@id="66405067_542650090_label"]/span[1]')[0]
agree.click()
time.sleep(randint(1,3))

question_1 = browser.find_elements_by_xpath('//*[@id="66405064"]')[0]
question_1.send_keys(idx)
time.sleep(randint(1,3))

question_2 = browser.find_elements_by_xpath('//*[@id="66405069_542650092_label"]/span[2]')[0]
question_2.click()
time.sleep(randint(1,3))


question_3_1 = browser.find_elements_by_xpath('//*[@id="66405065"]')[0]
question_3_1.send_keys(temperature)
time.sleep(randint(1,3))

question_3_2 = browser.find_elements_by_xpath('//*[@id="question-field-66405075"]/fieldset/div/div[1]/div[1]/div/label/span[1]')[0]
question_3_2.click()
time.sleep(randint(1,3))

question_3_3 = browser.find_elements_by_xpath('//*[@id="66405078_542650167_label"]')[0]
question_3_3.click()
time.sleep(randint(1,3))

question_3_3_2 = browser.find_elements_by_xpath('//*[@id="66405129_542650744_DMY"]')[0]
question_3_3_2.send_keys(today)
time.sleep(randint(1,3))

question_4_1 = browser.find_elements_by_xpath('//*[@id="66405074_542650161_label"]/span[1]')[0]
question_4_1.click()
time.sleep(randint(1,3))

question_4_2 = browser.find_elements_by_xpath('//*[@id="66405076_542650156_label"]/span[1]')[0]
question_4_2.click()
time.sleep(randint(1,3))

question_4_3 = browser.find_elements_by_xpath('//*[@id="66405066_542650082_label"]/span[1]')[0]
question_4_3.click()
time.sleep(randint(1,3))


submit = browser.find_elements_by_xpath('//*[@id="66405129_542650744_DMY"]')[0]
submit.click()
time.sleep(randint(1,3))

browser.close()