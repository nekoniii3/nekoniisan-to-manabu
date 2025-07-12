from flask import Flask
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def today_weather():

    URL = "https://weather.yahoo.co.jp/weather/jp/13/?day=1"

    response = requests.get(URL)

    soup = BeautifulSoup(response.text,'html.parser')

    elem = soup.find("div", class_="cmnMod condition")

    condition = elem.find("p", class_="text")

    content = condition.text

    return content

if __name__ == '__main__':
    app.run()