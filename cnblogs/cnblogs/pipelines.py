# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
import MySQLdb.cursors
import logging
from twisted.enterprise import adbapi


class CnblogsPipeline(object):
    def __init__(self):
        self.dbpool = adbapi.ConnectionPool(
                    dbapiName = "MySQLdb",
                    host = "127.0.0.1",
                    db = "scrapy",
                    user = "root",
                    passwd = "123456mac",
                    cursorclass = MySQLdb.cursors.DictCursor,
                    charset = "utf8",
                    use_unicode = False
                )
    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        logging.debug(query)
        return item

    def _conditional_insert(self, tx, item):
        parms = (MySQLdb.escape_string(item['Title'][0].encode('utf8')), MySQLdb.escape_string(item['TitleUrl'][0].encode('utf8')))
        sql = "insert into blogs (Title, TitleUrl) values('%s', '%s')" % parms
        tx.execute(sql)
        return
