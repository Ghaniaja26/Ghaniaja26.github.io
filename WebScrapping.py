# Import package request dan BeautifulSoup
import requests
from bs4 import BeautifulSoup
import json

# Request to website
page = requests.get("https://republika.co.id/")

# Extract content to BeautifulSoup object
obj = BeautifulSoup(page.text,'html.parser');

print ("\nMenampilkan semua teks headline")
print ("===================================")
for publish in obj.find_all('div',class_='conten1'):
    print(publish.find('h2').text)


print('\nMenampilkan waktu publish')
print("===================================")
for publish in obj.find_all('div',class_='date'):
        print(publish.text)


print('\nMenampilkan kategori')
print("===================================")
for publish in obj.find_all('div',class_='teaser_conten1_center'):
        print(publish.find('a').text)

# Date
import datetime
now = datetime.datetime.now()
print('\nMenampilkan waktu scrapping')
print("===================================")
for publish in obj.find_all('div',class_='teaser_conten1_center'):
        print (now.strftime("%Y-%m-%d %H:%M:%S"))

# Deklarasi list kosong
data=[]
# Lokasi file json
f=open(r'C:\Users\GHANI\Documents\Document\EDUKASI\KULIAH\TUGAS\Semester 2\Proyek 1\Data Scrapping\headline1.json','w')
for publish in obj.find_all('div',class_='conten1'):
    # append headline ke variable data
    data.append({"judul":publish.find('h2').text,"kategori":publish.find('a').text,"waktu_publish":publish.find('div',class_='date').text,"waktu_scraping":now.strftime("%Y-%m-%d %H:%M:%S")})
# dump list dictionary menjadi json
jdumps=json.dumps(data, indent = 2)
f.writelines(jdumps)
f.close()
