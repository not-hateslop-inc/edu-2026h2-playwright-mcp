import json, re
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    page = p.chromium.launch().new_page()
    page.goto("https://books.toscrape.com/")
    page.get_by_role("link", name="Travel").click()
    links = [a.get_attribute("href") for a in page.locator("article.product_pod h3 a").all()]
    base = page.url.rsplit("/", 1)[0]
    rows = []
    for href in links:
        page.goto(base + "/" + href)
        stock = page.locator("p.instock.availability").inner_text()
        rows.append({"title": page.locator("h1").inner_text(),
                     "price": page.locator("p.price_color").first.inner_text(),
                     "stock": int(re.search(r"\d+", stock).group())})
json.dump(rows, open("results/b_playwright.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(rows), "books")
