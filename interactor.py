import socket
import xml.etree.ElementTree as ET
import time
import sys
import pandas as pd
from lxml import etree
import urllib2
import json
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

driver= webdriver.Chrome('C:\Users\Mojix\Downloads\chromedriver_win32\chromedriver.exe')
def start():
    driver.get("http://192.168.50.42:3161/devices/AdvanSafe-200-us/start")
def stop():
    driver.get("http://192.168.50.42:3161/devices/AdvanSafe-200-us/stop")
driver.get("http://192.168.50.42:3161/index.html")
user=driver.find_element_by_id("lg_login")
user.send_keys("admin")

#time.sleep(2)
password = driver.find_element_by_id("lg_pass")
password.send_keys("admin")

driver.find_element_by_id('login-button').click()

time.sleep(3) #this is to wait for the website
select1 = Select (driver.find_element_by_id("devices"))
select1.select_by_value("AdvanSafe-200-us")


driver.find_element_by_xpath("//span[text()='Monitor']").click()
time.sleep(2)
#driver.find_element_by_xpath("//input[@id='start']").click()
#driver.find_element_by_id('start').click()
#driver.find_element_by_id('stop').click()
stop()