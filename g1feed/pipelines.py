import pymongo
from g1feed.items import G1FeedItem


class G1FeedPipeline:
    def __init__(self, mongo_uri, mongo_db, collection_name):
        self.db = None
        self.mongo_client = None
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.collection_name = collection_name

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get("MONGO_URI"),
            mongo_db=crawler.settings.get("MONGO_DATABASE"),
            collection_name=crawler.settings.get("COLLECTION_NAME"),
        )

    def open_spider(self, spider):
        self.mongo_client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.mongo_client[self.mongo_db]

    def close_spider(self, spider):
        self.mongo_client.close()

    def process_item(self, item, spider):
        g1item = G1FeedItem(item)
        self.db[self.collection_name].insert_one(g1item.__dict__)
        return item
