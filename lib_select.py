from urllib.request import urlopen
from bs4 import BeautifulSoup
import random


def find_subject_library():
    # gives a random subject.section number in index for day's review
    html = urlopen("https://docs.python.org/3/library/index.html")
    soupy_page = BeautifulSoup(html.read(), "html.parser")
    index_body = soupy_page.findAll("", {"class":"reference internal"})

    nums = []
    items_to_go = []
    for item in index_body:
        nums.append(item.get_text()[:5])
    for num in nums:
        for c in num:
            if c.isalpha():
                items_to_go.append(num)

    fresh_index = [item for item in nums if item not in items_to_go]

    today_lesson = random.choice(fresh_index)
    print(today_lesson)

   
find_subject_library()

