#!/usr/bin/env python3
# Kate Archer - Project 5 - p5.py
# CSCI 3038 - June 30, 2016

import requests, sys
from bs4 import BeautifulSoup as bs
print()

if (sys.argv[1]=='-j'):
    url = 'https://maps.googleapis.com/maps/api/distancematrix/json?origins=' + sys.argv[2] +'&destinations=' + sys.argv[3]
    r = requests.get(url).json()
    print(r)
    print()
    print(r['rows'][0]['elements'][0]['distance']['text'], 'between', sys.argv[2], 'and', sys.argv[3])
    print()

elif (sys.argv[1]=='-x'):
    url = 'https://maps.googleapis.com/maps/api/distancematrix/xml?origins=' + sys.argv[2] +'&destinations=' + sys.argv[3]
    r = requests.get(url)
    print(r)
    soup = bs(r.content, 'html')
    first_text, sec_text = soup.find_all('text')
    print(str(sec_text)[6:-7], 'between', sys.argv[2], 'and', sys.argv[3])
    print()

else:
    url = sys.argv[2]
    r = requests.get(url)
    print(r)
    soup = bs(r.content, 'html')
    for link in soup.find_all('a'): print(link.get('href'))
    print()
