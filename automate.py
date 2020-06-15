# Import modules
from datetime import datetime as dt, timedelta
from time import sleep
from random import randint
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import config

# Wait a random number of seconds
max_mins = 10
max_seconds = 60 * max_mins
random_seconds = randint(max_seconds)
current_datetime = dt.now()
start_datetime = current_datetime + timedelta(seconds=random_seconds)
print(f'Current datetime: {current_datetime}')
print(f'Start datetime: {start_datetime}')
sleep(random_seconds)

# Instantiate driver
driver_path = '/usr/local/bin/chromedriver'
browser = webdriver.Chrome(driver_path)

# Go to URL
garnet_url = 'https://ga-garnet-production.herokuapp.com/sign_in'
browser.get(garnet_url)

# Authenticate using GitHub
github_button = browser.find_element_by_class_name('github')
github_button.click()

# Login to GitHub
if 'github.com' in browser.current_url:
    user_field = browser.find_element_by_id('login_field')
    password_field = browser.find_element_by_id('password')
    gh_sign_in_button = browser.find_element_by_class_name('btn-primary')

    user_field.send_keys(config.user_name)
    password_field.send_keys(config.password)
    gh_sign_in_button.click()

# Go to attendance page
attendance_url = 'https://ga-garnet-production.herokuapp.com/memberships/3058'
browser.get(attendance_url)

# Check in automatically (if button is present)
try:
    check_in_button = browser.find_element_by_tag_name('button')
    check_in_button.click()
    print('Successfully checked in!')
except NoSuchElementException:
    print('Unable to find check-in button.')

# Quit browser afterwards
sleep(10)
browser.quit()
