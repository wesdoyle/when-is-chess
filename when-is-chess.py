import scrapy
from scrapy.crawler import CrawlerProcess
from mpl.mpl.spiders.calendar_spider import ChessCalendarSpider

process = CrawlerProcess(
    {
        "USER_AGENT": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
        "LOG_LEVEL": "ERROR",
        "ROBOTSTXT_OBEY": True,
        "HTTPCACHE_ENABLED": True,
        "HTTPCACHE_EXPIRATION_SECS": 86_400,  # 24 hours
        "HTTPCACHE_DIR": "httpcache",
        "HTTPCACHE_STORAGE": "scrapy.extensions.httpcache.FilesystemCacheStorage",
    }
)

process.crawl(ChessCalendarSpider)
process.start()
