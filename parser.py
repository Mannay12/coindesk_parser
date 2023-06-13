import re
import requests
import csv
from models import Items


class ParserWB:
    def __init__(self, url):
        self.news = self.__get_news(url)

    @staticmethod
    def __get_news(url: str):
        regex = '(?<==).+'
        news = re.search(regex, url)[0]
        return news

    def parse(self):
        page = 0
        self._create_csv()
        while page < 5:
            params = {
                'query': f'{{"search_query":"bitcoin","page":{page}}}',
            }

            response = requests.get(
                'https://www.coindesk.com/pf/api/v3/content/fetch/search',
                params=params
            )
            page += 1
            items_info = Items.parse_obj(response.json())
            if not items_info.items:
                break
            self._save_csv(items_info)

    def _create_csv(self):
        with open('coindesk.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['title', 'pubdate', 'link'])

    def _save_csv(self, items):
        with open('coindesk.csv', mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for item in items.items:
                writer.writerow([item.title,
                                 item.pubdate,
                                 item.link])


if __name__ == '__main__':
    ParserWB('https://www.coindesk.com/search?s=bitcoin').parse()
