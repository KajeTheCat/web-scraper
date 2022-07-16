from urllib import parse
import requests
from bs4 import BeautifulSoup



def get_citations_needed_count(URL):
    counter = 0
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    # print(soup)
    ptags = soup.find_all("p")
    atags = soup.find_all("a")
    # print(ptags)
    for tag in atags:
        if "citation needed" in str(tag):
            print(str(tag))
            counter += 1

    for tag in ptags:
        if "citation needed" in tag.text:
            # print("\n")
            # print(tag.text)
            # print("\n")
            for text in tag.text.split():
                # print(text)
                if "[citation" in text:
                    # print(text)
                    pass                 
            
    print(counter)    



def get_citations_needed_report(URL):

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    # print(soup)
    ptags = soup.find_all("p")
    atags = soup.find_all("a")
    # print(ptags)
    for tag in ptags:
        if "citation needed" in tag.text:
            # print("\n")
            # print(tag.text)
            # print("\n")
            for text in tag.text.split("."):
                # print(text)
                if "[citation" in text:
                    print(text)


URL = "https://en.wikipedia.org/wiki/1989_Tiananmen_Square_protests_and_massacre"
print(get_citations_needed_count(URL))
print(get_citations_needed_report(URL))