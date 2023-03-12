{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "885496a6",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'hardware_store_parser'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-2-42b9aa61595b>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0msys\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      6\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0mcryptography\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mhazmat\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mbindings\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mopenssl\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mbinding\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mBinding\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 7\u001b[1;33m \u001b[1;32mfrom\u001b[0m \u001b[0mhardware_store_parser\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mspiders\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcastorama_ru\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mCastoramaRuSpider\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      8\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      9\u001b[0m \u001b[1;32mif\u001b[0m \u001b[0m__name__\u001b[0m \u001b[1;33m==\u001b[0m \u001b[1;34m'__main__'\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'hardware_store_parser'"
     ]
    }
   ],
   "source": [
    "from twisted.internet import reactor\n",
    "from scrapy.crawler import CrawlerRunner\n",
    "from scrapy.utils.project import get_project_settings\n",
    "from scrapy.utils.log import configure_logging\n",
    "import sys\n",
    "from cryptography.hazmat.bindings.openssl.binding import Binding\n",
    "from hardware_store_parser.spiders.castorama_ru import CastoramaRuSpider\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    search = \"котел\"\n",
    "    if len(sys.argv) != 1:\n",
    "        search = ' '.join(sys.argv[1:])\n",
    "\n",
    "    configure_logging()\n",
    "    settings = get_project_settings()\n",
    "    runner = CrawlerRunner(settings)\n",
    "    runner.crawl(CastoramaRuSpider, search=search)\n",
    "    d = runner.join()\n",
    "    d.addBoth(lambda _: reactor.stop())\n",
    "    reactor.run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3f257f0b",
   "metadata": {},
   "outputs": [],
   "source": []
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
