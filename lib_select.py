import sqlite3
from urllib.request import urlopen
from bs4 import BeautifulSoup


def create_lib_list():
    # creates a light db for the list of sections of the python library index
    db = sqlite3.connect('lib-list')
    cursor = db.cursor()
    
    cursor.execute(""" DROP TABLE lib""")
    db.commit()
    cursor.execute('''
        CREATE TABLE lib(id INTEGER PRIMARY KEY, section TEXT,
                        done INTEGER)''')
    # note no BOOLEAN Data type in sqlite hence INTEGER(0,1)
    db.commit()
    
    # official python page for built-ins
    html = urlopen("https://docs.python.org/3/library/index.html")
    soupy_page = BeautifulSoup(html.read(), "html.parser")
    # since I'm web scraping a static official page I just used html tags
    index_body = soupy_page.findAll("", {"class":"reference internal"})

    nums = []
    items_to_go = []
    for item in index_body:
        # didn't bother with regex since just doing this once to populate db
        section = item.get_text()[:5]
        nums.append(section)
    # if there is a letter in the first five chars it is a section header not a library section.subsection 
    for num in nums:
        for c in num:
            if c.isalpha():
                items_to_go.append(num)

    fresh_index = [item for item in nums if item not in items_to_go]

    for item in fresh_index:   
        cursor.execute("""INSERT INTO lib(section, done) VALUES(?, ?)""", (item, 0))

    print("db populated, ")
    db.commit()
    print("and created.")
   


def find_subject_library():
    # gives a random subject.section number in index for day's review
    db = sqlite3.connect('lib-list')
    cursor = db.cursor()

    today_lesson = cursor.execute("""SELECT section FROM lib WHERE done==0 ORDER BY RANDOM() LIMIT 1""")
    # today_lesson currently a Cursor object
    lib_num_tuple = today_lesson.fetchone() # now tuple
    lib_num = ''.join(lib_num_tuple) # now string
    if lib_num[-1] == '.':
        print(lib_num[:-1])  
    else:
        print(lib_num)

    # marks that section as done (1 = true), will no longer be elgible for selection
    cursor.execute('''UPDATE lib SET done = ? WHERE section = ? ''', (1, lib_num))
    db.commit()

    count_curs = cursor.execute(''' SELECT COUNT (*) FROM lib WHERE done == 0''')
    count = str(count_curs.fetchone())
    print("db updated, lesson marked as done")
    print("Only {} more built-ins to review!".format(count))
    
# uncomment below if I need to recreate the whole list of library sections
# create_lib_list()
find_subject_library()

