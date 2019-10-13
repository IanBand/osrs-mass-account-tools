from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

import os
from selenium import webdriver
import json

# clear terminal screen
os.system('cls' if os.name=='nt' else 'clear')

# load settings
with open('settings.json') as json_file:
    settings = json.load(json_file)

    driverPath = settings['driver-path']

    if len(settings['accounts']) > 0:
        manualAccounts = True
        accounts = settings['accounts']
        numberAccounts = len(accounts)
        

    else:
        manualAccounts = False
        numberAccounts = settings['number-accounts']
        password = settings['password']
        baseGoogleAccount = settings['base-google-account']
        startNameIndex = settings['start-name-index']


# instantiate selenium driver
browser = webdriver.Chrome(executable_path=driverPath)


# make accounts
for i in range(0, numberAccounts):

    # prep account information
    if manualAccounts:
        email = accounts[i].email
        password = accounts[i].password
        month = "6"
        day = "6"
        year = "1996"
        

    else:
        email = baseGoogleAccount + '+' + str( i + startNameIndex ) + '@gmail.com'
        month = "6"
        day = "6"
        year = "1996"

    print(email)

    # sign up for account

    # navigate to runescape.com
    browser.get('https://runescape.com')

    delay = 3 # seconds
    try:
        homeDiv = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'home')))
        print "Page is ready!"
    except TimeoutException:
        print "Loading took too much time!"

