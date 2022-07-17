from urllib import parse
import requests
from bs4 import BeautifulSoup



def get_citations_needed_count(URL):
    counter = 0
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    atags = soup.find_all("a")

    for tag in atags:
        if "citation needed" in str(tag):

            counter += 1
                 
    return counter    



def get_citations_needed_report(URL):

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    ptags = soup.find_all("p")
    k = 1
    messagestr = ""
    clean_message = ""
    
    for tag in ptags:
        if "citation needed" in tag.text:
            messagestr += tag.text.strip()
    
    message = messagestr.split(".")
    for i,sentence in enumerate(message):
        if "citation needed" in sentence:
            clean_sentence = sentence.replace("[citation needed]", "")
            clean_message += f"\n({k}.) {clean_sentence})\n"
            k += 1

    return clean_message


URL = "https://en.wikipedia.org/wiki/1989_Tiananmen_Square_protests_and_massacre"
print(get_citations_needed_count(URL))
print(get_citations_needed_report(URL))