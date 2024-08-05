# s24004
# 沖縄県の推計人口

import requests
from bs4 import BeautifulSoup

uri = 'https://www.pref.okinawa.jp/toukeika/estimates/estimates_suikei.html'
html = requests.get(uri)

html.encoding = "Shift_JIS"

soup = BeautifulSoup(html.text, 'html.parser')
baseElement = soup.find('table', class_='table1 font2 gyo5')


jinkou = [
  "",
  "",
  "",
  ""
]

for i, element in enumerate(baseElement.find_all("td", align="right")):
  jinkou[i] = element.text

print("沖縄県の推計人口")
print(f"総人口: {jinkou[0]}")
print(f"男: {jinkou[1]}")
print(f"女: {jinkou[2]}")