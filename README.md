# LMS Attendance Marker

Automatic script for lazy people to mark attendance on LMS for Practice School 1.

## Setup
Add your LMS credentials and time slot to ```creds.json``` \
![Image](credsSS1.png)

## Installation
Run the following to meet the requirements:
`
$ pip install -r requirements.txt
`

- Make sure ```selenium``` and Chrome Webdriver are properly installed.
- If you wish to use any other webdriver, you may change the script accordingly
- The Chrome Webdriver here is for Chrome version 91. If you have some other version of Chrome installed, download the appropriate driver from this [website](https://chromedriver.chromium.org/downloads) and replace it in this folder.

## Run
Run the following command to start:
`
$ python3 attendance.py
`

## Quick FAQs
If you are a first time ```selenium``` user, there might be some errors due to missing dependencies. You may google them and solve.
