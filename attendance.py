from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import datetime, schedule
import json

def repeater(func):
	while True:
		try:
			retVal = func()
			break
		except:
			continue
	
	return retVal

def getDateToday():
	now = datetime.datetime.now()
	return now.strftime("%a %-d %b %Y")

def getCreds():
	fh = open("creds.json")
	JSON = json.loads(fh.read())

	return (JSON['username'], JSON['password'])

def wait_find_15(driver, method, path):
	ele = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((method, path)))
	return ele

def startTheShow():
	browser = webdriver.Chrome(executable_path=r"/usr/bin/chromedriver")
	browser.maximize_window()
	browser.delete_all_cookies()
	repeater(lambda: browser.get("https://lms-practice-school.bits-pilani.ac.in/my/"))
	

	userNameField = "//input[@id='username']"
	passField = "//input[@id='password']"
	userName, password = getCreds()

	if(not userName):
		print("Please add your username to creds.json")
	if(not password):
		print("Please add password to creds.json")

	# *Login
	wait_find_15(browser, By.XPATH, userNameField).send_keys(userName)
	wait_find_15(browser, By.XPATH, passField).send_keys(password)
	wait_find_15(browser, By.XPATH, "//button[@id='loginbtn']").click()

	# *Select PS Station
	psName = "//body/div[@id='page-wrapper']/div[@id='page']/div[@id='page-content']/div[@id='region-main-box']/section[@id='region-main']/div[1]/aside[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/a[1]/span[3]"
	wait_find_15(browser, By.XPATH, psName).click()

	# *Mark as done Button
	markAsDone = "//body/div[@id='page-wrapper']/div[@id='page']/div[@id='page-content']/div[@id='region-main-box']/section[@id='region-main']/div[1]/div[1]/ul[1]/li[2]/div[3]/ul[1]/li[1]/div[1]/div[1]/div[2]/div[2]/div[1]/button[1]"
	try:
		markEle = wait_find_15(browser, By.XPATH, markAsDone)
	except TimeoutException:
		print("No Attendance section OR No Button 'Mark as Done' or 'Done'")
		browser.quit()
		return

	# print(markEle.text)

	if(markEle.text == "Mark as done"):
		markEle.click()
		print("Attendance for " + getDateToday() + " recorded.")
	else:
		print("Attendance for " + getDateToday() + " already recorded.")

	input()

	browser.quit()



if __name__ == "__main__":
	fh = open("creds.json")
	JSON = json.loads(fh.read())
	schedule.every().day.at(JSON["time_24"]).do(startTheShow)
	while True:
		schedule.run_pending()

	# startTheShow