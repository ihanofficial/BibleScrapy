# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class DoubanMovieItem(scrapy.Item):
    # 电影排名
    rank = scrapy.Field()
    # 电影标题
    title = scrapy.Field()
    # 电影评分
    rating = scrapy.Field()
    # 评价人数
    rating_num = scrapy.Field()
    # 电影简介
    quote = scrapy.Field()
    # 导演和主演信息
    info = scrapy.Field()
    # 电影链接
    url = scrapy.Field()
    # 爬取时间
    crawl_time = scrapy.Field()

