# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import mysql.connector
class WebscrapingPipeline(object):

    def __init__(self):
        self.createConn()
        self.createTable()

    def createConn(self):
        self.conn=mysql.connector.connect(
            host= 'localhost',
            user='root',
            passwd='************',
            database='webscrapingquotes'
        )
        self.cur=self.conn.cursor()

    def createTable(self):
        self.cur.execute("""drop table if exists quotesTable""")
        self.cur.execute("""create table quotesTable(
                        quotes text,
                        authors text,
                        tags text)""")

    def process_item(self, item, spider):
        self.storeDB(item)
        print("Pipeline :"+item['quotes'][0])
        return item

    def storeDB(self,item):
        self.cur.execute("""insert into quotesTable values (%s,%s,%s)""",(
            item['quotes'][0],
            item['authors'][0],
            item['tags'][0]
        ))
        self.conn.commit()
