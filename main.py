import requests
from bs4 import BeautifulSoup
import json

# 1 block

url = "https://auto.ria.com/newauto/catalog/"

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}

req = requests.get(url, headers = headers)
src = req.text
print(src)

with open("index.html", "w") as file:
  file.write(src)




# 2 block

# with open("index.html") as file:
#   src = file.read()
#
#
# soup = BeautifulSoup(src, "lxml")
# all_cars_hrefs = soup.find_all(class_ = "item-brands")
#
#
# for item in all_cars_hrefs:
#   item_text = item.text
#   item_href = "https://auto.ria.com" + str(item.get("href"))
#   print(f"{item_text} : {item_href}")




# 3 block

# with open("index.html") as file:
#   src = file.read()
#
# soup = BeautifulSoup(src, "lxml")
# all_cars_hrefs = soup.find_all(class_="item-brands")
#
# all_categories_dict = {}
#
# for item in all_cars_hrefs:
#   item_text = item.text
#   item_href = "https://auto.ria.com" + str(item.get("href"))
#
#   all_categories_dict[item_text] = item_href
#
# with open("all_categories_dict.json", "w") as file:  #когда здесь создаешь json file то он туда с index.html файла не всю информацию переносит
#   json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)




# 4 block

# with open("all_categories_dict.json") as file:
#    all_categories = json.load(file)
#
# print(all_categories)

# count = 0
# for cars_name, cars_href in all_categories.items():
#   if count == 0:
#     req = requests.get(url = cars_href, headers = headers)
#     src = req.text
#
#     with open(f"data/{count}_{cars_name}.html", "w") as file:
#       file.write(src)
#
#     count += 1