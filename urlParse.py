import requests
from bs4 import BeautifulSoup

def start(url):
    header={ 'User-Agent': 'Mozilla/5.0' }
    source_code = requests.get(url, headers = header)
    soup = BeautifulSoup(source_code.text, 'html.parser')
    print(soup.prettify())

# Driver code
if __name__ == '__main__':
    start("http://bgp.he.net/report/world")