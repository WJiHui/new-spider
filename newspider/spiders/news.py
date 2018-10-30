# -*- coding: utf-8 -*-
import scrapy 
from newspider import websites
from newspider.items import NewspiderItem 

def spider_factory(classname):
    
    # class_module =  __import__(classname)
    class_file = getattr(websites, classname)
    cls = getattr(class_file, classname.capitalize())
    spider = cls()
    return spider  


class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = []
    start_urls = {'people': 'http://www.people.com.cn/'}

    def start_requests(self):
        for website, url in self.start_urls.items():
            request = scrapy.Request(url=url, callback=self.parse, errback=None)
            request.meta['website'] = website 
            yield request

    def parse(self, response):
        website = response.meta['website']
        spider = spider_factory(website)
        spider.response = response
        spider.run()
        
        for category, title_url_dict in spider.new_dict.items():
            for title, url in title_url_dict.items():
                item = NewspiderItem()
                item['website'] = website 
                item['category'] = category 
                item['link'] = title 
                item['url'] = url 
                # item['posttime'] = None 
                yield 
        
