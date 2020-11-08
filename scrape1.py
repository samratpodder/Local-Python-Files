from bs4 import BeautifulSoup as bsp
from datetime import datetime
import requests
import time
import csv

while (True):
    csv_file2 = open('scrape1.csv', 'w')
    print("Pinging")
    csv_writer = csv.writer(csv_file2)
    csv_writer.writerow(["Title", "Link"])
    src = requests.get("http://makautexam.net/").text
    soup = bsp(src, 'lxml')
    print(soup)
    st = f"Box2"
    div1 = soup.findAll("div", class_=st)
    for art in div1:
        # print(art.h1.text)
        link = art.a['href']
        # print(link)
        csv_writer.writerow([art.h1.text, link])
    with open("scrape1.csv", "r") as csv_file:
        csv_reader01 = csv.reader(csv_file, delimiter=',')
        # for lines in csv_reader01:
        #    print(lines[0])
