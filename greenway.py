#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 20:38:37 2020

@author: davidjensen

This python script will compare the current height of the Roanoke River with the
height of the lowest bridge on the Roanoke River greenway. River height is obtained
by accessing online usgs stream gauge data, so an internet connection is required
for this script to run. Have a good bike ride! 
"""

""

#This python script will compare the current height of the Roanoke River with the
#height of the lowest bridge on the Roanoke River greenway. River height is obtained
#by accessing online usgs stream gauge data, so an internet connection is required
#for this script to run. Have a good bike ride! 

#Import requests and datetime
import requests
from datetime import datetime

#Get date to put together url string with most recent stream gauge data
date_now = datetime.now()
date_string = date_now.strftime("%Y-%m-%d")
time_string1 = date_now.strftime("%H:%M:%S")
time_string0 = str(int(time_string1[0:2])-1) + time_string1[2:len(time_string1)]

#get all the text from the usgs river gauge site
url_txt = "https://waterservices.usgs.gov/nwis/iv/?sites=02055000&parameterCd=00065&startDT="+date_string+"T"+time_string0+".000-04:00&endDT="+date_string+"T"+time_string1+".781-04:00&siteStatus=all&format=rdb"
res = requests.get(url_txt)
html_page = str(res.content)

#Split the text down to the river height and convert to float
html_split = html_page.split('\\')
html_select = html_split[-3]
height = float(html_select[1:len(html_select)])

#Create strings for script results
str_intro = "Greenway conditions are "
str_flood = "FLOODED. "
str_maybe = "MAYBE flooded. "
str_no = "NOT flooded. "
str_river = "River height is "
str_height = str(height)
str_unit = " feet."

print_flood = str_intro + str_flood + str_river + str_height + str_unit
print_maybe = str_intro + str_maybe + str_river + str_height + str_unit
print_no = str_intro + str_no + str_river + str_height + str_unit


#Determine if greenway is flooded, and print the answer
if height >= 3.2:
    print(print_flood)
elif height < 3.2 and height >= 3.0:
    print(print_maybe)
else:
    print(print_no)

