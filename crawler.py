import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def is_valid(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def get_all_links(soup, base_url):
    links = set()
    for a_tag in soup.find_all("a"):
        href = a_tag.attrs.get("href")
        if href == "" or href is None:
            continue
        href = urljoin(base_url, href)
        href_parsed = urlparse(href)
        href = href_parsed.scheme + "://" + href_parsed.netloc + href_parsed.path
        if is_valid(href):
            links.add(href)
    return links

def crawl(url, max_pages=10):
    visited = set()
    to_visit = [url]
    pages_crawled = 0

    while to_visit and pages_crawled < max_pages:
        current_url = to_visit.pop(0)
        if current_url in visited:
            continue

        try:
            response = requests.get(current_url)
            if response.status_code == 200:
                page_content = response.text
                soup = BeautifulSoup(page_content, 'html.parser')
                visited.add(current_url)
                to_visit.extend(get_all_links(soup, current_url))
                pages_crawled += 1
                print(f"Crawled: {current_url}")
        except requests.RequestException as e:
            print(f"Error crawling {current_url}: {e}")

    return visited
