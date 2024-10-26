# Scrapy settings for cars_sc project

BOT_NAME = "cars_sc"

SPIDER_MODULES = ["cars_sc.spiders"]
NEWSPIDER_MODULE = "cars_sc.spiders"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "cars_sc (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False  # Обратите внимание, что это может нарушать правила сайта

# Configure maximum concurrent requests performed by Scrapy
CONCURRENT_REQUESTS = 64  # Увеличиваем количество одновременных запросов

# Configure a delay for requests for the same website
DOWNLOAD_DELAY = 0.5  # Устанавливаем небольшую задержку между запросами

# Configure the number of concurrent requests per domain and IP
CONCURRENT_REQUESTS_PER_DOMAIN = 32  # Увеличиваем до 32
CONCURRENT_REQUESTS_PER_IP = 32  # Увеличиваем до 32

# Disable cookies (enabled by default)
COOKIES_ENABLED = False  # Отключаем куки для ускорения

# Enable or disable extensions
EXTENSIONS = {
    "scrapy.extensions.logstats.LogStats": None,
}

# Configure item pipelines
ITEM_PIPELINES = {
    "cars_sc.pipelines.CarsScPipeline": 300,
}

# Enable and configure the AutoThrottle extension (enabled by default)
AUTOTHROTTLE_ENABLED = True  # Включаем автоматическую регулировку
AUTOTHROTTLE_START_DELAY = 1  # Устанавливаем начальную задержку
AUTOTHROTTLE_MAX_DELAY = 10  # Максимальная задержка в случае высокой латентности
# Увеличиваем количество параллельных запросов
AUTOTHROTTLE_TARGET_CONCURRENCY = 2.0

# Enable and configure HTTP caching (disabled by default)
HTTPCACHE_ENABLED = True  # Включаем кэширование HTTP для повторных запросов
HTTPCACHE_EXPIRATION_SECS = 3600  # Время кэширования 1 час
HTTPCACHE_DIR = "httpcache"
# Можно добавить коды ошибок, которые игнорируются
HTTPCACHE_IGNORE_HTTP_CODES = []

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
