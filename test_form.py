import datetime
import requests
from requests import Session
from robobrowser import RoboBrowser
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
username = config.get("information", "Username")
password = config.get("information", "Password")
val2 = config.get("information", "Link-to-Personal-Site")
val1 = config.get("information", "Canvas-Auth")





print( val1 + " " + val2)

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

requests.packages.urllib3.disable_warnings()
c = Session()
c.verify = False

browser = RoboBrowser(session=c,parser='html.parser')

browser.open('https://utk.instructure.com/')
form = browser.get_form()
form['username'] = username
form['password'] = password
browser.submit_form(form)
poop = browser.find('body')
poop = str(poop['class'])
poop = find_between(poop, "'context-", "']")
user = poop
personal_site = val2
Canvas_authcode = val1
headers = {
    'Authorization': 'Bearer ' + Canvas_authcode}

browser.open(personal_site)
hrs = browser.find_all("strong")
for list in hrs:
    line = list.text
   # print(line)
   # print(check)
    dydak_date = find_between(line, "on ", " (")
    line2 = find_between(line, ". ", "M:")
    manny_date = datetime.datetime.strptime(dydak_date, "%m/%d/%y").strftime("%Y-%m-%d")
    check = c.get("https://utk.instructure.com/api/v1/calendar_events?context_codes%5B%5D=" + user + "&context_codes%5B%5D=course_45009&context_codes%5B%5D=course_45015&context_codes%5B%5D=course_46248&context_codes%5B%5D=course_48317&context_codes%5B%5D=course_9088&start_date=" + manny_date + "T05%3A00%3A00.000Z&end_date=2018-09-09T05%3A00%3A00.000Z", headers=headers)
    check = str(check.json())
    print(line2)
    if line2 not in check:
        #print(manny_date)
        fun = manny_date + 'T21:00:00Z'
        files = {
            'calendar_event[context_code]': (None, user),
            'calendar_event[title]': (None, line2),
            'calendar_event[start_at]': (None, fun),
            'calendar_event[end_at]': (None, fun),
            'calendar_event[description]': (None, '''<a href="http://www.math.utk.edu/~dydak/251Sp18/Grades/xmcm3464web.html">Dydak's Hell Hole</a>''')
        }
        response = c.post('https://utk.instructure.com/api/v1/calendar_events.json', headers=headers, files=files)
        response = response.json()
        if "errors" in response:
            print(
                """Content-type: text/html

                Failure: Exit the script<br/>""")
    else:
     print("Assignment ALREADY ADDED, SKIPPING")




