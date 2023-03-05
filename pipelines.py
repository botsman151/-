{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "62428497",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Define your item pipelines here\n",
    "#\n",
    "# Don't forget to add your pipeline to the ITEM_PIPELINES setting\n",
    "# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html\n",
    "\n",
    "\n",
    "# useful for handling different item types with a single interface\n",
    "from itemadapter import ItemAdapter\n",
    "from pymongo import MongoClient\n",
    "\n",
    "\n",
    "class ProjectParserHhPipeline:\n",
    "    def __init__(self):\n",
    "        client = MongoClient('localhost', 27017)\n",
    "        self.mongobase = client.vacancies_python_hh\n",
    "\n",
    "\n",
    "    def process_item(self, item, spider):\n",
    "        collection = self.mongobase[spider.name]\n",
    "        collection.insert_one(item)\n",
    "\n",
    "        return item"
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
