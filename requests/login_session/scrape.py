import requests
from bs4 import BeautifulSoup as BS, BeautifulSoup

soup = BeautifulSoup()

data = {'csrf': 'DMzC8wcInE3fMYuQ0A6QdQ==',
        'nick': '',
        'passwd': ''}

cookies = {'CSRF_TOKEN': 'DMzC8wcInE3fMYuQ0A6QdQ==',
           '__utma': '75309071.1655505578.1608729783.1608729783.1608729783.1',
           '__utmc': '75309071',
           '__utmz': '75309071.1608729783.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
           '__utmt': '1',
           'JSESSIONID': '640C1E94C242A4913B83CA138594194B',
           '__utmb': '75309071.4.10.1608729783'}

url = 'https://www.linux.org.ru/login_process'
s = requests.Session()

response = s.post(url, data=data, cookies=cookies)

notifications = soup.findAll("span", {"id": "main_events_count"})

print(notifications)
