import requests
import datetime
from bs4 import BeautifulSoup
import csv
import os

url = "https://lbma.datanauts.co.uk/table"

r = requests.get(url)

soup = BeautifulSoup(r.content)

  
rows = []
rows.append(['date','USDAM','USDPM','GBPAM','GBPPM','EURAM','EURPM'])  
  
table = soup.find("table", { "class" : "data" })
for row in table.findAll("tr"):
    cells = row.findAll("td")
    if len(cells) == 7:
        date = cells[0].find(text=True)
        USDAM = cells[1].find(text=True)
        USDPM = cells[2].find(text=True)
        GBPAM = cells[3].find(text=True)
        GBPPM = cells[4].find(text=True)
        EURAM = cells[5].find(text=True)
        EURPM = cells[6].find(text=True)
        rows.append([date,USDAM,USDPM,GBPAM,GBPPM,EURAM,EURPM])



today = datetime.datetime.now().date()

filename = "DailyGoldPrice{}.csv".format(today.isoformat())  
    
with open(filename,'w',newline='') as f_output:
  csv_output = csv.writer(f_output)
  csv_output.writerows(rows)


current_path = "/home/azfar"
save_path = "/home/azfar/GoldPrice"
os.rename(current_path+'/'+filename, save_path+'/'+filename)