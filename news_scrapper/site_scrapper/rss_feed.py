import json
import requests

SITES_PATH = "news_scrapper/site_scrapper/sites.json"
OPEN_SITES_PATH = "news_scrapper/site_scrapper/open_sites.txt"


class RssFeedScrapper:
    SITES = json.load(open(SITES_PATH, "r"))
    session = requests.Session()

    def __init__(self):
        pass

    def test(self):
        open_sites = ""
        with open(OPEN_SITES_PATH, "w") as w:
            w.write("")
            w.close()
        
        for name, url in self.SITES["sites"].items():
            try:
                response = self.session.get(url, timeout=10)
                if response.status_code == 200:
                    open_sites +=  f"Successfully accessed {name} at {url}\n"
                    print(f"Successfully accessed {name} at {url}")
                else:
                    open_sites += f"Failed to access {name} at {url} with status code {response.status_code}\n"
            except requests.RequestException:
                pass

        with open(OPEN_SITES_PATH, "w") as f:
            f.write(open_sites)