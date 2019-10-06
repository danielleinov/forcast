
import requests
from bs4 import BeautifulSoup
import json
url = 'https://weather.com/weather/hourbyhour/l/ISXX0026:1:IS'
page = requests.get(url)
soup=BeautifulSoup(page.content,"html.parser")
table=soup.find_all("table",{"class":"twc-table"})
time_dic = {}
for items in table:
    for i in range(len(items.find_all("tr"))-1):
         details_dic = {}
         time = items.find_all("span", {"class": "dsx-date"})[i].text
         details_dic["DESC"] = items.find_all("td", {"class": "description"})[i].text
         details_dic["TEMP"] = items.find_all("td", {"class": "temp"})[i].text
         details_dic["FEEL"] = items.find_all("td", {"class": "feels"})[i].text
         details_dic["PRECIP"] = items.find_all("td", {"class": "precip"})[i].text
         details_dic["HUMIDITY"] = items.find_all("td", {"class": "humidity"})[i].text
         details_dic["WIND"] = items.find_all("td", {"class": "wind"})[i].text
         time_dic[time] = details_dic
with open('forcast_data.json', 'w') as json_file:
  json.dump(time_dic, json_file, indent=4)

