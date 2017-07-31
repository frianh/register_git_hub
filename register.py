#!/usr/bin/env python

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

'Edit profile'
def edit_profile(skype, linked, twitter, website, location, bio, countcpt):
    findByCss('a.header-user-dropdown-toggle > i.fa.fa-caret-down').click()
    time.sleep(0.5)
    findByLink('Profile').click()
    time.sleep(0.5)
    findByCss('i.fa.fa-pencil').click()
    time.sleep(0.5)
    countcpt = countcpt + 1
    namescr = "reg_" + str(i) + "_" + str(countcpt)
    driver.save_screenshot(namescr)

    findById('search').send_keys(Keys.PAGE_DOWN)

    time.sleep(1)
    countcpt = countcpt + 1
    namescr = "reg_" + str(i) + "_" + str(countcpt)
    driver.save_screenshot(namescr)

    findById('user_skype').send_keys(skype)
    findById('user_linkedin').send_keys(linked)
    findById('user_twitter').send_keys(twitter)
    findById('user_website_url').send_keys(website)
    findById('user_location').send_keys(location)
    findById('user_bio').send_keys(bio)

    countcpt = countcpt + 1
    namescr = "reg_" + str(i) + "_" + str(countcpt)
    driver.save_screenshot(namescr)

    findByName('commit').click()
    time.sleep(0.5)
    countcpt = countcpt + 1
    namescr = "reg_" + str(i) + "_" + str(countcpt)
    driver.save_screenshot(namescr)

    findById('search').send_keys(Keys.PAGE_UP)

    time.sleep(1)
    countcpt = countcpt + 1
    namescr = "reg_" + str(i) + "_" + str(countcpt)
    driver.save_screenshot(namescr)

    findByCss('a.header-user-dropdown-toggle > i.fa.fa-caret-down').click()
    time.sleep(0.5)
    findByLink('Sign out').click()
    time.sleep(0.5)



temp = ""
a = ""
b = ""
c = ""
d = ""
e = ""
f = ""

