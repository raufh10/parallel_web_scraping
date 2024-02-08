# Project Title

## Overview

This project offers a suite of web scraping tools designed to enable parallel scraping of heavy JavaScript websites. By leveraging the capabilities of the Playwright library for browser automation and the BeautifulSoup4 library for HTML parsing, these tools provide a robust solution for efficiently handling dynamic web content. The design emphasizes modularity and ease of use, allowing users to customize their scraping tasks to meet diverse requirements. Whether you're dealing with single-page applications or complex web portals, this toolkit simplifies the extraction of valuable data from the modern web.

## Requirements

To use this project, you will need to install the following Python packages:

- beautifulsoup4==4.12.3
- greenlet==3.0.3
- lxml==5.1.0
- numpy==1.26.4
- pandas==2.2.0
- playwright==1.41.1
- pyee==11.0.1
- python-dateutil==2.8.2
- pytz==2024.1
- six==1.16.0
- soupsieve==2.5
- typing_extensions==4.9.0
- tzdata==2023.4

These packages can be installed using the command: pip install -r requirements.txt

## How to Use It

1. Clone the repository to your local machine.
2. Install the required Python packages listed in `requirements.txt`, you can do this by running the command: pip install -r requirements.txt
3. Explore the `examples.py` for sample implementations or use the functions provided in `utility.py` to create your own scraping scripts.
4. Customize the functions and scripts according to your specific data parsing and web scraping needs.

## Current List of Method Functions

### In `examples.py`

- `main`: Main function to demonstrate example usage of the utility functions like how to run the tool.
- `interaction`: Function to handle user interactions.
- `parse`: Function to parse the input data.

### In `utility.py`

- `loading_page`: Method to handle the loading of web pages.
- `fetch`: Method to fetch data from the web.
- `interaction`: Method to manage interactions with web elements.
- `parse`: Method to parse web content.
- `response_collector`: Method to collect responses from web requests.
- `response_parser`: Method to parse responses.
- `run`: Method to execute the main functionality.

Please refer to the source code for detailed implementation and usage of these methods.
