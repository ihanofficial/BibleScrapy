import scrapy


import scrapy
from douban_movie.items import DoubanMovieItem
from scrapy.http import Request
from datetime import datetime

class DoubanTop250Spider(scrapy.Spider):
    name = 'douban_top250'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    # 自定义设置
    custom_settings = {
        'DOWNLOAD_DELAY': 2,  # 下载延迟，避免请求过快
        'DEFAULT_REQUEST_HEADERS': {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
        }
    }

    def parse(self, response):
        # 解析当前页的电影信息
        movies = response.css('.item')
        for movie in movies:
            item = DoubanMovieItem()
            item['rank'] = movie.css('.pic em::text').get()
            item['title'] = movie.css('.title::text').get()
            item['rating'] = movie.css('.rating_num::text').get()
            item['rating_num'] = movie.css('.star span:nth-child(4)::text').re_first(r'(\d+)')
            item['quote'] = movie.css('.inq::text').get()
            item['info'] = movie.css('.bd p:nth-child(1)::text').get().strip()
            item['url'] = response.urljoin(movie.css('.hd a::attr(href)').get())
            item['crawl_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            yield item

        # 处理分页
        next_page = response.css('.next a::attr(href)').get()
        if next_page:
            next_url = response.urljoin(next_page)
            yield Request(next_url, callback=self.parse)
