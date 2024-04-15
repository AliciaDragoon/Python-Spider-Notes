# Scrapy settings for wangxiao project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "wangxiao"

SPIDER_MODULES = ["wangxiao.spiders"]
NEWSPIDER_MODULE = "wangxiao.spiders"
LOG_LEVEL = "WARNING"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "wangxiao (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
   "Accept-Language": "en",
    "Cookie":"agentmembers=wx; mantis6894=15d77bbd92eb44c8a4c6fad2e5ab0400@6894; safedog-flow-item=; UserCookieName=pc_586480502; OldUsername2=fViTdjnFXL7VdIFv48JLkg%3D%3D; OldUsername=fViTdjnFXL7VdIFv48JLkg%3D%3D; UserCookieName_=pc_586480502; OldUsername2_=fViTdjnFXL7VdIFv48JLkg%3D%3D; OldUsername_=fViTdjnFXL7VdIFv48JLkg%3D%3D; pc_586480502_exam=jz1; register-sign=jz1; sign=; userInfo=%7B%22userName%22%3A%22pc_586480502%22%2C%22token%22%3A%22d7616c3c-6d84-4c4c-8740-841608a53e6f%22%2C%22headImg%22%3Anull%2C%22nickName%22%3A%22185****6121%22%2C%22sign%22%3A%22fangchan%22%2C%22isBindingMobile%22%3A%221%22%2C%22isSubPa%22%3A%220%22%2C%22userNameCookies%22%3A%22fViTdjnFXL7VdIFv48JLkg%3D%3D%22%2C%22passwordCookies%22%3A%22Zjaf4MyWoxw%3D%22%7D; token=d7616c3c-6d84-4c4c-8740-841608a53e6f; OldPassword=Zjaf4MyWoxw%3D; OldPassword_=Zjaf4MyWoxw%3D"
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "wangxiao.middlewares.WangxiaoSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "wangxiao.middlewares.WangxiaoDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # 先下载图片，再写入md
   "wangxiao.pipelines.WangxiaoPipeline": 300,
    "wangxiao.pipelines.WangxiaoImagePipeline": 290,
}
# 设置图片下载路径
IMAGES_STORE = "./"

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
