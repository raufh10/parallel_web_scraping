import time
from src import ScraperWorker
# Ensure you have Playwright installed for browser automation
# and BeautifulSoup for HTML parsing.

class ToScrapeWorker(ScraperWorker):
    """
    A specialized scraper worker for "http://quotes.toscrape.com/".

    This class extends `ScraperWorker` by implementing specific interaction
    and parsing logic to scrape quotes from the website. It utilizes the
    Playwright library for browser automation to interact with web elements and
    navigate pages, and BeautifulSoup from bs4 for parsing HTML content.
    """

    def interaction(self, page):
        """
        Interacts with the web page using Playwright to ensure all necessary elements are loaded.

        Utilizes Playwright's page.keyboard.press to simulate keyboard actions,
        such as paging down to trigger lazy-loaded content and returning to the
        top of the page. These interactions are essential for ensuring that dynamic
        content is fully loaded before scraping.

        Parameters:
        - page: The Playwright page object to interact with.
        """
        for _ in range(3):
            page.keyboard.press('PageDown')  # Simulate pressing the Page Down key
            time.sleep(1)  # Wait a bit for the page to load content
        page.keyboard.press('Home')  # Simulate pressing the Home key to return to the top

        self.fetch(page)  # Triggers the fetch method to process the loaded page
    
    def parse(self, response):
        """
        Parses the fetched page to extract quotes and their authors using BeautifulSoup.

        This method employs BeautifulSoup (bs4) to parse the HTML content of the response.
        It searches for div elements with the class "quote" to extract text and author
        information, showcasing how to handle and parse HTML content efficiently.

        Parameters:
        - response: The HTML response object to parse, expected to be a BeautifulSoup object.
        """
        try:
            # Utilize BeautifulSoup's find_all method to locate elements by class
            quotes_tag = response.find_all("div", class_="quote")
            for item in quotes_tag:
                try:
                    author = item.find("small", class_="author").text  # Extract author
                    quote = item.find("span", class_="text").text  # Extract quote text
                    print(f"Author: {author}, Quote: {quote}")
                except:
                    print("No author or quote found")
        except Exception as e:
            print(f"Error in parse: {e}")

def main():
    """
    Main function to initiate scraping process.

    Constructs a list of URLs to scrape and initializes a `ToScrapeWorker`
    instance to scrape quotes from each page. Demonstrates how to configure
    and use Playwright for browser interactions and BeautifulSoup for parsing
    HTML in a real-world scraping project.
    """
    urls = ["http://quotes.toscrape.com/"]

    # Generate URLs for subsequent pages
    for i in range(2, 11):
        urls.append(f"http://quotes.toscrape.com/page/{i}/")

    # Initialize the scraper worker
    yp_worker = ToScrapeWorker(start_urls=urls, worker_number=5, headless=False)

    # Start the scraping process
    yp_worker.run()

if __name__ == "__main__":
    main()
