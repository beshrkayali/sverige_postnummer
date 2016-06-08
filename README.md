🇸🇪 Sweden's Postnummer Dataset
=================================

This is  a dataset of [all possible post numbers](https://en.wikipedia.org/wiki/List_of_postal_codes_in_Sweden)
in Sweden, along with names of streets within the postcode's geographic location, provided in CSV and JSON format.

You can read more about the postcodes format used in Sweden on [wikipedia](https://en.wikipedia.org/wiki/Postal_codes_in_Sweden).

This dataset is scraped from [Posten.se](http://www.posten.se) using the [search
service](http://www.posten.se/soktjanst/postnummersok/gb/index_v.jspv), as I couldn't
find a dataset of all postal codes in Sweden with street names and street/box-numbers of each one.

**Note:** Some of these postcodes don't have the entire set of street names and box
numbers within their area as the search page limits the number of results (~100),
for example: `647 91`.

**Here's an example:**

```csv
Code,Street Name,Street/Box No.,Postcode,City/Locality
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

**An example of from the json set:**

```json
["11331", [{"Street/Box No.": "47 - 59", "Street Name": "Dalagatan", "City/Locality": "Stockholm", "Postcode": "113 31"}, {"Street/Box No.": "21 - 51", "Street Name": "Hälsingegatan", "City/Locality": "Stockholm", "Postcode": "113 31"}, {"Street/Box No.": "1 - 11", "Street Name": "Hälsingehöjden", "City/Locality": "Stockholm", "Postcode": "113 31"}, {"Street/Box No.": "2 - 2", "Street Name": "Hälsingehöjden", "City/Locality": "Stockholm", "Postcode": "113 31"}, {"Street/Box No.": "96 - 124", "Street Name": "Sankt Eriksgatan", "City/Locality": "Stockholm", "Postcode": "113 31"}, {"Street/Box No.": "97 - 111", "Street Name": "Sankt Eriksgatan", "City/Locality": "Stockholm", "Postcode": "113 31"}, {"Street/Box No.": "1 - 5", "Street Name": "Vanadisplan", "City/Locality": "Stockholm", "Postcode": "113 31"}, {"Street/Box No.": "2 - 8", "Street Name": "Vanadisplan", "City/Locality": "Stockholm", "Postcode": "113 31"}, {"Street/Box No.": "40 - 44", "Street Name": "Vanadisvägen", "City/Locality": "Stockholm", "Postcode": "113 31"}]]
["11333", [{"Street/Box No.": "1 - 9", "Street Name": "Kadettgatan", "City/Locality": "Stockholm", "Postcode": "113 33"}, {"Street/Box No.": "2 - 2", "Street Name": "Kadettgatan", "City/Locality": "Stockholm", "Postcode": "113 33"}, {"Street/Box No.": "1 - 11", "Street Name": "Rödabergsgatan", "City/Locality": "Stockholm", "Postcode": "113 33"}, {"Street/Box No.": "2 - 16", "Street Name": "Rödabergsgatan", "City/Locality": "Stockholm", "Postcode": "113 33"}, {"Street/Box No.": "1 - 1", "Street Name": "Tempeltrappan", "City/Locality": "Stockholm", "Postcode": "113 33"}, {"Street/Box No.": "2 - 2", "Street Name": "Tempeltrappan", "City/Locality": "Stockholm", "Postcode": "113 33"}, {"Street/Box No.": "2 - 2", "Street Name": "Väringgatan", "City/Locality": "Stockholm", "Postcode": "113 33"}, {"Street/Box No.": "9 - 27", "Street Name": "Väringgatan", "City/Locality": "Stockholm", "Postcode": "113 33"}]]
["11332", [{"Street/Box No.": "2 - 24", "Street Name": "Falugatan", "City/Locality": "Stockholm", "Postcode": "113 32"}, {"Street/Box No.": "3 - 23", "Street Name": "Falugatan", "City/Locality": "Stockholm", "Postcode": "113 32"}, {"Street/Box No.": "65 - 95", "Street Name": "Sankt Eriksgatan", "City/Locality": "Stockholm", "Postcode": "113 32"}, {"Street/Box No.": "8 - 10", "Street Name": "Sankt Eriksplan", "City/Locality": "Stockholm", "Postcode": "113 32"}, {"Street/Box No.": "19 - 19", "Street Name": "Sankt Eriksplan", "City/Locality": "Stockholm", "Postcode": "113 32"}]]
["11335", [{"Street/Box No.": "47 - 89", "Street Name": "Karlbergsvägen", "City/Locality": "Stockholm", "Postcode": "113 35"}, {"Street/Box No.": "62 - 86", "Street Name": "Karlbergsvägen", "City/Locality": "Stockholm", "Postcode": "113 35"}]]
["11334", [{"Street/Box No.": "9 - 49", "Street Name": "Norrbackagatan", "City/Locality": "Stockholm", "Postcode": "113 34"}, {"Street/Box No.": "34 - 94", "Street Name": "Norrbackagatan", "City/Locality": "Stockholm", "Postcode": "113 34"}]]
["11337", [{"Street/Box No.": "39 - 45", "Street Name": "Karlbergsvägen", "City/Locality": "Stockholm", "Postcode": "113 37"}, {"Street/Box No.": "46 - 60", "Street Name": "Karlbergsvägen", "City/Locality": "Stockholm", "Postcode": "113 37"}, {"Street/Box No.": "45 - 81", "Street Name": "Torsgatan", "City/Locality": "Stockholm", "Postcode": "113 37"}, {"Street/Box No.": "48 - 82", "Street Name": "Torsgatan", "City/Locality": "Stockholm", "Postcode": "113 37"}]]
["11336", [{"Street/Box No.": "1 - 21", "Street Name": "Birkagatan", "City/Locality": "Stockholm", "Postcode": "113 36"}, {"Street/Box No.": "2 - 12", "Street Name": "Birkagatan", "City/Locality": "Stockholm", "Postcode": "113 36"}, {"Street/Box No.": "1 - 11", "Street Name": "Bråvallagatan", "City/Locality": "Stockholm", "Postcode": "113 36"}, {"Street/Box No.": "2 - 14", "Street Name": "Bråvallagatan", "City/Locality": "Stockholm", "Postcode": "113 36"}, {"Street/Box No.": "1 - 9", "Street Name": "Robert Almströmsgatan", "City/Locality": "Stockholm", "Postcode": "113 36"}, {"Street/Box No.": "2 - 14", "Street Name": "Robert Almströmsgatan", "City/Locality": "Stockholm", "Postcode": "113 36"}]]
["11339", [{"Street/Box No.": "14 - 36", "Street Name": "Birkagatan", "City/Locality": "Stockholm", "Postcode": "113 39"}, {"Street/Box No.": "23 - 35", "Street Name": "Birkagatan", "City/Locality": "Stockholm", "Postcode": "113 39"}, {"Street/Box No.": "1 - 23", "Street Name": "Tomtebogatan", "City/Locality": "Stockholm", "Postcode": "113 39"}, {"Street/Box No.": "2 - 16", "Street Name": "Tomtebogatan", "City/Locality": "Stockholm", "Postcode": "113 39"}]]
["43221", [{"Street/Box No.": "1 - 49", "Street Name": "Box", "City/Locality": "Varberg", "Postcode": "432 21"}]]
["43222", [{"Street/Box No.": "50 - 99", "Street Name": "Box", "City/Locality": "Varberg", "Postcode": "432 22"}]]
["43223", [{"Street/Box No.": "100 - 149", "Street Name": "Box", "City/Locality": "Varberg", "Postcode": "432 23"}]]
```

The scraping is done with a simple script written using [Scrapy](http://scrapy.org)
and is available in [src/scrape.py](src/scrape.py).

To run again, make sure you `pip install scrapy` and then just run:

```bash
scrapy runspider scrape.py
```

The code for the scraping script is licensed under [MIT](https://beshr.mit-license.org).
