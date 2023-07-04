import base64
import requests
from bs4 import BeautifulSoup as BS
from fake_useragent import UserAgent


class Weather:
    def __init__(self):
        self.base_url = "https://world-weather.ru/pogoda/kazakhstan/pavlodar/"
        self.headers = {"User-Agent": UserAgent().random}

    def get_html(self):
        response = requests.get(self.base_url, headers=self.headers)
        bs = BS(response.text, "lxml")
        return bs

    def get_temp(self):
        html = self.get_html()
        temp = html.find("div", id="weather-now-number").text
        img = html.find("span", id="weather-now-icon").get("title")
        return temp, img









