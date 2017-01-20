#coding:utf8
from scrapy.spiders import Spider
from cnblogs.items import CnblogsItem

class CnblogsSpider(Spider):
    name = "cnblogs"
    allowed_domains = ["cnblogs.com"]
    start_urls = [
        "http://www.cnblogs.com/"
    ]

    def parse(self, response):
        self.log("Fetch cnblogs homepage: %s"%response.url)
        hxs = response.selector
        items = hxs.select("//a[@class='titlelnk']")

        item_list = []
        for data in items:
            item = CnblogsItem()
            item['Title'] = data.xpath("text()").extract()
            item['TitleUrl'] = data.xpath("@href").extract()
            item_list.append(item)

        return item_list
