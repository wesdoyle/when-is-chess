"""
Finds chess events on the library calendar for and prints the date and location
"""
import scrapy
import calendar
from bs4 import BeautifulSoup

BRANCHES = {'#ff0000': 'central',
            '#ffa500': 'alicia_goodman',
            '#008000': 'goodman_south',
            '#00ced1': 'hawthorne',
            '#0000ff': 'lakeview',
            '#4b0082': 'meadowridge',
            '#ee82ee': 'monroe_street',
            '#708090': 'pinney',
            '#a52a2a': 'sequoya'}


class ChessCalendarSpider(scrapy.Spider):
    name = "chess"

    def start_requests(self):
        urls = ['https://madisonpubliclibrary.org/calendar/search']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        day = 7  # calendar starts on sunday
        day_idx = day % 7
        day_name = calendar.day_name[day_idx]
        print(day_name)

        for el in response.css('.has-events').extract():
            soup = BeautifulSoup(el)

            for div in soup.find_all("div", {"class": "colorbox"}):
                for sub_div in div.find_all('a'):
                    if 'chess' in str(sub_div.string).lower():
                        print(sub_div.string)

        day += 1


