# -*- coding: utf-8 -*-
import os

import dotenv

env = dotenv.Dotenv(os.path.expanduser('~/.env'))
# Scrapy settings for newspider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html


# ************************Redis Start ******************************
# ****** ITEM_PIPELINES 加上 'scrapy_redis.pipelines.RedisPipeline': 300
REDIS_HOST = env.get('REDIS_HOST') or 'localhost'
REDIS_PORT = env.get('REDIS_PORT') or '6379'
# REDIS_URL = 'redis://user:password@host:post'  # 另一种连接方式，优先上面的配置

# REDIS_ENCODING = 'utf-8' 
# 默认  其他'latin1'

REDIS_PARAMS = {'password': env.get('REDIS_PASSWORD')}
# 自定义redis连接参数
# 默认参数{'socket_timeout': 30, 'socket_connect_timeout': 30, 
#           'retry_on_timeout': True, 'encoding': REDIS_ENCODING}


# REDIS_PARAMS['redis_cls'] = 'myproject.RedisClient'
# 使用自定义的redis client 连接类, 默认：redis.StrictRedis

SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 在redis中启用调度存储请求队列。

DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 去重规则对应处理的类,确保所有spider通过redis共享相同的重复过滤器

# SCHEDULER_DUPEFILTER_KEY = '%(spider)s:dupefilter'
# 去重规则，在redis中保存时对应的key

# SCHEDULER_PERSIST = True
# Don't cleanup redis queues, allows to pause/resume crawls.
# 在关闭时候保留原来的调度器和去重记录，True=保留

# SCHEDULER_FLUSH_ON_START = True 
# 是否在开始之前清空 调度器和去重记录，True=清空，False=不清空

# Schedule requests using a priority queue. (default)
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.PriorityQueue'

# Alternative queues.
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.FifoQueue'
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.LifoQueue'

# Max idle time to prevent the spider from being closed when distributed crawling.
# This only works if queue class is SpiderQueue or SpiderStack,
# and may also block the same time when your spider start at the first time (because the queue is empty).
# SCHEDULER_IDLE_BEFORE_CLOSE = 10
# 去调度器中获取数据时，如果为空，最多等待时间（最后没数据，未获取到）

# ******** 数据持久化，指定key和序列化函数 REDIS ******
# The item pipeline serializes and stores the items in this redis key.
# REDIS_ITEMS_KEY = '%(spider)s:items'
# 在redis中的键值，列表类型，存储每个items

# The items serializer is by default ScrapyJSONEncoder. You can use any
# importable path to a callable object.
# REDIS_ITEMS_SERIALIZER = 'json.dumps'
# 使用Python的json.dumps序列化后再存储

# ******************起始URL相关************************
# If True, it uses redis' ``SPOP`` operation. You have to use the ``SADD``
# command to add URLs to the redis queue. This could be useful if you
# want to avoid duplicates in your start urls list and the order of
# processing does not matter.
# REDIS_START_URLS_AS_SET = False
# 获取起始URL时，去集合中获取还是去列表中获取？  True，集合；False，列表
# 获取起始URL时，如果为True，则使用self.server.spop；如果为False，则使用self.server.lpop

# Default start urls key for RedisSpider and RedisCrawlSpider 
# REDIS_START_URLS_KEY = '%(name)s:start_urls'
# 起始URL从redis的Key中获取
# ****************************** Redis End************************************


BOT_NAME = 'newspider'

SPIDER_MODULES = ['newspider.spiders']
NEWSPIDER_MODULE = 'newspider.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'newspider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# S  PIDER_MIDDLEWARES = {
#    'newspider.middlewares.NewspiderSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'newspider.middlewares.NewspiderDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'scrapy_redis.pipelines.RedisPipeline': 300,
    'newspider.pipelines.NewspiderPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
