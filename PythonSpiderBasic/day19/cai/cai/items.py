# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CaiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    qi = scrapy.Field()
    red_ball = scrapy.Field()
    blue_ball = scrapy.Field()

