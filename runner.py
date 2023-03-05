{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "617d7a22",
   "metadata": {},
   "outputs": [],
   "source": [
    "from twisted.internet import reactor\n",
    "\n",
    "from scrapy.crawler import CrawlerRunner\n",
    "from scrapy.utils.log import configure_logging\n",
    "from scrapy.utils.project import get_project_settings\n",
    "\n",
    "from project_parser_hh.spiders.hh_ru import HhRuSpider\n",
    "\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    configure_logging()\n",
    "    settings = get_project_settings()\n",
    "\n",
    "    runner = CrawlerRunner(settings)\n",
    "    runner.crawl(HhRuSpider)\n",
    "\n",
    "    reactor.run()"
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
