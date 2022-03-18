from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import urllib.request
import json
from datetime import datetime

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get(
    "https://www.metacritic.com/browse/albums/score/metascore/all/filtered?sort=desc")

now = datetime.now()
albumlist = []
i = 1

while i<=100:
    for album in driver.find_elements_by_tag_name("tr"):
        print(album.text)
        for tag in album.find_elements_by_tag_name("a"):
            for img in tag.find_elements_by_tag_name("img"):
                print(img.get_attribute("src"))
                urllib.request.urlretrieve(img.get_attribute("src"), str(i)+".png")
                i = i+1
                albumlist.append(
                    {"Rating": album.text.split("\n")[0],
                     "No": album.text.split("\n")[1],
                     "Judul": album.text.split("\n")[2],
                     "Singer": album.text.split("\n")[3],
                     "Release": album.text.split("\n")[4],
                     "waktu_scraping":now.strftime("%Y-%m-%d %H:%M:%S"),
                     "Image": img.get_attribute("src")
                     }
                )
hasil_scraping = open("AlbumScrapping.json", "w")
json.dump(albumlist, hasil_scraping, indent=5)
hasil_scraping.close()

driver.quit()
