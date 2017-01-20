# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json


class QiyemingluPipeline(object):
    def process_item(self, item, spider):
        return item


class JsonPipeline(object):
    def __init__(self):
        self.file = open('qiyeminglu.json', 'a')

    def __del__(self):
        self.file.close()

    def process_item(self, item, spider):
        self.file.write(json.dumps(dict(item), ensure_ascii=False).encode('utf8'))
        return item

