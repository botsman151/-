{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "26318512",
   "metadata": {},
   "outputs": [],
   "source": [
    "import scrapy\n",
    "from scrapy.http import HtmlResponse\n",
    "from hardware_store_parser.items import HardwareStoreParserItem\n",
    "from scrapy.loader import ItemLoader\n",
    "\n",
    "\n",
    "class CastoramaRuSpider(scrapy.Spider):\n",
    "    name = 'castorama_ru'\n",
    "    allowed_domains = ['castorama.ru']\n",
    "\n",
    "    def __init__(self, **kwargs):\n",
    "        super().__init__(**kwargs)\n",
    "        self.start_urls = [f\"https://www.castorama.ru/catalogsearch/result/?q={kwargs.get('search')}\"]\n",
    "\n",
    "    # start_urls = ['http://castorama.ru/']\n",
    "\n",
    "    def parse(self, response: HtmlResponse):\n",
    "        print(response.url)\n",
    "        next_page = response.xpath(\"//a[@class='next i-next']/@href\").get()\n",
    "        if next_page:\n",
    "            yield response.follow(next_page, callback=self.parse)\n",
    "        links = response.xpath(\"//a[contains(@class, 'product-card__name')]\")\n",
    "        for link in links:\n",
    "            yield response.follow(link, callback=self.goods_parse)\n",
    "\n",
    "    def goods_parse(self, response: HtmlResponse):\n",
    "        loader = ItemLoader(item=HardwareStoreParserItem(), response=response)\n",
    "        loader.add_xpath('good_name', \"//h1/text()\")\n",
    "        loader.add_xpath('price', \"//span[@class='price']//text()\")\n",
    "        loader.add_value('link', response.url)\n",
    "        loader.add_xpath('images', \"//div[@class='js-zoom-container']//@data-src\")\n",
    "        loader.add_xpath('product_characteristics_keys', \"//div[contains(@class, 'product-block')]//dl[contains(@class, 'specs-table')]/dt/span[contains(@class, 'specs-table__attribute-name')]/text()\")\n",
    "        loader.add_xpath('product_characteristics_values', \"//div[contains(@class, 'specifications')]//dd[contains(@class, 'specs-table__attribute-value')]/text()\")\n",
    "        yield loader.load_item()"
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
