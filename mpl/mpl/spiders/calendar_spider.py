'''
Finds chess events on the library calendar for and prints the date and location
'''
import scrapy
import calendar
from bs4 import BeautifulSoup

BRANCHES = {'ff0000': 'central',
            'ffa500': 'alicia_goodman',
            '008000': 'goodman_south',
            '00ced1': 'hawthorne',
            '0000ff': 'lakeview',
            '4b0082': 'meadowridge',
            'ee82ee': 'monroe_street',
            '708090': 'pinney',
            'a52a2a': 'sequoya'}


class ChessCalendarSpider(scrapy.Spider):
    name = 'chess'

    def start_requests(self):
        urls = ['https://madisonpubliclibrary.org/calendar/search']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        day = 0

        for el in response.css('.has-events').extract():
            day_idx = day % 8
            day_name = calendar.day_name[day_idx - 1]
            soup = BeautifulSoup(el, 'lxml')

            links = soup.find_all('div', {'class': 'colorbox-inline'})
            days = soup.find_all('div', {'class': 'day'})
            colors = soup.find_all('div', {'class': 'stripe'})

            for color in colors:
                hex_color = str(color['style'][-6:])
                if hex_color in BRANCHES:
                    print(BRANCHES[hex_color])

            for div in links:
                print(div.string)
                # if 'chess' in str(div.string).lower():
                #     print(day_name)
                #     print(div.string)

            for d in days:
                print(f'Day: {d.find("a").text}')

            day += 1
            print(len(links))
            print(len(colors))
            print('*'*30)
