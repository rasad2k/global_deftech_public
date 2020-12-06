import requests as r
from bs4 import BeautifulSoup

if __name__ == "__main__":
    url = "https://koronavirusinfo.az/az/post/176"
    res = r.get(url).text
    soup = BeautifulSoup(res, "html.parser")
    text =  soup.find("section", {"class": "readmore"}).get_text()
    print(" ".join(text.split())[:-19].split('.'))