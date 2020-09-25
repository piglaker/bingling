import scrapy


class PixivSpider(scrapy.Spider):
    name = 'pixiv'
    allowed_domains = ['alibabacloud.com']
    start_urls = ['https://www.alibabacloud.com/help/zh/doc-detail/31883.htm']

    def parse(self, response):
        filename = "31883.html"
        print(response)
        open(filename, 'w').write(str(response.body, encoding="utf-8"))
        pass
