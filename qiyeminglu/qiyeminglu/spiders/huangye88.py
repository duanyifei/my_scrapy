#coding:utf8
import scrapy
from qiyeminglu.items import QiyemingluItem

class HuangYe88(scrapy.spiders.Spider):
    name = 'huangye88'
    allowed_domains = ['huangye88.com']
    start_urls = [
                'http://b2b.huangye88.com/henan/fuwu/',
                'http://b2b.huangye88.com/henan/fuwu946/pn2/',
                ]

    def parse(self, response):
        items = []
        loops = response.xpath('//form[@id="jubao"]/dl/dt')
        for dt in loops:
            item = QiyemingluItem()
            name = dt.xpath("h4/a/text()").extract()
            phone = dt.xpath("span/a/text()").extract()
            if (not name) or (not name[0]):
                continue
            phone = phone[0] if phone else ''
            item['name'] = name[0]
            item['phone'] = phone
            items.append(item)
        return items
