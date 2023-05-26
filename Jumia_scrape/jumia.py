import requests
from bs4 import BeautifulSoup
import csv
url = "https://www.jumia.co.ke/flash-sales/"

response = requests.get(url).text
#print(response.status_code)

s = BeautifulSoup(response,"html.parser")

#Flash Sales Time Left
time_left = s.find("time",class_="-mlxs -ttn").text
print(time_left)

#Flash sale items
with open("Flash_sales.csv","w") as fhand:
    writer = csv.writer(fhand)
    items = s.find_all("article",class_="prd _fb _p col c-prd")
    for item in items:
        name = item.find("h3",class_="name").text
        new_price = item.find("div",class_="prc").text
        review = item.find("div",class_="stars _s").text
        stock = item.find("div",class_="stk").text
        writer.writerow([name,new_price,review,stock])
    review = s.find_all("div",class_="s-prc-w")
    for i in review:
        old_price = i.find("div",class_="old").text
        disc_percentage = i.find("div",class_="bdg _dsct _sm").text
        writer.writerow([old_price,disc_percentage])
    
