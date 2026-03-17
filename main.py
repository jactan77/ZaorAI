from news_scrapper import (
    NewsScrappper,
    NewScrapper,
    GoogleNewsScrapper,
    RssFeedScrapper,
    ExpertSiteScrapper,
    TwitterXScrapper,
    PdfReportScrapper,
)


def main():
    news_scrapper = RssFeedScrapper()
    news_scrapper.test()


if __name__ == '__main__':
    main()