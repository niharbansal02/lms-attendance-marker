from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import time, datetime, schedule
import json


def getDateToday():
	now = datetime.datetime.now()
	return now.strftime("%a %-d %b %Y")

def getCreds():
	fh = open("creds.json")
	JSON = json.loads(fh.read())

	#return (JSON['username'], JSON['password'])
	return (JSON['email'], JSON['password'])

def wait_find_15(driver, method, path):
	ele = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((method, path)))
	return ele

def getSlot():
	fh = open("creds.json")
	JSON = json.loads(fh.read())
	slots = JSON["slot"]
	return slots
	print(slots)
	fh.close()


def startTheShow():
	options = Options()
	# options.add_argument('--headless')
	# options.add_argument('--disable-gpu') 
	# driver = webdriver.Chrome(CHROMEDRIVER_PATH, )

	# browser = webdriver.Chrome(executable_path=r"/usr/bin/chromedriver", options=options)
	# browser = webdriver.Chrome(options=options)
	browser =webdriver.Chrome('./chromedriver')
	# browser = webdriver.Chrome()
	browser.maximize_window()
	browser.delete_all_cookies()
	browser.get("https://lms-practice-school.bits-pilani.ac.in/my/")
	
	userNameField = "//input[@id='username']"
	passField = "//input[@id='password']"
	#userName, password = getCreds()

	email, password = getCreds()

	if(not email):
		print("Please add your email to creds.json")
	if(not password):
		print("Please add password to creds.json")

	# *Google Login
	oauth_button='//*[@id="region-main"]/div/div[2]/div/div/div/div/div/div[2]/div[3]/div/a'
	email_input='//*[@id="identifierId"]'
	email_next='//*[@id="identifierNext"]/div/button/span'
	pass_input='//*[@id="password"]/div[1]/div/div[1]/input'
	submit='//*[@id="passwordNext"]/div/button/span'
	wait_find_15(browser,By.XPATH,oauth_button).click()
	wait_find_15(browser,By.XPATH,email_input).send_keys(email)
	wait_find_15(browser,By.XPATH,email_next).click()
	wait_find_15(browser,By.XPATH,pass_input).send_keys(password)
	wait_find_15(browser,By.XPATH,submit).click()

	# *Login
	# wait_find_15(browser, By.XPATH, userNameField).send_keys(userName)
	# wait_find_15(browser, By.XPATH, passField).send_keys(password)
	# wait_find_15(browser, By.XPATH, "//button[@id='loginbtn']").click()

	# *Select PS Station
	psName = "//body/div[@id='page-wrapper']/div[@id='page']/div[@id='page-content']/div[@id='region-main-box']/section[@id='region-main']/div[1]/aside[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/a[1]/span[3]"
	wait_find_15(browser, By.XPATH, psName).click()

	# *Select Attendance
	# attendance = "//body/div[@id='page-wrapper']/div[@id='page']/div[@id='page-content']/div[@id='region-main-box']/section[@id='region-main']/div[1]/div[1]/ul[1]/li[2]/div[3]/ul[1]/li[1]/div[1]/div[1]/div[2]/div[1]/a[1]/span[1]"
	# try:
	# 	wait_find_15(browser, By.XPATH, attendance).click()
	try:
		wait_find_15(browser, By.LINK_TEXT, 'Attendance').click()
	except TimeoutException:
		print("No Attendance Section")
		browser.quit()
		return

	present = "//a[contains(text(),'Submit attendance')]"
	try:
		wait_find_15(browser, By.XPATH, present).click()
	except TimeoutException:
		print("Attendance for " + getDateToday() + " already recorded.")
		browser.quit()
		return

	#radio = "//input[@id='id_status_825']"
	radio="//span[contains(text(),'Present')]"
	save_changes = "//input[@id='id_submitbutton']"

	try:
		wait_find_15(browser, By.XPATH, radio).click()
		wait_find_15(browser, By.XPATH, save_changes).click()
		print("Attendance for " + getDateToday() + " recorded.")
	except TimeoutException:
		print("Attendance for " + getDateToday() + " already recorded.")
		

	time.sleep(0.5)

	browser.quit()


if __name__ == "__main__":
	# fh = open("creds.json")
	# JSON = json.loads(fh.read())
	# schedule.every().day.at(JSON["time_24"]).do(startTheShow)
	# while True:
	# 	schedule.run_pending()

	# startTheShow()
	for sl, vl in getSlot().items():
		print(sl, vl[0])

'''
Slot
Morning Attendance		0800 1000
Evening Attendance		1700 1900
'''