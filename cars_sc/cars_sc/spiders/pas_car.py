import scrapy


class PasCarSpider(scrapy.Spider):
    name = "pas_car"
    allowed_domains = ["auto.ria.com"]
    start_urls = ["https://auto.ria.com"]

    def parse(self, response):
        pass
