# encoding:utf-8
from __future__ import print_function
import requests 
from bs4 import BeautifulSoup

class SpiderBase(object):
    def __init__(self):
        self.parser = 'html5lib' # html.parser lxml lxml-xml
        self.start_url = None
        self.response = None
    
    def request_url(self, url):
        response = requests.get(url)
        if response.status == '200':
            return response 
        else:
            print('***** request failed*****')
            return False 

    def download(self, url, path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)


class People(SpiderBase):
    def __init__(self):
        super(People, self).__init__()
        self.website = 'people'
        self.start_url = "http://www.people.com.cn/" 
        self.hot_news = {}
    
    def visit_nav(self, soup):
        body = soup.find(id='rmw_nav')
        nav = body.find('nav')
        nav_dict = {}
        for a in nav.find_all('a'):
            nav_dict[a.text] = a['href']
            print('nav', a.text, a['href'])
        return nav_dict

    def visit_home(self, soup):
        home = soup.find('section', class_='w1000 cont_a')
        for a in home.find_all('a'):
            if not a.text:
                continue
            print('xx', a['href'], a.text)
            self.hot_news[a.text] = a['href']
        

    def visit_page(self, title_url_dict, category):
        for text, href in self.hot_news.items():
            response = self.request_url(href)
            soup = BeautifulSoup(response.text, self.parser)
            article =  soup.find('div', class_='box_con')
            if article:
                with open('index.html', 'w') as f:
                    f.write(str(article))

    def run(self):
        print('people class')
        soup = BeautifulSoup(self.response.text, self.parser)
        self.visit_home(soup)
        self.visit_nav(soup) 

