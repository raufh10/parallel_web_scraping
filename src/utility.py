import time
import threading

from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright, Page

class PageInteraction:

    def __init__(self, page: Page):
        self.page = page

    def loading_page(self, url: str):
        """Loads a given URL and optionally scrolls through the page."""
        while True:
            try:
                self.page.goto(url, timeout=300000)
                self.page.wait_for_load_state()
                break
            except Exception as e:
                print(f"Error in loading_page on {url}: {e}")
                time.sleep(5)  # Sleep before retrying
    
class ScraperWorker:

    def __init__(self, start_urls, worker_number, headless):
        self.worker_number = worker_number
        self.headless = headless
        
        if isinstance(start_urls, list):
            self.undivided_input_list = start_urls
            self.job_size = max(1, len(start_urls) // self.worker_number)
            self.divided_input_list = [start_urls[i:i + self.job_size] for i in range(0, len(start_urls), self.job_size)]
        else:
            raise TypeError("start_urls should be a list.")

        self.soup_list = []
        self.list_lock = threading.Lock()

    def fetch(self, page):
        """Fetches the BeautifulSoup object from the current page content."""
        try:
            soup = BeautifulSoup(page.content(), 'lxml')
            with self.list_lock:  # Ensure thread safety
                self.soup_list.append(soup)
        except Exception as e:
            print(f"Error in fetch_soup: {e}")

    def interaction(self, page):
        raise NotImplementedError("This method should be implemented by subclasses.")

    def parse(self, response):
        raise NotImplementedError("This method should be implemented by subclasses.")

    def response_collector(self, divided_list):
        try:
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=self.headless)
                context = browser.new_context()
                page = context.new_page()

                pi = PageInteraction(page)

                for item in divided_list:
                    pi.loading_page(item)
                    page.wait_for_load_state()
                    self.interaction(page)

                browser.close()
        except Exception as e:
            print(f"Error in soup_collector_crawler: {e}")

    def response_parser(self):
        input_length = len(self.undivided_input_list)
        counter = 0

        while True:
            if len(self.soup_list) != 0:
                with self.list_lock:
                    for item in self.soup_list.copy():
                        self.parse(item)
                        self.soup_list.remove(item)
                        counter += 1
            else:
                if counter < input_length:
                    time.sleep(1)  # Prevent high CPU usage
                    continue
                else:
                    break

    def run(self):
        threads = []
        for divided_list in self.divided_input_list:
            t = threading.Thread(target=self.response_collector, args=(divided_list,))
            threads.append(t)
            t.start()

        t = threading.Thread(target=self.response_parser, args=())
        threads.append(t)
        t.start()

        for thread in threads:
            thread.join()
