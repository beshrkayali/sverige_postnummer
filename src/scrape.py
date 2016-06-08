# -*- coding: utf-8 -*-
from operator import methodcaller
from itertools import product
import scrapy
import codecs


class PostalScraper(scrapy.Spider):
    name = 'PostalSpider'
    start_urls = ['http://www.posten.se/soktjanst/postnummersok/gb/index_v.jspv']

    def parse(self, response):
        zip_codes = product(range(1, 10), repeat=5)
        for code in zip_codes:
            code = ''.join([str(digit) for digit in code])
            yield scrapy.http.FormRequest.from_response(
                response,
                formdata={'pnr': code},
                callback=lambda r, code=code: self.after_post(r, code)
            )

    def after_post(self, response, code):
        if "Your search produced no hits." not in response.body:
            with codecs.open('postcodes.csv', "ab", "utf-8") as csv_file:
                with codecs.open('errors.csv', "ab", "utf-8") as errors_file:
                    for result in response.css('table.result').css('tr'):
                        try:
                            if len(result.css('td::text').extract()) == 3:
                                street_name, post_code, city = \
                                    result.css('td::text').extract()
                                po_box_no = ''
                            else:
                                street_name, po_box_no, post_code, city = \
                                    result.css('td::text').extract()

                            titler = methodcaller('title')
                            txt = u','.join(
                                map(titler,
                                    (street_name, po_box_no, post_code, city))
                            )
                            csv_file.write(u'%s,%s\n' % (code, txt))
                        except:
                            errors_file.write('%s\n' % code)
