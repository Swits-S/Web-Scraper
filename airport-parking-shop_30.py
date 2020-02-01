"""
Web scraper
By Jake Gourley
last edited 01/02/2020
"""
"""
This program is used to scrape the data from airport parking shop
and then write the data to a csv file
"""

#imports libraries
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
import datetime
from datetime import date
from datetime import timedelta
from time import sleep
import ssl

#declaring variables
month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#Setting headless
chrome_options = Options()
chrome_options.add_argument("--headless")

#Initialising Variables
a = 2
b = 2
c = 2
f = 1
g = 0
h = 0
j = 1
stron = {}
subcat = {}
now = datetime.datetime.now()

#Starting loop
while c == 2:
    i = 0
    g = 0
    j = 1
"""
Entry Date generator code
"""
    #creating start date
    Date= date.today()
    Date = Date +timedelta(days=30)
    print(Date)

    #creating exit date
    if f == 1:
        exit_Date =Date + timedelta(days=1)
    elif f == 2:
        exit_Date =Date + timedelta(days=2)
    elif f == 3:
        exit_Date =Date + timedelta(days=3)
    elif f == 4:
        exit_Date =Date + timedelta(days=4)
    elif f == 5:
        exit_Date =Date + timedelta(days=5)
    elif f == 6:
        exit_Date =Date + timedelta(days=6)
    elif f == 7:
        exit_Date =Date + timedelta(days=7)
    elif f == 8:
        exit_Date =Date + timedelta(days=8)
    elif f == 9:
        exit_Date =Date + timedelta(days=9)
    elif f == 10:
        exit_Date =Date + timedelta(days=10)
    elif f == 11:
        exit_Date =Date + timedelta(days=11)
    elif f == 12:
        exit_Date =Date + timedelta(days=12)
    elif f == 13:
        exit_Date =Date + timedelta(days=13)
    elif f == 14:
        exit_Date =Date + timedelta(days=14)
    elif f == 15:
        exit_Date =Date + timedelta(days=15)
        c = 3
    #creating entryDate string
    enDay=str(Date.day)
    #creating exit Date string
    exDay=str(exit_Date.day)
    print(enDay)
    print(exDay)
    day= str(now.day)
    entDate = str(Date.day) + " " + str(month[Date.month - 1]) + " " + str(Date.year)
    extDate = str(exit_Date.day) + " " + str(month[exit_Date.month - 1]) + " " + str(exit_Date.year)
    #Setting up the web browser automation
    driver = webdriver.Chrome("/Users/jakegourley/Desktop/chromedriver", options=chrome_options)
    driver.get("https://www.airport-parking-shop.co.uk/?agent=aw_40035887186_airport%20parking%20shop_4433370&gclid=EAIaIQobChMIsb7_xLyl5QIVxLHtCh3YeAGIEAAYASAAEgJNtPD_BwE")

"""
Airport selection Code
"""
    #Locating Airport Field and Id
    airport = Select(driver.find_element_by_id("airports"))
    #Selecting Name of airport
    airport.select_by_visible_text("Edinburgh")
"""
Entry Date Code
"""
    #Locating Entry Date callendar picker
    clicker = driver.find_element_by_xpath("//*[contains(@class, 'datepicker arrivalDate flatpickr-input form-control input')]")
    clicker.click()
    
    
    #Locating Current month on callendar pop up
    entryMonth = driver.find_element_by_xpath("//*[contains(@class, 'cur-month')]")
    sleep(1)
    #Locating Next Month Button
    nxtMonth = driver.find_element_by_xpath("//*[contains(@class, 'flatpickr-next-month')]")
    sleep(1)
    #Loop for checking then changing month selected
    while a == 2:
        entryMonth = driver.find_element_by_xpath("//*[contains(@class, 'cur-month')]")
        nxtMonth = driver.find_element_by_xpath("//*[contains(@class, 'flatpickr-next-month')]")
        if entryMonth.text == month[Date.month-1]:
            a = 1
        else:
            nxtMonth.click()

   
    #Locating entry Day on callendar pop up
    entryDay = driver.find_element_by_xpath("//*[@class = 'flatpickr-day ' and text() = '"+ str(Date.day)+"']")
    sleep(2)
    entryDay.click()
    a = 1
"""
Exit Date code
"""
    #Locating and clicking exit Day callendar pop up
    clicker = driver.find_element_by_xpath("//*[contains(@class, 'datepicker returnDate flatpickr-input form-control input')]")
    clicker.click()
    
    
    #Locating current month field
    entryMonth = driver.find_element_by_xpath("//*[contains(@class, 'cur-month')]")
    sleep(2)
    #Locating next month button
    nxtMonth = driver.find_element_by_xpath("//*[contains(@class, 'flatpickr-next-month')]")
    sleep(2)
    #Loop for checking month
    while a == 1:
        entryMonth = driver.find_elements_by_xpath("//*[contains(@class, 'cur-month')]")
        prevMonth = driver.find_elements_by_xpath("//*[contains(@class, 'flatpickr-prev-month')]")
        nextMonth = driver.find_elements_by_xpath("//*[contains(@class, 'flatpickr-next-month')]")
        #Checking Month Data
        if entryMonth[1].text == month[exit_Date.month-1]:
            a = 2
            if entryMonth[1].text == month[Date.month]:
                j = 0
            else:
                j = 1
        elif entryMonth[1].text == month[exit_Date.month]:
            sleep(2)
            prevMonth[1].click()
            j = 1
        else :
            sleep(2)
            nextMonth[1].click()
            j = 0

    #Clicking exit Date 
    if driver.find_elements_by_xpath("//*[@class = 'flatpickr-day selected' and text() = '"+ str(exit_Date.day)+"']") == True:
        ExitDay = driver.find_element_by_xpath("//*[@class = 'flatpickr-day selected' and text() = '"+ str(exit_Date.day)+"']")
        ExitDay.click()
    else:
        ExitDay = driver.find_elements_by_xpath("//*[@class = 'flatpickr-day ' and text() = '"+ str(exit_Date.day)+"']")
        sleep(3)
        ExitDay[j].click()
"""
Search Button Click code and wait for page to load
"""
    #Locating Search Button and clicking
    searchBtn = driver.find_element_by_xpath("//*[contains(@class, 'button large success expanded')]")
    searchBtn.click()
   
    time.sleep(10)
"""
Accessing Data and writing to document Code
"""
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
    strongArray = soup.find_all("div", {"class": "result"})
    counter = len(strongArray)
    
    #checks whether end of strong tags has been reached
    while i != 99:
        
        #sets h2 value
        h2Arry = soup.find_all("div", {"class": "amount text-right"})
        for x in h2Arry:
            h2  = x.find('div').text

            #sets strong value
            strongArry = soup.find_all("div", {"class": "result"})
            for y in strongArry:
                subcat [h] = y.find('h5').text
                h = h + 1

            #sets h2T
            h2T = str(h2)
    
            #sets strongT
            strongT = str(subcat [g])
    
            #opens file
            with open ('Airparks.csv', 'a') as file:
            
                #writes to file
                file.write(strongT)
                file.write(",")
                file.write(h2T)
                file.write(",")

            g = g +1

            
        i = 99
        with open ('Airparks.csv', 'a') as file:
            file.write("\n")

    f = f +1
    driver.close()
print("end of program")

