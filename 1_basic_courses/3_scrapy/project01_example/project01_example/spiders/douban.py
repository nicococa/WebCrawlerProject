import scrapy
from scrapy import Selector
from ..items import Project01ExampleItem

class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["movie.douban.com"]
    start_urls = ["https://movie.douban.com/top250?start=0&filter="]

    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            "Referer": "https://movie.douban.com/"
        }
        for page_num in range(10):  # 这里示例前 5 页
            start_num = page_num * 25
            url = f'https://movie.douban.com/top250?start={start_num}&filter='
            yield scrapy.Request(
                url=url,
                callback=self.parse,
                headers=headers,
            )

    def parse(self, response):
        tree = Selector(text=response.text)
        articles_items = tree.xpath("//ol[@class='grid_view']/li")
        for article in articles_items:
            item = Project01ExampleItem()
            item['title'] = article.xpath("div//div[@class='hd']/a/span[1]/text()").get()
            item['score'] = article.xpath("div//div[@class='bd']//span[@class='rating_num']/text()").get()
            item['motto'] = article.xpath("div//div[@class='bd']//p[@class='quote']/span/text()").get()
            yield item
