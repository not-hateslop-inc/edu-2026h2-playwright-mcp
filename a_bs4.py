import json, re, time
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

START = "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"
s = requests.Session(); s.headers["User-Agent"] = "hateslop-edu/2.0"

def soup(url): return BeautifulSoup(s.get(url, timeout=10).text, "lxml")

rows = []
for a in soup(START).select("article.product_pod h3 a"):
    d = soup(urljoin(START, a["href"]))
    stock = d.select_one("p.instock.availability").get_text(strip=True)
    rows.append({"title": d.select_one("h1").text, "price": d.select_one("p.price_color").text,
                 "stock": int(re.search(r"\d+", stock).group())})
    time.sleep(0.5)
json.dump(rows, open("results/a_bs4.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(rows), "books")
