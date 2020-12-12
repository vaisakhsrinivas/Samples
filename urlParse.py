import json
import re

import requests
from bs4 import BeautifulSoup

def start(url):
    header={ 'User-Agent': 'Mozilla/5.0' }
    links = []
    source_code = requests.get(url, headers = header)
    soup = BeautifulSoup(source_code.text, 'html.parser')
    main_class = soup.find(class_ = "sortable")
    all_reports = main_class.find_all('a')

    for country_link in all_reports:
        links.append('http://bgp.he.net' + country_link.get('href'))

    for i in links:
        link_data = requests.get(i, headers = header)
        data = BeautifulSoup(link_data.text, 'html.parser')
        jsonObj = json.dumps(data.decode("utf-8"))
        print(jsonObj)








# Driver code
if __name__ == '__main__':
    start("http://bgp.he.net/report/world")