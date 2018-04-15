"""
Finds chess events on the library calendar for and prints the date and location
"""
import scrapy

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
        # todo: rather than this, iterate over each day div,
        # store the date, if chess, add to list, else continue
        for el in response.css('a.colorbox-inline::text').extract():
            if el is not None:
                if 'chess' in el.lower():
                    print(el)
            else:
                print('No chess events found.')
