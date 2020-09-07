import requests
import datetime


class Request:
    __url = "https://covid-19-data.p.rapidapi.com/report/country/name"
    __now = datetime.datetime.now()

    def __init__(self, method, country, form='json'):
        self.__method = str(method)
        self.__format = str(form)
        self.__country = str(country)

    def get_api(self):
        error = SyntaxError('Error with request try again ')
        headers = {
            'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
            'x-rapidapi-key': "c5a3cb0bf5msh8ddf0bdd20db605p12b483jsn5661d04d9293"
        }
        query = {"date-format": "YYYY-MM-DD",
                 "format": f"{self.__format}",
                 "date": f"{datetime.datetime.strftime(self.__now, '%Y')}-"
                         f"{datetime.datetime.strftime(self.__now, '%m')}-"
                         f"{datetime.datetime.strftime(self.__now, '%d')}",
                 "name": f"{self.__country.upper()}"}

        if self.__method.upper() == 'GET':
            try:
                req = requests.request(self.__method.upper(), self.__url, headers=headers, params=query)
                if req.status_code == 200:
                    return req.json()
            except EnvironmentError:
                return error
