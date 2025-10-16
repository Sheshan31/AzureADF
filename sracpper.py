import requests
from bs4 import BeautifulSoup
import pandas as pd
import json


parent_link = "https://www.bloomberg.com/billionaires/"
user_agt = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"

headers = {
  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
  "User-Agent": user_agt
}


def get_richies():
    parent_webpage = requests.get(parent_link, headers=headers)
    soup = BeautifulSoup(parent_webpage.content, "lxml")

    rows = soup.find_all("div", attrs={"class":"table-row"})

    data = {"rank": [], "name": [], "net_worth": [], "last_change":[], "year_change":[], "country":[], "industry":[]}

    for row in rows:
        try:
            rank = row.find("div", attrs={"class":"table-cell t-rank"}).text.strip()
        except:
            rank = None


        try:
            name = row.find("div", attrs={"class":"table-cell t-name"}).text.strip()
        except:
            name = None


        try:
            net_worth = row.find("div", attrs={"class":"table-cell active t-nw"}).text.strip()
        except:
            net_worth = None

        try:
            last_change = row.find("div", attrs={"class":"table-cell t-lcd pos"}).text.strip()
        except:
            last_change = None

        try:
            year_change = row.find("div", attrs={"class":"table-cell t-ycd pos"}).text.strip()
        except:
            year_change = None

        try:
            country = row.find("div", attrs={"class":"table-cell t-country"}).text.strip()
        except:
            country = None

        try:
            industry = row.find("div", attrs={"class":"table-cell t-industry"}).text.strip()
        except:
            industry = None

        data["rank"].append(rank)
        data["name"].append(name)
        data["net_worth"].append(net_worth)
        data["last_change"].append(last_change)
        data["year_change"].append(year_change)
        data["country"].append(country)
        data["industry"].append(industry)

    df = pd.DataFrame(data)
    res = json.loads(df.to_json(orient="records"))
    return res