{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f9ddfdc9",
   "metadata": {},
   "outputs": [],
   "source": [
    "import scrapy\n",
    "from scrapy.http import HtmlResponse\n",
    "from project_parser_hh.items import ProjectParserHhItem\n",
    "\n",
    "\n",
    "class HhRuSpider(scrapy.Spider):\n",
    "\n",
    "    name = 'hh_ru'\n",
    "    allowed_domains = ['hh.ru']\n",
    "    start_urls = [\n",
    "        'https://spb.hh.ru/search/vacancy?area=76&search_field=name&search_field=company_name&search_field=description&text=python&no_magic=true&L_save_area=true&items_on_page=20',\n",
    "        'https://spb.hh.ru/search/vacancy?area=88&search_field=name&search_field=company_name&search_field=description&text=python&no_magic=true&L_save_area=true&items_on_page=20'\n",
    "    ]\n",
    "\n",
    "    def parse(self, response: HtmlResponse):\n",
    "        next_page = response.xpath(\"//a[@data-qa='pager-next']/@href\").get()\n",
    "\n",
    "        if next_page:\n",
    "            yield response.follow(next_page, callback=self.parse)\n",
    "\n",
    "        urls_vacancies = response.xpath(\"//div[@class='serp-item']//a[@data-qa='vacancy-serp__vacancy-title']/@href\").getall()\n",
    "        for url_vacancy in urls_vacancies:\n",
    "            yield response.follow(url_vacancy, callback=self.vacancy_parse)\n",
    "\n",
    "    def vacancy_parse(self, response: HtmlResponse):\n",
    "        vacancy_name = response.css(\"h1::text\").get()\n",
    "        vacancy_salary = response.xpath(\"//div[@data-qa='vacancy-salary']//text()\").getall()\n",
    "        vacancy_url = response.url\n",
    "\n",
    "        yield ProjectParserHhItem(\n",
    "            name=vacancy_name,\n",
    "            salary=vacancy_salary,\n",
    "            url=vacancy_url\n",
    "        )"
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
