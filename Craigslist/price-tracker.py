from bs4 import BeautifulSoup
import datetime
from tinydb import TinyDB, Query
import urllib3
import xlsxwriter

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'https://www.ebay.co.uk/itm/OMEGA-Seamaster-Planet-Ocean-600M-2201-5000-42-mm-2011/324218448116?_trkparms=aid%3D111001%26algo%3DREC.SEED%26ao%3D1%26asc%3D225114%26meid%3D9c1456d59e524e3cb186e461bb58fcef%26pid%3D100970%26rk%3D1%26rkt%3D1%26mehot%3Dnone%26sd%3D324218448116%26itm%3D324218448116%26pmt%3D0%26noa%3D1%26pg%3D2380057%26brand%3DOMEGA&_trksid=p2380057.c100970.m5481&_trkparms=pageci%3Aca98765a-0a21-11eb-8ffe-fa637c2bc1bd%7Cparentrq%3A0d19937e1750a69c21892be3fff031f6%7Ciid%3A1'
total_added = 0

def make_soup(url):
    http = urllib3.PoolManager()
    r = http.request("GET", url)
    return BeautifulSoup(r.data,'lxml')

def main(url):
    global total_added
    htmlSource = make_soup(url)
    title = htmlSource.title

    item_info = {
      "title": title,
      "price": "$2,345",
      "url": "https://www.ebay.co.uk/itm/OMEGA-Seamaster-Planet-Ocean-600M-2201-5000-42-mm-2011/324218448116?_trkparms=aid%3D111001%26algo%3DREC.SEED%26ao%3D1%26asc%3D225114%26meid%3D9c1456d59e524e3cb186e461bb58fcef%26pid%3D100970%26rk%3D1%26rkt%3D1%26mehot%3Dnone%26sd%3D324218448116%26itm%3D324218448116%26pmt%3D0%26noa%3D1%26pg%3D2380057%26brand%3DOMEGA&_trksid=p2380057.c100970.m5481&_trkparms=pageci%3Aca98765a-0a21-11eb-8ffe-fa637c2bc1bd%7Cparentrq%3A0d19937e1750a69c21892be3fff031f6%7Ciid%3A1"
    }

    return (item_info)