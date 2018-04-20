# tripdriver !!

A python3 application to scrape comments from a given set of pages on tripadvisor.

## Usage

#### To Scrape a Single Page's Comments

  Tripdriver contains a class called getComments.py. To scrape a single page, change the hard coded url variable in getComments.py and then run getComments.py as `__main__` :
  
    `if __name__ == "__main__":
       ...
       url = "tripadvisor.com/some_url_you_want_to_scrape"`
     
  getComments.py will scrape the indicated page and save results as a .xlsx file with a name based on the url provided.
  
#### To Scrape a List of Pages

  Tripdriver contains a class called tripdriver.py which will use a Tripadvisor page containing a set of links as an index to scrape multiple pages. To do this, change the hard coded url variable in tripdriver.py and then run as `__main__` :
  
    `if __name__ == "__main__":
       ...
       url = "tripadvisor.com/some_url_you_want_to_use_as_index"`
       
  tripdriver.py will scrape each indexed page and save results as a .xlsx file with a name based on the url of the scraped page.
 

## Output

  Tripdriver's output is now in .xlsx format with each row representing a given comment of a scraped page and five columns representing place of posting user, date of post, rating (10, 20, 30, 40, 50), and comment text. The example below contains explanitory headers, these awre not added to output files
  
  |Place|Date|Rating|Title|Text|
  |:----|:---|:----:|:----|:---|
  |someCity, someCountry|someTime|50|The Title of my Comment|The things I said about some place.|
  
  Each file is saved with a name derived from the url of its source.

### Dependancies

This project depends on: 

* `Selenium Webdriver` 
* `Firefox`
* `BeautifulSoup4`
* `geckodriver`
* `openpyxl`
