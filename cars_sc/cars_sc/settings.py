# Scrapy settings for cars_sc project

BOT_NAME = "cars_sc"

SPIDER_MODULES = ["cars_sc.spiders"]
NEWSPIDER_MODULE = "cars_sc.spiders"

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

# Промежуточное ПО для случайных заголовков
DOWNLOADER_MIDDLEWARES = {
    # Отключаем стандартный User-Agent
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    # Включаем наше промежуточное ПО для случайных заголовков
    'cars_sc.middlewares.RandomHeadersMiddleware': 400,
    # Оставляем стандартное промежуточное ПО
    'cars_sc.middlewares.CarsScDownloaderMiddleware': 543,
}

# Настраиваем список возможных User-Agent и Accept-Language для случайного выбора
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0",
    # Добавьте больше User-Agent при необходимости
]

ACCEPT_LANGUAGES = [
    "en-US,en;q=0.9",
    "ru-RU,ru;q=0.9",
    "uk-UA,uk;q=0.9",
    # Добавьте другие языки при необходимости
]
