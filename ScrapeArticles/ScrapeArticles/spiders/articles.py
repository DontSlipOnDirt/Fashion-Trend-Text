import scrapy

class ArtcleSpider(scrapy.Spider):
    name = "articles"
    
    start_urls = [
        # "https://www.vogue.com/article",
        # "https://www.teenvogue.com/story",
        # "https://www.elle.com/fashion/trend-reports/"
        # "https://fashionmagazine.com/style",
        # "https://www.cosmopolitan.com/style-beauty/fashion",
        # "https://www.wmagazine.com/fashion/",
        "https://fashionunited.com/news/fashion"
        # "https://www.seventeen.com/fashion/trends"
    ]

    def parse(self, response):
        # Extract article links
        article_links = response.css("div.MuiGrid-root.MuiGrid-container.MuiGrid-item.MuiGrid-spacing-xs-4.MuiGrid-grid-xs-12.e10gwzwj0.css-63g34r a::attr(href)").getall()
        for link in article_links:
            yield response.follow(link, callback=self.parse_article)

    def parse_article(self, response):
        # Extract article content
        article_title = response.css("h1::text").get()
        article_content = response.css("p::text").getall()

        yield {
            "title": article_title,
            "content": article_content
        }

# Run the spider
# scrapy runspider articles.py -o articles.json