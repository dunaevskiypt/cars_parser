# Scrapy settings for cars_sc project

BOT_NAME = "cars_sc"

SPIDER_MODULES = ["cars_sc.spiders"]
NEWSPIDER_MODULE = "cars_sc.spiders"

# User-Agent для имитации реального пользователя
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"

# Отключаем соблюдение robots.txt, если необходимо
ROBOTSTXT_OBEY = False

# Снижаем число одновременных запросов
CONCURRENT_REQUESTS = 8

# Устанавливаем более значительную задержку между запросами
DOWNLOAD_DELAY = 2  # 2 секунды между запросами

# Снижаем количество одновременных запросов на один домен/IP
CONCURRENT_REQUESTS_PER_DOMAIN = 4
CONCURRENT_REQUESTS_PER_IP = 4

# Отключаем куки для предотвращения отслеживания
COOKIES_ENABLED = False

# Отключаем лишние расширения
EXTENSIONS = {
    "scrapy.extensions.logstats.LogStats": None,
}

# Конфигурация конвейеров (pipelines)
ITEM_PIPELINES = {
    "cars_sc.pipelines.CarsScPipeline": 300,
}

# Включаем AutoThrottle для автоматического контроля скорости запросов
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 3  # Начальная задержка 3 секунды
AUTOTHROTTLE_MAX_DELAY = 30  # Максимальная задержка до 30 секунд
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0  # Снижаем до 1 запроса в секунду

# Включаем кэширование HTTP для повторных запросов
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 3600  # Время кэширования 1 час
HTTPCACHE_DIR = "httpcache"
HTTPCACHE_IGNORE_HTTP_CODES = []

# Устанавливаем настройки для стабильной работы
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
