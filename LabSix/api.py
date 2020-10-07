import requests
import os
from datetime import datetime
import logging

logging.basicConfig(filename='debug.log', level=logging.DEBUG, format=f'%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def get_city():
    while True:
        city = input("City: ").strip().lower()

        if len(city) <= 0:
            logging.warn("Please type in a city.")
            logging.debug(f'user has entered invalid data "{city}"')
            continue
        else:
            break

    return city

def get_state():
    while True:
        state = input("State initials: ").strip().lower()

        if len(state) != 2:
            logging.warn("Please type in your states two letter initials.")
            logging.debug(f'user has entered invalid data "{state}"')
            continue
        else:
            break

    return state

def get_country():
    while True:
        country = input("Country initials: ").strip().lower()

        if len(country) < 2:
            logging.warn("Please enter in your countries 2-3.")
            logging.debug(f'user has entered invalid data "{country}"')
            continue
        elif len(country) > 3:
            logging.warn("Please enter in your countries 2-3.")
            logging.debug(f'user has entered invalid data "{country}"')
            continue
        else:
            break

    return country


def main():
    try:
        city = get_city()
        state = get_state()
        country = get_country()
        print(city, state, country)

        key = os.environ.get('weather_key')
        query = {'q':'minneapolis,mn,us', 'units':'imperial', 'appid':key}

        url = 'http://api.openweathermap.org/data/2.5/forecast'
        data = requests.get(url, params=query).json()

        forecast_items = data['list']

        print(f'Date:'.ljust(25),'Temperature:'.ljust(15),'Description:'.ljust(25),'Wind Speed'.ljust(20))
        print("-----------------------------------------------------------------------------------------")

        for forecast in forecast_items:
            timestamp = forecast['dt']
            date = datetime.fromtimestamp(timestamp)
            temp = forecast['main']['temp']
            desc = forecast['weather'][0]['description']
            wind = forecast['wind']['speed']
            print(str(date).ljust(25) + "|", str(temp).ljust(15) + "|", str(desc).ljust(25) + "|", str(wind).ljust(20))
    except Exception as e:
        logging.warn("Invalid information or our servers are currently offline.")
        logging.error(e)

if __name__ == '__main__':
    main()