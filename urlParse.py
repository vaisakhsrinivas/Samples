import json
import re
import requests
from bs4 import BeautifulSoup

def start(url):
    header={ 'User-Agent': 'Mozilla/5.0' }
    links = []
    headings = []
    report_jsonObj = dict()
    session = requests.Session()
    source_code = session.get(url, headers = header)
    soup = BeautifulSoup(source_code.text, 'html.parser')
    world_class = soup.find(class_ = "sortable")
    all_reports = world_class.find_all('a')

    for country_link in all_reports:
        links.append('http://bgp.he.net' + country_link.get('href'))

    for report_links in links:
        link_data = requests.get(report_links, headers = header)
        data = BeautifulSoup(link_data.text, 'html.parser')
        country_class = data.find(class_ = "sortable")
        country_data = [[cell.text for cell in row("td")]
                        for row in country_class("tr")]
        #final_country_data = list(filter(None, country_data))
        #report_jsonObj = json.dumps(dict(final_country_data))
        #print(report_jsonObj)

        print(country_data)


# Driver code
if __name__ == '__main__':
    start("http://bgp.he.net/report/world")