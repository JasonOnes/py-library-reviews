"""urllib.error is an exception class raised bu urllib.request problems"""

# URLError subclass of OSError as of 3.3 (instead of IOError)
import webbrowser

from urllib.error import HTTPError, URLError
from urllib.request import urlopen

from bs4 import BeautifulSoup

def get_city_temp(city, country):
    # prints temp of city, catches the HTTPError if can't find for that city (ie no page)
    try:
        html = urlopen("https://www.timeanddate.com/weather/" + str(country) + "/" + str(city))
        temp_page = BeautifulSoup(html.read(), "html.parser")
        temp_html = temp_page.find("div", {"id":"qlook"}).find("div", {"class":"h2"})
        temp = temp_html.get_text()
        print(temp)
    except HTTPError:
        print("No info found for that input, perhaps check your spelling.")

def check_local_8000():
    # checks local port to see if anything running there, catches URLErro if not
    try:
        resp = urlopen("http://127.0.0.1:8000")
    except URLError:
        print("You've got nothing current running at that port.")

if __name__ == "__main__":
    get_city_temp("dhaka", "bangladesh")
    get_city_temp("berin", "germany")
    check_local_8000()

    