# Master loop
for i in range(1, 8):
    'Open browser'
    driver = webdriver.Chrome()
    driver.get("http://10.0.50.210")
    driver.maximize_window()

    countcpt = 0

    #Set variable
    if i == 1:
        name = ""
        userName = "automation7"
        email = "automation7@yahoo.com"
        emailConf = "automation7@yahoo.com"
        pwd = "tes1234567"
        skype = "skpy6"
        linked = "liknd6"
        twitter = "twt6"
        website = "web6"
        location = "loc6"
        bio = "bio6"
    elif i == 2:
        name = "automation7"
        userName = ""
        email = "automation7@yahoo.com"
        emailConf = "automation7@yahoo.com"
        pwd = "tes1234567"
        skype = "skpy6"
        linked = "liknd6"
        twitter = "twt6"
        website = "web6"
        location = "loc6"
        bio = "bio6"
    elif i == 3:
        name = "automation7"
        userName = "automation7"
        email = ""
        emailConf = "automation7@yahoo.com"
        pwd = "tes1234567"
        skype = "skpy6"
        linked = "liknd6"
        twitter = "twt6"
        website = "web6"
        location = "loc6"
        bio = "bio6"
    elif i == 4:
        name = "automation7"
        userName = "automation7"
        email = "automation7@yahoo.com"
        emailConf = ""
        pwd = "tes1234567"
        skype = "skpy6"
        linked = "liknd6"
        twitter = "twt6"
        website = "web6"
        location = "loc6"
        bio = "bio6"
    elif i== 5:
        name = "automation7"
        userName = "automation7"
        email = "automation7@yahoo.com"
        emailConf = "automation7@yahoo.com"
        pwd = ""
        skype = "skpy6"
        linked = "liknd6"
        twitter = "twt6"
        website = "web6"
        location = "loc6"
        bio = "bio6"
    elif i == 6:
        name = "automation7"
        userName = "automation7"
        email = "automation7@yahoo.com"
        emailConf = "automation7@yahoo.com"
        pwd = "tes"
        skype = "skpy6"
        linked = "liknd6"
        twitter = "twt6"
        website = "web6"
        location = "loc6"
        bio = "bio6"
    elif i == 7:
        name = "automation7"
        userName = "automation7"
        email = "automation7@yahoo.com"
        emailConf = "automation7@yahoo.com"
        pwd = "tes1234567"
        skype = "skpy6"
        linked = "liknd6"
        twitter = "twt6"
        website = "web6"
        location = "loc6"
        bio = "bio6"

    findById = driver.find_element_by_id
    findByLink = driver.find_element_by_link_text
    findByCss = driver.find_element_by_css_selector
    findByName = driver.find_element_by_name
    findByXPath = driver.find_element_by_xpath

    findByLink('Register').click()
    time.sleep(0.5)
    countcpt = countcpt + 1
    namescr = "reg_" + str(i) + "_" + str(countcpt)
    time.sleep(2)
    driver.save_screenshot(namescr)
    time.sleep(2)
    findById('new_user_name').send_keys(name)
    time.sleep(2)
    findById('new_user_username').send_keys(userName)
    time.sleep(2)
    findById('new_user_email').send_keys(email)
    time.sleep(2)
    findById('new_user_email_confirmation').send_keys(emailConf)
    time.sleep(2)
    findById('new_user_password').send_keys(pwd)

    time.sleep(0.5)
    countcpt = countcpt + 1
    namescr = "reg_" + str(i) + "_" + str(countcpt)
    driver.save_screenshot(namescr)
    findByXPath("(//input[@name='commit'])[2]").click()
    time.sleep(2)
    countcpt = countcpt + 1
    namescr = "reg_" + str(i) + "_" + str(countcpt)
    driver.save_screenshot(namescr)

    try:
        if findByCss('h2.blank-state-welcome-title').is_displayed():
            flgStatus = True
    except NoSuchElementException:
            flgStatus = False

    if flgStatus:
        edit_profile(skype, linked, twitter, website, location, bio, countcpt)
    else:
        time.sleep(1)
        try:
            if findByCss('#new_new_user > div.form-group > p.gl-field-error.hide').is_displayed():
                a = findByCss('#new_new_user > div.form-group > p.gl-field-error.hide').text
                flgStatus = False
            else:
                a = ""
            if findByCss('div.username.form-group > p.gl-field-error.hide').is_displayed():
                b = findByCss('div.username.form-group > p.gl-field-error.hide').text
                flgStatus = False
            else:
                b = ""
            if findByCss('#password-strength > p.gl-field-error.hide').is_displayed():
                c = findByCss('#password-strength > p.gl-field-error.hide').text
                flgStatus = False
            else:
                c = ""
            if findByXPath("//form[@id='new_new_user']/div[4]/p").is_displayed():
                d = findByXPath("//form[@id='new_new_user']/div[4]/p").text
                flgStatus = False
            else:
                d = ""
            if findByXPath("//form[@id='new_new_user']/div[5]/p").is_displayed():
                e = findByXPath("//form[@id='new_new_user']/div[5]/p").text
                flgStatus = False
            else:
                e = ""

            if findByCss("p.validation-error.hide").is_displayed():
                g = findByCss("p.validation-error.hide").text
                flgStatus = False
            else:
                g = ""
        except:
            if findById("error_explanation").is_displayed():
                f = findById("error_explanation").text
                flgStatus = False
            else:
                f = ""

    resultRun = temp + chr(13) + "Test case " + str(i)  + chr(13) + " " + str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + str(g)+ chr(13)

    if flgStatus:
        temp = resultRun + "Pass" + chr(13)
        resultRun = resultRun + "Pass"
        print i, "Register Succesfully !"
    else:
        temp = resultRun
        print i, "Register Failed !"

    a = ""
    b = ""
    c = ""
    d = ""
    e = ""
    f = ""

    'Close browser'
    driver.close()

# Create log
file = open("myLog.txt", "w")
file.write(resultRun)
file.close()