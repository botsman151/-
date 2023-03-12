{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "278976f8",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Define your item pipelines here\n",
    "#\n",
    "# Don't forget to add your pipeline to the ITEM_PIPELINES setting\n",
    "# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html\n",
    "import scrapy\n",
    "# useful for handling different item types with a single interface\n",
    "from itemadapter import ItemAdapter\n",
    "from scrapy.pipelines.images import ImagesPipeline\n",
    "from pymongo import MongoClient\n",
    "import hashlib\n",
    "from scrapy.utils.python import to_bytes\n",
    "\n",
    "\n",
    "class HardwareStoreParserPipeline:\n",
    "    def __init__(self):\n",
    "        client = MongoClient('127.0.0.1', 27017)\n",
    "        self.mongo_base = client.db_hardware_store\n",
    "\n",
    "    def process_item(self, item, spider):\n",
    "        if item:\n",
    "            item['price'] = int(item['price'].replace(' ', ''))\n",
    "            item['product_characteristics'] = dict(zip(item['product_characteristics_keys'], item['product_characteristics_values']))\n",
    "            del item['product_characteristics_keys'], item['product_characteristics_values']\n",
    "            collection = self.mongo_base[spider.name]\n",
    "            collection.insert_one(item)\n",
    "        return item\n",
    "\n",
    "\n",
    "class PhotosPipeline(ImagesPipeline):\n",
    "    def get_media_requests(self, item, info):\n",
    "        if item['images']:\n",
    "            for img in item['images']:\n",
    "                try:\n",
    "                    yield scrapy.Request(img)\n",
    "                except Exception as e:\n",
    "                    print(e)\n",
    "\n",
    "    def item_completed(self, results, item, info):\n",
    "        item['images'] = [itm[1] for itm in results if itm[0]]\n",
    "        return item\n",
    "\n",
    "    def file_path(self, request, response=None, info=None, *, item=None):\n",
    "        print()\n",
    "        image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()\n",
    "        return f\"full/{item['good_name']}/{image_guid}.jpg\""
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
