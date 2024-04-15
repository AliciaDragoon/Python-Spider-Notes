# Scrapy settings for xiaoshuo project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "xiaoshuo"

SPIDER_MODULES = ["xiaoshuo.spiders"]
NEWSPIDER_MODULE = "xiaoshuo.spiders"

LOG_LEVEL = "WARNING"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False
# 开启使用自己的饼干。默认的饼干中间件会在每次请求后自动更新

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en",
    "Cookie": "GUID=eda4ec9d-a2a6-4f07-8145-8a63dcc26666; BAIDU_SSP_lcr=https://www.bing.com/; Hm_lvt_9793f42b498361373512340937deb2a0=1710853305; c_channel=0; c_csc=web; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F19%252F99%252F14%252F95041499.jpg-88x88%253Fv%253D1648893235000%26id%3D95041499%26nickname%3D%25E5%2598%25BB%25E5%2598%25BB%25E5%2598%25BB%25E7%259A%2584%25E6%259D%25B0%25E4%25BC%25A6%26e%3D1726481704%26s%3D9a325957b9c961e0; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2295041499%22%2C%22%24device_id%22%3A%2218e56cdb33de6-01bd33716e56df-4c657b58-810000-18e56cdb33e1e48%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22eda4ec9d-a2a6-4f07-8145-8a63dcc26666%22%7D; ssxmod_itna=Yq0x0D2GG=eWqGIx0dY8+DyGK3mxY54GODXRR0DBq2O4iNDnD8x7YDvIIhtIKQKB0DhQfet4uNqfFm2hfQGD2mhfpuC1x0aDbqGkwA074GGUxBYDQxAYDGDDpkDj4ibDY+tODjnz/Zl61KDpxGrDlKDRx0749KDbxDaDGakw704KDvxDGvxz4miiDi36O5HY3A+DiyY9EikD75Dux0HtikIDDH6y8Ds9cf4+fROK8YDvxDk=bvH34Gd0g5zmofNiARDiQhx/i0eNh0YYiDYi70Ydj1SFiDoi7/ewmhPhWDxdGh/1kDDirXN0GDD=; ssxmod_itna2=Yq0x0D2GG=eWqGIx0dY8+DyGK3mxY54GODXRRD8dphDGNYTGaKQmk1x8O7WtVTIwQSKDx+NGeGB0p=GYKclK+kiCrp06AWx1k2aOOcYZB7kqlS4=crF1II8lh9CtQUjrrHskAwkEufULik6XiBYxOiIeqQ68FmNcS2EHWnEXKD6dawfeuDR2teWqsdWS+jLB/STgGxWMKafsAOjCSo52KSvw/hcX9x61eC5f/OhnRgYVC7D5ii=ObPFshIa7dMLu+ltKmfcZKLvcKSAzS/BFaiIRjLL4plX28t/hKD1BCskU5+cnQsMZWqiDKkQ+vcolepV=GhlX0PdVnfRmINoYePEd9=eKfHp4DQ9xQRaj24QAQ3O7QGYaHoE43o04D08DiQqYD===; tfstk=ffXvymGWSz4DQUPGhiNl_pHpNhrurtI2mZSIIFYm1aQRAMuD1IMbW_Q1zIYfBGk9fG_a0Fq4ZiS2Qda3-deh0iPHKCM7xhTWFg-nhbv_11S2QdakeUjofi7pFWZ3kdZJFhxj1dOXf8ZJjHT6CEOsPbtBPF96CNTSNHtEChTjhQTSiNEDWxTIBTuS4pI3jBDsCtwwMeKssAHOendACiT8MSBJDILBwX6Svt_lftX2a7GJQgfdW1_atbJAfs9XxiyxepsfZOKlIlc9lZWRVtR-xvbpHNdChQnsIi9vyLK5dlcerTLc5td7xvdMF9ABh_VzoCvvvN6VkcH1Rgjh3QWTJ4TNiHJWxiyxepsXfgyfK9H-42YpjjZ82flwG30ZihLF1BLZN3L34QGZ_Qwy2eq82fGs8vtJ-u-r_fRmJ; Hm_lpvt_9793f42b498361373512340937deb2a0=1712118780",
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    "xiaoshuo.middlewares.XiaoshuoSpiderMiddleware": 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    "xiaoshuo.middlewares.XiaoshuoDownloaderMiddleware": 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    "xiaoshuo.pipelines.XiaoshuoPipeline": 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
