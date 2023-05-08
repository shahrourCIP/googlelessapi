import requests
from bs4 import BeautifulSoup

import scrapy
from urllib.parse import urlencode
from urllib.parse import urlparse
import json
from datetime import datetime

import scrapy
from urllib.parse import urlencode
from urllib.parse import urlparse
import json
from datetime import datetime

# Set the search query
# query = """
# site:jo.linkedin.com/in "PMP" AND "Government"
# """
def get_res(query:str):
    all_res = []
    # Set the number of pages to scrape
    num_pages = 30

    # Iterate over each page of search results
    for page in range(num_pages):
        # Calculate the start parameter for pagination
        start = page * 10

        # Send a request to Google and get the response
        url = f"https://www.google.com/search?q={query}&start={start}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
        }
        response = requests.get(url, headers=headers)

        # Parse the HTML content
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract search results
        search_results = []
        for result in soup.find_all("div", class_="g"):
            title = result.find("h3", class_="LC20lb DKV0Md").text if result.find("h3", class_="LC20lb DKV0Md") else None
            link = result.find("a")["href"] if result.find("a") else None
            description = result.find("span", class_="aCOpRe").text if result.find("span", class_="aCOpRe") else None
            search_results.append({"title": title, "link": link, "description": description})

        # Print search results for the current page
        print(f"Search results - Page {page + 1}:")
        for result in search_results:
            all_res.append(result["link"])
        
    return all_res

def how_to_get(par1:str, page:int):
    pass

class clone:
    def __init__():
        pass

    def __get__():
        def __init__():
            clone.__get__()
        
        def get_exp():
            di = json.loads(response.text)
            pos = response.meta['pos']
            dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            for result in di['organic_results']:
                title = result['title']
                snippet = result['snippet']
                link = result['link']
                item = {'title': title, 'snippet': snippet, 'link': link, 'position': pos, 'date': dt}
                pos += 1
                yield item
            next_page = di['pagination']['nextPageUrl']
            if next_page:
                yield scrapy.Request(get_url(next_page), callback=self.parse, meta={'pos': pos})