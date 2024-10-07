import requests as req
from bs4 import BeautifulSoup

while True:
    City = input("City: ")
    State = input("State: ")

    url = f"https://www.wunderground.com/weather/us/{State}/{City}"

    response = req.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        
        current_temp = soup.find("span", class_="wu-value wu-value-to").text
        high_temp = soup.find("span", class_="hi").text
        low_temp = soup.find("span", class_="lo").text
        weather_canditions = soup.find("div", class_="condition-icon small-6 medium-12 columns").text
        print("")
        print(f"Current Temperature in {City.title()}, {State.title()}: {current_temp}°F")
        print(f"High Temp {high_temp}F")
        print(f"Low Temp {low_temp}F")
        print(f"weather Conditions: {weather_canditions}")
        print("")
    else:
        print("Weather data fetch failed. status code:", response.status_code)

    loop = input("another city? y/n: ")

    if loop == "y":
        print("")
        pass
    elif loop == "n":
        break
    else:
        break