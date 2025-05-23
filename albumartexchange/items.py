# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ImageItem(scrapy.Item):
    image_url = scrapy.Field()
    dimensions = scrapy.Field()
    file_size = scrapy.Field()
    details_url = scrapy.Field()
