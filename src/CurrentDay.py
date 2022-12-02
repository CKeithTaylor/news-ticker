import requests
import json
import config


class Headline:
    def __init__(self, api):
        self.api = api

    def get_news():
        api = config.news_api["world_news"]

        with open("data/news_sources.json") as json_file:
            data = json.load(json_file)
            links = list(data.values())

        url = f"{api['url']}url={links}&analyze=TRUE"
        headers = {"apikey": api["key"]}
        payload = {}

        api_return = requests.get(url, headers=headers, data=payload)
        api_data = api_return.json()
        json_file = json.dumps(api_data)
        with open("data/news.json", "w") as f:
            f.write(json_file)

    def local():
        ...

    def national():
        ...

    def world():
        ...


class Currency:
    def __init__(self, api):
        self.api = api

    def get_currency_data(self):
        for i in self.api:
            item = self.api[i]
            url = f"{item['url']}&{item['key']}"
            outfile = f"data/{i}_latest.json"
            data = requests.get(url)
            data = data.json()
            json_file = json.dumps(data)
            with open(outfile, "w") as f:
                f.write(json_file)


class Weather:
    def __init__(self, api):
        self.api = api

    def get_forecast(self):
        params = {"access_key": self.api["key"], "query": "71913", "units": "f"}
        url = f"{self.api['url']}forecast"
        outfile = "data/forecast.json"
        api_return = requests.get(url, params)
        api_data = api_return.json()
        json_file = json.dumps(api_data)
        with open(outfile, "w") as f:
            f.write(json_file)

    def get_current(self):
        params = {"access_key": self.api["key"], "query": "71913", "units": "f"}
        url = f"{self.api['url']}current"
        outfile = "data/current_weather.json"
        api_return = requests.get(url, params)
        api_data = api_return.json()
        json_file = json.dumps(api_data)
        with open(outfile, "w") as f:
            f.write(json_file)
