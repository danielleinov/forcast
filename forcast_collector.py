"""
This script collect the hourly temperature from weather.com and save the table data in a json file.
"""

# Author: Daniel Leinov

import requests
from bs4 import BeautifulSoup
import json
import sys

url = 'https://weather.com/weather/hourbyhour/l/ISXX0026:1:IS'

# Get the page from the url
try:
     page = requests.get(url)

# Error and break the script if not success get the page
except:
     print("Can't success get page from weather.com")
     sys.exit(1)  # Exit from script

# Initialize Beautiful soup instance with html parser
soup = BeautifulSoup(page.content,"html.parser")

# Find the table in html 
table=soup.find_all("table",{"class":"twc-table"})
time_dic = {}  # Dictionary that will hold the details for each hour

# Pass on each item in the table
for items in table:
     for i in range(len(items.find_all("tr"))-1):
          details_dic = {}  # Dictionary for details of the hour time
          time = items.find_all("span", {"class": "dsx-date"})[i].text  # The time

          # Save in each key the value from the table
          details_dic["DESC"] = items.find_all("td", {"class": "description"})[i].text
          details_dic["TEMP"] = (items.find_all("td", {"class": "temp"})[i].text).split('\u00b0')[0]
          details_dic["FEEL"] = (items.find_all("td", {"class": "feels"})[i].text).split('\u00b0')[0]
          details_dic["PRECIP"] = items.find_all("td", {"class": "precip"})[i].text
          details_dic["HUMIDITY"] = items.find_all("td", {"class": "humidity"})[i].text
          details_dic["WIND"] = items.find_all("td", {"class": "wind"})[i].text

          # Save for the hour time the dictionary with details
          time_dic[time] = details_dic

# Save the dictionary in JSON format in JSON file
with open('forcast_data.json', 'w') as json_file:
  json.dump(time_dic, json_file, indent=4)

