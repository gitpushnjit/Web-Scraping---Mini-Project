# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import pymongo
class WebscrapingPipeline(object):

    def __init__(self):

        self.conn=pymongo.MongoClient(
            'localhost',
            2****
        )
        db=self.conn['WebScraping']
        self.connection=db['QuotesTable']


    def process_item(self, item, spider):
        self.connection.insert(dict(item))

