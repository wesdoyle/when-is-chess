'''
Finds chess events on the library calendar for and prints the date and location
'''
import scrapy
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
        calendar = dict()

        for el in response.css('.has-events').extract():

            soup = BeautifulSoup(el, 'lxml')

            day = soup.find('div', {'class': 'day'})
            daylink = day.find('a')
            if daylink.string not in calendar:
                calendar[daylink.string] = {'events' : []}

            links = soup.find_all('a', {'class': 'colorbox-inline'})
            branch_colors = soup.find_all('div', {'class': 'stripe'})

            for link in links:
                calendar[daylink.string]['events'].append(link.string)

            # branches = []
            # for color in branch_colors:
            #     hex_color = str(color['style'][-6:])
            #     if hex_color in BRANCHES:
            #         branches.append(BRANCHES[hex_color])

        print(calendar)

