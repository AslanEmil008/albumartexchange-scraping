import scrapy


class AlbumartexchangeSpider(scrapy.Spider):
    name = "albumartexchange"
    allowed_domains = ["www.albumartexchange.com"]
    start_urls = ["https://www.albumartexchange.com/covers"]

    def parse(self, response):
        pass
