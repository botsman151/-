{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5495f9f5",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Define here the models for your scraped items\n",
    "#\n",
    "# See documentation in:\n",
    "# https://docs.scrapy.org/en/latest/topics/items.html\n",
    "\n",
    "import scrapy\n",
    "\n",
    "\n",
    "class InstaparserItem(scrapy.Item):\n",
    "    # define the fields for your item here like:\n",
    "    user_id = scrapy.Field()\n",
    "    username = scrapy.Field()\n",
    "    photo = scrapy.Field()\n",
    "    likes = scrapy.Field()\n",
    "    post_data = scrapy.Field()\n",
    "    _id = scrapy.Field()\n"
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
