🇸🇪 Sweden's Postnummer CSV
=============================

This repo includes a single csv file ([postcodes.csv](postcodes.csv)) which is a dataset of [all
possible post numbers](https://en.wikipedia.org/wiki/List_of_postal_codes_in_Sweden)
in Sweden, along with names of streets within the postcode's geographic location.

You can read more about the postcodes format used in Sweden on [wikipedia](https://en.wikipedia.org/wiki/Postal_codes_in_Sweden).

This dataset is scraped from [Posten.se](http://www.posten.se) using the [search
service](http://www.posten.se/soktjanst/postnummersok/gb/index_v.jspv), as I couldn't
find a dataset of all postal codes in Sweden with street names and street/box-numbers of each one.

**Note:** Some of these postcodes don't have the entire set of street names and box
numbers within their area as the search page limits the number of results (~100),
for example: `647 91`.

**Here's an example set:**

```csv
A,B,C,D,E
11122,Korgmakargränd,2 - 6,111 22,Stockholm
11122,Kungsbron,1 - 23,111 22,Stockholm
11122,Kungsbron,2 - 30,111 22,Stockholm
11122,Kungsgatan,49 - 65,111 22,Stockholm
11122,Kungsgatan,56 - 74,111 22,Stockholm
11122,Målargatan,1 - 7,111 22,Stockholm
11122,Målargatan,2 - 6,111 22,Stockholm
11122,Olof Palmes Gata,17 - 31,111 22,Stockholm
11127,Bedoirsgränd,2 - 2,111 27,Stockholm
11127,Didrik Ficks Gränd,1 - 5,111 27,Stockholm
11127,Didrik Ficks Gränd,2 - 6,111 27,Stockholm
11127,Funckens Gränd,1 - 3,111 27,Stockholm
11127,Funckens Gränd,2 - 4,111 27,Stockholm
11127,Gåsgränd,1 - 7,111 27,Stockholm
11127,Gåsgränd,2 - 4,111 27,Stockholm
11127,Göran Hälsinges Gränd,3 - 5,111 27,Stockholm
11127,Göran Hälsinges Gränd,4 - 8,111 27,Stockholm
```

The columns are:

- **A:** Post code (as a single integer)
- **B:** Street name
- **C:** Street/post Box No.
- **D:** Post code (as it should be written/displayed)
- **E:** City/Locality

The scraping is done with a simple script written using [Scrapy](http://scrapy.org)
and is available in [src/scrape.py](src/scrape.py).

To run again, make sure you `pip install scrapy` and then just run:

```bash
scrapy runspider scrape.py
```

The code for the scraping script is licensed under [MIT](https://beshr.mit-license.org).
