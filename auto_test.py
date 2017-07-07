#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import pytesseract
from PIL import Image
from io import BytesIO
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import redis


def verify_code():
    while True:
        driver.find_element_by_css_selector("#reg-code-refresh > img").click()
        time.sleep(2)
        image_elem = driver.find_element_by_id("reg-code")
        verify_image = image_elem.screenshot_as_png
        image = Image.open(BytesIO(verify_image))
        vcode = pytesseract.image_to_string(image)
        if vcode != '' and len(vcode) == 6:
            # with open('code/' + vcode + '.png', 'wb') as f:
            #     f.write(verify_image)
            # print(vcode)
            return vcode


def wait_register():
    for i in range(2):
        try:
            time.sleep(1)
            if "http://user.domain.net/m-users.htm" == driver.current_url:
                return True
        except:
            pass


def wait_url():
    for i in range(2):
        try:
            time.sleep(1)
            if "http://user.domain.net/m-users.htm" == driver.current_url:
                return True
        except:
            pass


def input_account():
    driver.find_element_by_id("reg_email").clear()
    driver.find_element_by_id("reg_email").send_keys(user_mail)
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys(user_pass)
    driver.find_element_by_id("password_confirm").clear()
    driver.find_element_by_id("password_confirm").send_keys(user_pass)

    vcode = verify_code()
    driver.find_element_by_id("regcode").clear()
    driver.find_element_by_id("regcode").send_keys(vcode)
    driver.find_element_by_id("subCreate").click()


driver = webdriver.Firefox()
driver.implicitly_wait(30)

# driver.get('http://user.gw-ec.com/login/safelog/redirectt?session=Jr9ahP88locYTgCmg3%2frpr6U%2fITc%2bK5a7T%2fIqVHKDkqh9tflBpUtpQ%3d%3d&url=http%3a%2f%2fgts.gw-ec.com')
# time.sleep(3)
# driver.get("http://gts.gw-ec.com/webcheck/check_do/243")
# time.sleep(3)
# driver.get("http://gts.gw-ec.com/webcheck/check_do/244")
# time.sleep(3)
# driver.get("http://gts.gw-ec.com/webcheck/check_do/245")
# time.sleep(3)
# driver.get("http://gts.gw-ec.com/webcheck/check_do/246")
# time.sleep(3)
# driver.get('http://user.gw-ec.com/login/safelog/redirectt?session=bsnH%2ft1tnzRHaYiu2Fwn6%2b1pWVvNYnWFx4Lgj5pZTVVAVzHJrAsUeA%3d%3d&url=http%3a%2f%2fwww.rms110.com')
# time.sleep(3)
# driver.get("http://gts.gw-ec.com/webcheck/check_do/247")
# time.sleep(3)
# driver.get("http://gts.gw-ec.com/webcheck/check_do/255")
# time.sleep(3)

base_url = "http://www.domain.net"
verificationErrors = []
accept_next_alert = True

driver.get(base_url + "/m-users-a-sign.htm")

user_pass = time.strftime("%y%m%d", time.localtime())
cache_key = 'ebemail_suffix:' + user_pass
red = redis.StrictRedis(host='192.168.117.128', port=6379, db=0,password='jameslouis')
suffix = red.get(cache_key)
if suffix is None:
    suffix = ''
    red.set(cache_key,1,86400)
else:
    red.incr(cache_key)

user_mail_key = user_pass + suffix.decode("utf-8")
user_mail = 'eb' + user_mail_key + '@mailinator.com'

input_account()

while True:
    is_success = wait_register()
    if is_success:
        break
    else:
        input_account()

driver.get(base_url + "/product1137643.html")
driver.find_element_by_id("new_addcart").click()

wait = WebDriverWait(driver, 11)
element = wait.until(EC.element_to_be_clickable((By.ID, 'cartPaypal')))
driver.find_element_by_css_selector("#cartChcekout > a > img[alt=\"checkout\"]").click()

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, 'js_upFormBtn')))

driver.find_element_by_id("firstname_0").clear()
driver.find_element_by_id("firstname_0").send_keys("James")
driver.find_element_by_id("lastname_0").clear()
driver.find_element_by_id("lastname_0").send_keys("Louis")
driver.find_element_by_id("addressline1_0").clear()
driver.find_element_by_id("addressline1_0").send_keys(u"≤‚ ‘∂©µ•Œ∑¢")
Select(driver.find_element_by_name("province")).select_by_visible_text("California")
driver.find_element_by_id("consignee_02").clear()
driver.find_element_by_id("consignee_02").send_keys(u"…Ó€⁄")
driver.find_element_by_id("tel_0").clear()
driver.find_element_by_id("tel_0").send_keys("123456789")
driver.find_element_by_id("zipcode_0").clear()
driver.find_element_by_id("zipcode_0").send_keys("123456")
driver.find_element_by_id("btn-save-consignee").click()
time.sleep(5)
driver.find_element_by_id("js_upFormBtn").click()

# wait = WebDriverWait(driver, 20)
# element = wait.until(EC.element_to_be_clickable((By.ID, 'btnLogin')))
#
# driver.find_element_by_id("email").clear()
# driver.find_element_by_id("email").send_keys("ppaccount.test@yahoo.com")
# driver.find_element_by_id("password").clear()
# driver.find_element_by_id("password").send_keys("Egrow%$167168")
# driver.find_element_by_id("btnLogin").click()
#
# time.sleep(3)
# driver.find_element_by_id("confirmButtonTop").click()

# time.sleep(15)
# driver.get("http://user.domain.net/m-users-a-order_list.htm")

