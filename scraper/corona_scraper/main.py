import requests as r
import re
from bs4 import BeautifulSoup


if __name__ == "__main__":
    url = "https://koronavirusinfo.az/az/page/statistika/azerbaycanda-cari-veziyyet"
    res = r.get(url).text
    soup = BeautifulSoup(res, features="html.parser")
    div = soup.find_all("div", class_="gray_little_statistic")
    for i in div:
        print(f"{i.span.text}: {i.strong.text}")
