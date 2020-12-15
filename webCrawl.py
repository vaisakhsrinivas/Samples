import json
import requests
from bs4 import BeautifulSoup


def get_country_asn_info(raw_data, country_name):
    """get country info 
        @args:
          raw_data: Raw data from url parsed
          country_name: Country name
        @returns:
          None: If no data retrived from parsed url
          dict: Mapped ASN info
    """
    asn_info_map = {}
    country_class = raw_data.find(class_ = "sortable")

    if (country_class == None):
        return None

    for row in country_class("tr"):
        counter = 0
        details = {"Country": country_name, "Name": "", "Routev4": "", "Routev6": ""}
        ASN = ""
        if row("th"):
            continue
        for cell in row("td"):
            raw_data = cell.text
            if counter == 0:
                ASN = raw_data
            if counter == 1:
                details["Name"] = raw_data
            if counter == 3:
                details["Routev4"] = raw_data
            if counter == 5:
                details["Routev6"] = raw_data

            counter = counter + 1
        asn_info_map[ASN] = details

    return asn_info_map

def get_asn_info(url):
    """get asn info 
        @args:
          url: Base ASN site URL
        @returns:
    """
    header={ 'User-Agent': 'Mozilla/5.0' }
    session = requests.Session()
    source_code = session.get(url, headers = header)
    soup = BeautifulSoup(source_code.text, 'html.parser')
    world_class = soup.find(class_ = "sortable")
    all_reports = world_class.find_all('a')

    for country_link in all_reports:
        country_path = str(country_link.get('href'))
        country_name = country_path.split('/')[-1]

        report_link = 'http://bgp.he.net' + country_path
        link_raw_data = requests.get(report_link, headers = header)
        raw_data = BeautifulSoup(link_raw_data.text, 'html.parser')
        asn_info_map = get_country_asn_info(raw_data, country_name)

        if (asn_info_map != None):
            with open('asn_info_map.json', 'a') as fp:
                json.dump(asn_info_map, fp)

# Driver code
if __name__ == '__main__':
    get_asn_info("http://bgp.he.net/report/world")

