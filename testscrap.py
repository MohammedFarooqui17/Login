import pandas as pd
import requests
import re
from bs4 import BeautifulSoup
import os


# how can we extract the data from the website 
url ="https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
re = requests.get(url)
soup = BeautifulSoup(re.text,"lxml")
names = soup.find_all("a",class_="title")


product_name = []
for i in names:
    name = i.text
    product_name.append(name)
print(product_name)

pnames = soup.find_all("h4",class_="price float-end card-title pull-right")
product_price=[]
for i in pnames:
    product=i.text
    product_price.append(product)
print(product_price)


description = soup.find_all("p",class_="description")
descriptionss=[]
for i in description:
    desc=i.text
    descriptionss.append(desc)
print(descriptionss)



review = soup.find_all("p",class_="review-count float-end")
review_list=[]
for i in review:
    rev=i.text
    review_list.append(rev)
print(review_list)


nested = soup.find_all("div",class_="col-md-4 col-xl-4 col-lg-4")[3]


# by using we can fnd the nested element
hell=nested.find("a").text
print(hell)

df = pd.DataFrame({"Product Name":product_name,"Product Price":product_price,"Descriptions":descriptionss,"Reviews":review_list})
print(df)
df.insert(0, "Serial Number", range(1, len(df) + 1))
file_path = r"C:\Users\opo119062\Desktop\Admin_panel\Product_Details.xlsx"

# df.to_excel(file_path, index=False)
# os.startfile(file_path)

# print("Excel file saved and opened successfully.")



# **** ===================== how can we scrap the data from table  ================================= ***


url1 = "https://www.iplt20.com/auction/2024"
response = requests.get(url1)
print(response)

soup = BeautifulSoup(response.text,"lxml")


table=soup.find("table",class_="ih-td-tab w-100 auction-tbl t1")
headers = table.find_all("thead")
header_list=[]
for i in headers:
    th=i.text.strip()
    print(th)
    clean_header=" ".join(th.split())
    print(clean_header)
    header_list.append(clean_header)
print(header_list)



body = table.find("tbody",id='pointsdata')
rows = body.find_all('tr')
body_data=[]
for i in rows:
    cols = i.find_all("td")

    if len(cols) == 5:
        player_data ={
        # 'SR No.': cols[0].text.strip(),
        'Player Name': cols[1].text.strip(),
        'Nationality': cols[2].text.strip(),
        'Role': cols[3].text.strip(),
        'Price Paid': cols[4].text.strip(),
        }
        body_data.append(player_data)
    
print(body_data)

df1 = pd.DataFrame(body_data)
df1.reset_index(drop=True, inplace=True)
print(df1)

file_path = r"C:\Users\opo119062\Desktop\Admin_panel\Player_list.xlsx"
df1.to_excel(file_path, index=False)

