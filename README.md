🇸🇪 Sweden Postnummer Dataset
===============================

This is  a dataset of [all possible post numbers](https://en.wikipedia.org/wiki/List_of_postal_codes_in_Sweden)
in Sweden, along with names of streets within the postcode's geographic location, provided in [CSV](postcodes.csv) and [JSON](postcodes.json) format.

You can read more about the postcodes format used in Sweden on [wikipedia](https://en.wikipedia.org/wiki/Postal_codes_in_Sweden).

This dataset is scraped from [Posten.se](http://www.posten.se) using the [search
service](http://www.posten.se/soktjanst/postnummersok/gb/index_v.jspv), as I couldn't
find a dataset of all postal codes in Sweden with street names and street/box-numbers of each one.

**Note:** Some of these postcodes don't have the entire set of street names and box
numbers within their area as the search page limits the number of results (~100),
for example: `647 91`.

The scraping is done with a simple script written using [Scrapy](http://scrapy.org)
and is available in [src/scrape.py](src/scrape.py).

To run again, make sure you `pip install scrapy` and then just run:

```bash
scrapy runspider scrape.py
```

The code for the scraping script is licensed under [MIT](https://beshr.mit-license.org).
