# tripdriver !!

A python3 application to scrape comments from a given set of pages on tripadvisor.

## Usage

At the moment `tripindex.py`, the part of the srcipt which indexes the pages to be scraped, simply takes a hardcoded url in the `__main__` method.  The default url is for the Cairo Governate in Egypt. If annother city is desired, simply change the url to a similar one for a different place. 

The script should be run either as main from a python console using tripindex.py as the active srcipt or from the command line as `python3 tripindex.py`. `tripindex.py` will call separate instances of `tripdriver.py`, which should not need modification. 

## Dependancies

This project depends on: 

*`Selenium Webdriver`, `Firefox`, `BeautifulSoup4`, `geckodriver`
