# Get all the URLs from Sitemap
from bs4 import BeautifulSoup
from requests import get
import re
import csv

urls = []
index = 0
response = get("Enter Sitemap's URL here")
content = BeautifulSoup(response.content, 'lxml')
urls = content.find_all('loc')

while index < len(urls):
    print(urls[index].text)
    with open('urls.csv', 'a', newline='') as urll:
        writer = csv.writer(urll)
        writer.writerow([urls[index].text])
    index += 1
