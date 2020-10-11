import requests
import re
from bs4 import BeautifulSoup


def get_converted_price(price):

    stripped_price = price.strip("£ ,")
    replaced_price = stripped_price.replace(",", "")
    find_dot = replaced_price.find(".")
    converted_price = float(replaced_price)
    return converted_price


def extract_url(url):

    if url.find("www.amazon.co.uk") != -1:
        index = url.find("/dp/")
        if index != -1:
            index2 = index + 14
            url = "https://www.amazon.co.uk" + url[index:index2]
        else:
            index = url.find("/gp/")
            if index != -1:
                index2 = index + 22
                url = "https://www.amazon.co.uk" + url[index:index2]
            else:
                url = None
    else:
        url = None
    return url


def get_product_details(url):

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"
    }
    details = {"name": "", "price": 0, "deal": True, "url": ""}
    _url = extract_url(url)
    if _url is None:
        details = None
    else:
        page = requests.get(_url, headers=headers)
        soup = BeautifulSoup(page.content, "html5lib")
        title = soup.find(id="productTitle")
        price = soup.find(id="priceblock_dealprice")
        if price is None:
            price = soup.find(id="priceblock_ourprice")
            details["deal"] = False
        if title is not None and price is not None:
            details["name"] = title.get_text().strip()
            details["price"] = get_converted_price(price.get_text())
            details["url"] = _url
        else:
            details = None
    return details

print(get_product_details("https://www.amazon.co.uk/kindle-now-with-a-built-in-front-light%E2%80%94with-special-offers%E2%80%94black/dp/B07FQ4DJ7X/ref=sr_1_1?dchild=1&keywords=kindle&qid=1602411454&sr=8-1"))