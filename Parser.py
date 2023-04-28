import requests
from bs4 import BeautifulSoup

def parse():
    url = "https://www.omgtu.ru/general_information/the-structure/the-department-of-university.php"  # URL сайта для парсинга


    padge = requests.get(url)
    print(padge.status_code)

    soup = BeautifulSoup(padge.text, "html.parser")

    block = soup.findAll('h3', class_="news-card__title")


    for data in block:

        description = data.text.strip()

        return(description + "\n\n")
