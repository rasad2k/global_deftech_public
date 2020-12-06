import requests as r
import sys
from tika import parser
from bs4 import BeautifulSoup


def get_pages():

    link_list = []

    for i in range(1, 42):

        url = 'https://koronavirusinfo.az/az/page/xeberler?category=4&page='
        url += str(i)
        res = r.get(url).text
        soup = BeautifulSoup(res, "html.parser")
        link = ""

        for j in soup.find_all("a", {"class": "news_card"}, href=True):

            if j.p.get_text() == "Azərbaycan Respublikası Nazirlər Kabineti yanında Operativ Qərargahın məlumatı":
                continue

            link = j['href']
            link_list.append(link)

    return link_list


def get_data(url):
    print(url)
    response = r.get(url).text
    soup = BeautifulSoup(response, "html.parser")
    pdf_link = soup.find("a", {"class": "download_card"}, href=True)

    if pdf_link == None:
        response = r.get(url).text
        soup = BeautifulSoup(response, "html.parser")
        text = soup.find("section", {"class": "readmore"}).get_text()
        data = " ".join(text.split()).split('.')
        return data

    print(pdf_link['href'])

    if "koronavirus" not in pdf_link['href']:
        return None

    response = r.get(pdf_link['href'])

    if response.status_code == 404:

        print("Not published yet")
        sys.exit(1)

    data = response.content
    return data


def handle_data(data):
    if type(data) == list:
        return data
    with open("my_pdf.pdf", 'wb') as my_data:
        my_data.write(data)

    raw = parser.from_file("my_pdf.pdf")
    text = raw['content']
    new_text = ""
    text = text.replace('\n', ' ')

    for i in range(len(text)):

        if i == len(text) - 2:
            break

        if text[i] == '\n' and text[i+1] == '\n':
            continue

        if text[i] == " " and text[i+1] == ' ':
            continue

        if text[i] == "\n" and text[i+1] == " ":
            continue

        if text[i] == " " and text[i+1] == "\n":
            continue

        new_text += str(text[i])

    out = new_text.split('.')

    for i in range(len(out)):

        if len(out[i]) == 0:
            continue

        if out[i][0] == " ":
            out[i] = out[i][1:]

    return out


if __name__ == "__main__":

    links = get_pages()
    out = []

    for link in links:

        data = get_data(link)

        if data == None:
            continue

        out.append(handle_data(data))

    with open('koronavirusinfo_az.txt', 'w') as f:
        for item in out:
            f.write("%s\n" % ".".join(item))