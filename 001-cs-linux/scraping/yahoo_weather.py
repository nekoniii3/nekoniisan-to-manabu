import requests
import re
from bs4 import BeautifulSoup
import datetime
from zoneinfo import ZoneInfo

def main():

    URL = "https://weather.yahoo.co.jp/weather/jp/13/?day=1"

    response = requests.get(URL)

    soup = BeautifulSoup(response.text,'html.parser')

    elem = soup.find("div", class_="cmnMod condition")

    condition = elem.find("p", class_="text")

    content = condition.text

    dt = datetime.datetime.now(ZoneInfo("Asia/Tokyo"))

    file_name = dt.strftime("%Y%m%d") + ".txt"

    with open(file_name, mode="w") as f:

        f.write(content)

    return

if __name__ == "__main__":

    main()
