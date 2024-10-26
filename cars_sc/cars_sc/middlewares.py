import random
from scrapy import signals
# Импортируем списки из settings.py
from cars_sc.settings import USER_AGENTS, ACCEPT_LANGUAGES


class CarsScSpiderMiddleware:
    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        return None

    def process_spider_output(self, response, result, spider):
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        pass

    def process_start_requests(self, start_requests, spider):
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class CarsScDownloaderMiddleware:
    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        return None

    def process_response(self, request, response, spider):
        return response

    def process_exception(self, request, exception, spider):
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class RandomHeadersMiddleware:
    def process_request(self, request, spider):
        # Генерируем случайные заголовки User-Agent и Accept-Language
        request.headers['User-Agent'] = random.choice(USER_AGENTS)
        request.headers['Accept-Language'] = random.choice(ACCEPT_LANGUAGES)
        # Для лучшей поддержки сжатия
        request.headers['Accept-Encoding'] = 'gzip, deflate, br'
