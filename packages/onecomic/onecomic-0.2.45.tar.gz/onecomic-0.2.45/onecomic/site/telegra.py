import logging
from urllib.parse import urljoin

from ..crawlerbase import CrawlerBase

logger = logging.getLogger(__name__)


class TgCrawler(CrawlerBase):

    SITE = "telegra"
    SITE_INDEX = 'https://telegra.ph/'
    SOURCE_NAME = "telegra"
    LOGIN_URL = SITE_INDEX

    @property
    def source_url(self):
        return urljoin(self.SITE_INDEX, self.comicid)

    def get_comicbook_item(self):
        soup = self.get_soup(self.source_url)
        name = soup.h1.text
        desc = ""
        image_urls = []
        for figure in soup.find_all('figure'):
            image_url = figure.find('img').get('src')
            if image_url:
                image_urls.append(urljoin(self.SITE_INDEX, image_url))

        cover_image_url = image_urls[0] if image_urls else ''
        book = self.new_comicbook_item(name=name,
                                       desc=desc,
                                       cover_image_url=cover_image_url,
                                       source_url=self.source_url)
        book.add_chapter(chapter_number=1,
                         source_url=self.source_url,
                         title=name,
                         image_urls=image_urls)
        return book

    def get_chapter_image_urls(self, citem):
        return citem.image_urls
