import requests
from bs4 import BeautifulSoup


def get_weather(city):
    weather = requests.get(f"https://sinoptik.ua/погода-{city}")
    soup = BeautifulSoup(weather.content)
    temp = soup.find("p", class_="today-temp").text
    shamol = soup.find("div", class_="Tooltip wind wind-NE").text
    nam = soup.find("td", class_="p2 bR").text

    return (nam, temp, shamol)
