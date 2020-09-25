import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://itcast.cn/channel/teacher.html']

    def parse(self, response):
        filename = "teacher.html"
        open(filename, 'w').write(response.body)
        pass
