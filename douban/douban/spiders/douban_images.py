from scrapy.spiders import Spider
from douban.items import ImageItem
from scrapy.http import Request


class download_image(Spider):
    name = 'download_image'
    def __init__(self, url='128308020', *args, **kwargs):
        self.allowed_domains = ['douban.com']
        self.start_urls = [
            'http://www.douban.com/photos/album/%s/' % url,
        ]
        self.url = url
        super(download_image, self).__init__(*args, **kwargs)
    
    def parse(self, response):
        list_image = response.xpath("//div[@class='photolst clearfix']//img/@src").extract()
        if list_image:
            item = ImageItem()
            item['image_urls'] = list_image
            yield item