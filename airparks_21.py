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

#declaring variables
month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


a = 2
b = 2
c = 2
f = 1
now = datetime.datetime.now()
while c == 2:
    #creating start date
    Date= date.today()
    Date = Date +timedelta(days=21)
    print(Date)

    #creating exit date
    if f == 1:
        exit_Date =Date + timedelta(days=4)
        print(exit_Date)
    elif f == 2:
        exit_Date =Date + timedelta(days=8)
    elif f == 3:
        exit_Date = Date + timedelta(days=10)
    else:
        exit_Date =Date + timedelta(days=15)
        c = 3
    #creating entryDate string
    enDay=str(Date.day)
    if enDay < 10:
        enDay = "0" + enDay
    #creating exit Date string
    exDay=str(exit_Date.day)
    if exDay < 10:
        exDay = "0" + exDay
    print(enDay)
    print(exDay)
    day= str(now.day)
    entDate = str(Date.day) + "/" + str(Date.month) + "/" + str(Date.year)
    extDate = str(exit_Date.day) + "/" + str(exit_Date.month) + "/" + str(exit_Date.year)
    # Using Chrome to access web
    driver = webdriver.Safari()

    # Open the website
    driver.get('https://www.parkbcp.co.uk/edinburgh/airport-parking.html')
    time.sleep(2)
    print("ready")
    #selects the entry date element
    entryDate = driver.find_element_by_name("ArrivalDate")
    #clicks the element specified
    entryDate.click()
    #clear the text box
    entryDate.clear()
    #enters the entry date
    entryDate.send_keys(entDate)
    time.sleep(2)
    #clicks the lement again to close the calendar prompt
    entryDate.click()

    #selects the entry time element
    entryTime = Select(driver.find_element_by_name("ArrivalTime"))
    #selects the correct entry time
    entryTime.select_by_visible_text("12:00")

    #selects the exit date element
    exitDay = driver.find_element_by_name("DepartDate")
    #clicks the element specified
    exitDay.click()
    #clear the text box
    exitDay.clear()
    #enters the entry date
    exitDay.send_keys(extDate)
    time.sleep(2)
    #clicks the lement again to close the calendar prompt
    exitDay.click()
    entryDate.click()
    entryDate.click()

    #selects the exit time element
    exitTime = Select(driver.find_element_by_name('DepartTime'))
    #selects the correct exit time
    exitTime.select_by_visible_text("13:00")

    time.sleep(3)
    #finds the search button element
    SearchButton = driver.find_element_by_xpath("//*[contains(@class, 'submit btn btn-primary btn-large')]")
    #clicks the search button
    SearchButton.click()

    time.sleep(15)
    #sets url to current url
    url= driver.current_url

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
print("end of program")
