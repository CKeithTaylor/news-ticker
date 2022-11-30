import requests
import json
import config


class Headline:
    def __init__(self, api):
        self.api = api

    def get_news():
        api = config.news_api["world_news"]
        data = requests.get(f'{api["url"]}&{api["key"]}')
        data = data.json()
        json_file = json.dumps(data)
        with open("data/headlines.json", "w") as f:
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
