# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
from scrapy.exceptions import DropItem
from pymysql import cursors

class NewspiderPipeline(object):

    def process_item(self, item, spider):
        print("#########", item)

        return item


class JsonPipeline(object):
    def __init__(self):
        self.file = codecs.open('logs.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        # line = json.dumps(dict(item)) + '\n'
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()


class DuplicatesPipeline(object):

    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        if item['id'] in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(item['id'])
            return item
