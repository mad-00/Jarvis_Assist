from Utilities import talk, wifi_available

import requests
def jv_tell_weather(command):
    if wifi_available() == True:
        try:
            import requests
            from bs4 import BeautifulSoup

            # enter city name
            command = command.replace("jarvis", "")
            command = command.replace(" ","")
            command = command.replace("weather", "")
            command = command.replace("tell", "")
            command = command.replace("how", "")
            command = command.replace("at", "")
            command = command.replace("how's", "")
            command = command.replace("hows", "")
            command = command.replace("the", "")
            command = command.replace("temperature", "")
            command = command.replace("how", "")
            if "home" in command:
                city = "hyderabad telangana"
            else:
                city = command

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
            talk(f"The weather in {city} is {temp} with {sky} skies.")
            # print(other_data)
        except AttributeError:
            talk("I m having hard time understanding you.")
    else:
        talk("The weather is unpredictable around here. I might need wifi connection for this.")





while True:
    command = input("area: ")
    jv_tell_weather(command)