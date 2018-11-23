# -*- coding: utf-8 -*-
import scrapy 
from newspider import websites
from newspider.items import NewspiderItem 


def spider_factory(class_name):
    class_file = getattr(websites, class_name)
    cls = getattr(class_file, class_name.capitalize())
    spider = cls()
    return spider  


class NewsSpider(scrapy.Spider):
    name = 'new'
    allowed_domains = []
    start_urls = {'people': 'http://www.people.com.cn/'}
    # custom_settings = {
    #     'ITEM_PIPELINES': {'pipelineClass1': 300,
    #                        'pipelineClass2': 400},
    # }
    
    def start_requests(self):
        for site, url in self.start_urls.items():
            request = scrapy.Request(url=url, callback=self.parse, errback=None)
            request.meta['site'] = site
            yield request

    def parse(self, response):
        site = response.meta['site']
        spider = spider_factory(site)
        spider.response = response
        # spider.run()
       
        new_dict = {'redian': {'toutiao1': 'url1', 'toutiao2': 'url2'}}
        for category, title_url_dict in new_dict.items():
            for title, url in title_url_dict.items():
                item = NewspiderItem()
                item['site'] = site
                item['category'] = category 
                item['title'] = title 
                item['url'] = url 
                # item['posttime'] = None 
                yield item         
