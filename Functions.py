'''
IMPORTANT: 
All the functions title's must start with "jv_" to avoid confusion between jarvis functions and external functions.
1. Create all the processing and dependent functions here without any joining of "other pages".
2. After a function is defined and tested go to "Brain.py" and add "elif" statement relating the tag refering your function and actually calling the function you just have created.
3. Go to "Intents.json" and create new group with "tags", "patterns", "responses" in it, also fill them.
4. Give as much as data you can give to the "intents.json" file so that the accuracy of jarvis can be high.

TEMPLATE:
             {"tag": "",
              "patterns": [],
              "responses": []
             },
'''



from Utilities import *


def jv_home_complete_date():
    import datetime
    full_date = datetime.datetime.now()
    my_date = full_date.day
    my_year = full_date.year
    if my_date ==1:
        my_date = "first"
    elif my_date == 2:
        my_date = "second"
    elif my_date ==3:
        my_date = "third"
    elif my_date == 4:
        my_date = "fourth"
    elif my_date ==5:
        my_date = "fifth"
    elif my_date == 6:
        my_date = "sixth"
    elif my_date ==7:
        my_date = "seventh"
    elif my_date == 8:
        my_date = "eighth"
    elif my_date ==9:
        my_date = "ninth"
    elif my_date == 10:
        my_date = "tenth"
    elif my_date ==11:
        my_date = "eleventh"
    elif my_date == 12:
        my_date = "twelfth"
    elif my_date ==13:
        my_date = "thirteenth"
    elif my_date == 14:
        my_date = "fourteenth"
    elif my_date ==15:
        my_date = "fifteenth"
    elif my_date == 16:
        my_date = "sixteenth"
    elif my_date ==17:
        my_date = "seventeenth"
    elif my_date == 18:
        my_date = "eighteenth"
    elif my_date ==19:
        my_date = "nineteenth"
    elif my_date == 20:
        my_date = "twentieth"
    elif my_date ==21:
        my_date = "twentyfirst"
    elif my_date == 22:
        my_date = "twenty second"
    elif my_date ==23:
        my_date = "twenty third"
    elif my_date == 24:
        my_date = "twenty fourth"
    elif my_date == 25:
        my_date = "twenty fifth"
    elif my_date ==26:
        my_date = "twenty sixth"
    elif my_date == 27:
        my_date = "twenty seventh"
    elif my_date ==28:
        my_date = "twenty eighth"
    elif my_date == 29:
        my_date = "twenty ninth"
    elif my_date ==30:
        my_date = "thirtieth"
    elif my_date == 31:
        my_date = "thirty first"
    dt = f"its {full_date.strftime('%A')} the {my_date} {full_date.strftime('%B')} of {my_year}"
    talk(dt)

def jv_only_date():
    import datetime
    my_date = datetime.datetime.now().day
    if my_date ==1:
        my_date = "first"
    elif my_date == 2:
        my_date = "second"
    elif my_date ==3:
        my_date = "third"
    elif my_date == 4:
        my_date = "fourth"
    elif my_date ==5:
        my_date = "fifth"
    elif my_date == 6:
        my_date = "sixth"
    elif my_date ==7:
        my_date = "seventh"
    elif my_date == 8:
        my_date = "eighth"
    elif my_date ==9:
        my_date = "ninth"
    elif my_date == 10:
        my_date = "tenth"
    elif my_date ==11:
        my_date = "eleventh"
    elif my_date == 12:
        my_date = "twelfth"
    elif my_date ==13:
        my_date = "thirteenth"
    elif my_date == 14:
        my_date = "fourteenth"
    elif my_date ==15:
        my_date = "fifteenth"
    elif my_date == 16:
        my_date = "sixteenth"
    elif my_date ==17:
        my_date = "seventeenth"
    elif my_date == 18:
        my_date = "eighteenth"
    elif my_date ==19:
        my_date = "nineteenth"
    elif my_date == 20:
        my_date = "twentieth"
    elif my_date ==21:
        my_date = "twentyfirst"
    elif my_date == 22:
        my_date = "twenty second"
    elif my_date ==23:
        my_date = "twenty third"
    elif my_date == 24:
        my_date = "twenty fourth"
    elif my_date == 25:
        my_date = "twenty fifth"
    elif my_date ==26:
        my_date = "twenty sixth"
    elif my_date == 27:
        my_date = "twenty seventh"
    elif my_date ==28:
        my_date = "twenty eighth"
    elif my_date == 29:
        my_date = "twenty ninth"
    elif my_date ==30:
        my_date = "thirtieth"
    elif my_date == 31:
        my_date = "thirty first"
    dt = f"it's {my_date} sir."
    talk(str(dt))

def jv_open_youtube():
    import webbrowser
    talk("opening sir.")
    url = 'https://www.youtube.com/feed/subscriptions'
    webbrowser.open(url)

def jv_current_home_time():
    import datetime
    now_method = datetime.datetime.now()
    current_home_time = str(now_method.strftime("%H:%M")) # "%H"-Hour "%M"-Minutes "%S"-Seconds
    talk(f"its {current_home_time} sir.")

def jv_mac_app_opener(command):
    import os
    wanted_app = command.lower()
    wanted_app = wanted_app.replace("jarvis", "")
    wanted_app = wanted_app.replace("open", "")
    wanted_app = wanted_app.replace(" ", "")

    apps = os.listdir("/Applications")

    for app in apps:
        app_for_test = app.lower()
        app_for_test = app_for_test.replace(" ", "")
        if wanted_app in app_for_test:
            print(f"opening {app}")
            app = app.replace(" ", "\ ")
            os.system(f"open /Applications/{app}")
        else:
            continue

def jv_battery_meter():
    import os
    data = str(os.system("pmset -g batt"))
    if "discharging" in data:
        talk("we currently are running on built in power supply.")
    else:
        talk("we currently are running on external power supply.")

def jv_open_geeksforgeeks():
    import webbrowser
    talk("sure")
    g4g_url = "https://www.geeksforgeeks.org/"
    webbrowser.open(g4g_url)

def jv_open_stackoverflow():
    import webbrowser
    talk("opening")
    stackoverflow_url = "https://stackoverflow.com/"
    webbrowser.open(stackoverflow_url)

def jv_open_github():
    import webbrowser
    talk("ok")
    github_url = "https://github.com/"
    webbrowser.open(github_url)

def jv_open_instagram():
    import webbrowser
    insta_url = "https://www.instagram.com/"
    talk("done")
    webbrowser.open(insta_url)

def jv_tell_weather():
    if wifi_available() == True:
        import requests
        from bs4 import BeautifulSoup

        # enter city name
        city = "arizona"

        # create url
        url = "https://www.google.com/search?q="+"weather"+city
        # requests instance
        html = requests.get(url).content
        # getting raw data
        soup = BeautifulSoup(html, 'html.parser')
        # get the temperature
        temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
        # this contains time and sky description
        str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
        # format the data
        data = str.split('\n')
        time = data[0]
        sky = data[1]
        # list having all div tags having particular class name
        listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
        # particular list with required data
        strd = listdiv[5].text
        # formatting the string
        pos = strd.find('Wind')
        other_data = strd[pos:]
        # printing all the data
        talk(f"It is {temp}")
        # print("Time: ", time)
        talk(f"with {sky} skies")
        # print(other_data)
    else:
        talk("The weather is unpredictable around here. I might need wifi connection for this.")





        
jv_tell_weather()








































