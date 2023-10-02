from decouple import config

BOT_NAME = "g1feed"
SPIDER_MODULES = ["g1feed.spiders"]
NEWSPIDER_MODULE = "g1feed.spiders"
MONGO_URI = config('MONGO_URI')
MONGO_DATABASE = config('MONGO_DATABASE')
COLLECTION_NAME = config('COLLECTION_NAME')
ROBOTSTXT_OBEY = True
ITEM_PIPELINES = {
    "g1feed.pipelines.G1FeedPipeline": 300,
}
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
