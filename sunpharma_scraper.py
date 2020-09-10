# https://www.sunpharma.com/indiaproducts
import bs4 as bs
from urllib.request import Request,urlopen
import ssl
import urllib.error,urllib.parse
#sauce = urllib.request.urlopen("https://nmedicines.in/allopathy.html?___SID=U&dir=asc&limit=100&order=name").read()
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = 'https://www.sunpharma.com/indiaproducts'
req = Request(url,headers={'User-Agent':'Mozilla/5.0'})
sauce = urlopen(req).read()
soup = bs.BeautifulSoup(sauce,'html.parser')

import csv
rows = []
fields = ['PRODUCT NAME','STRENGTH','MOLECULE','THERAPY AREA','FORM','PACK SIZE']
filename = "sunpharma_enc.csv"

#print(soup.title)
#print(soup.title.string)
#print(soup.title.text)
table = soup.find_all('table')
for tabrow in table:
    table_rows = tabrow.find_all('tr')
    for tr in table_rows:
        td = tr.find_all('td')
        row = [i.text.encode("utf-8") for i in td]
        rows.append(row)

#print(soup.a) #first anchor element
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
    # writing the fields
    csvwriter.writerow(fields)
    # writing the data rows
    csvwriter.writerows(rows)
#print(soup.find_all('div'))
#table_rows = table.find_all('tr')
#for paragraph in soup.find_all('p'):
#    print(paragraph.string)  #bad output when child classes that too only under tags,not outside tags
#    print()
#    print(paragraph.text)    #good output but only under tags,not outside tags
