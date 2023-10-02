from scrapy import Item, Field


class G1FeedItem(Item):
    title = Field()
    link = Field()
    description = Field()
    category = Field()
    pubDate = Field()
    source = Field()