BOT_NAME = 'douban_movie'

SPIDER_MODULES = ['douban_movie.spiders']
NEWSPIDER_MODULE = 'douban_movie.spiders'

# 遵守robots.txt规则
ROBOTSTXT_OBEY = False

# 配置请求头
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
}

# 下载延迟
DOWNLOAD_DELAY = 2

# 用户代理列表
USER_AGENT_LIST = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
]

# 启用中间件
DOWNLOADER_MIDDLEWARES = {
    'douban_movie.middlewares.RandomUserAgentMiddleware': 543,
    'douban_movie.middlewares.ProxyMiddleware': 544,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
}

# 配置Item Pipeline
ITEM_PIPELINES = {
    'douban_movie.pipelines.DoubanMoviePipeline': 300,
}
