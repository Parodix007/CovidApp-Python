import requests
import datetime
from error import Error


class Request:

    def __init__(self, method, country):
        self.__method = method
        self.__country = country
        self.__url = f"https://covid-19-tracking.p.rapidapi.com/v1/{country}"

    def get_api(self):
        error = 'Don`t type word "WORLD", type valid country'

        headers = {
            'x-rapidapi-host': "covid-19-tracking.p.rapidapi.com",
            'x-rapidapi-key': "c5a3cb0bf5msh8ddf0bdd20db605p12b483jsn5661d04d9293"
        }

        if self.__method.upper() == 'GET' and self.__country.lower() != 'world':
            try:
                req = requests.request(self.__method.upper(), self.__url, headers=headers)
                if req.status_code == 200:
                    return req.json()
            except:
                Error('Connection error')
        else:
            Error(error)
