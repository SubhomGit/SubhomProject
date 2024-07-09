import requests
from bs4 import BeautifulSoup

def crawl(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            page_content = response.text
            soup = BeautifulSoup(page_content, 'html.parser')
            return soup
        else:
            return None
    except requests.RequestException as e:
        print(f"Error crawling {url}: {e}")
        return None
