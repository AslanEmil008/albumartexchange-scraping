# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter


# class AlbumartexchangePipeline:
#     def process_item(self, item, spider):
#         return item



import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from urllib.parse import urlparse

class CustomImagesPipeline(ImagesPipeline):
    
    def get_media_requests(self, item, info):
        # Download images using their URLs
        yield scrapy.Request(item['image_url'], meta={'item': item})
    
    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        # Set up a custom file naming scheme for the images
        img_name = item['image_url'].split('/')[-1]
        return f"images/{img_name}"
    
    def item_completed(self, results, item, info):
        # If the image was not downloaded, drop the item
        for ok, result in results:
            if not ok:
                raise DropItem(f"Failed to download image {item['image_url']}")
        return item
    
