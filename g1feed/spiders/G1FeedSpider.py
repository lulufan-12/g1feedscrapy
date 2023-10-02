from scrapy import Spider


class G1FeedSpider(Spider):
    name = "g1feedspider"
    allowed_domains = ["g1.globo.com"]
    start_urls = ["https://g1.globo.com/rss/g1/tecnologia/"]

    def parse(self, response):
        for item in response.css('item'):
            yield {
                'title': item.css('title::text').get(),
                'link': item.css('link::text').get(),
                'description': item.css('description::text').get(),
                'category': item.css('category::text').get(),
                'pubDate': item.css('pubDate::text').get(),
                'source': item.css('source::text').get(),
            }