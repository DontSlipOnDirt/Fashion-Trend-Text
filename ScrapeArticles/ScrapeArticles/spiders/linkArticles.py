import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class VogueArticlesSpider(CrawlSpider):
    name = "vogueArticles"
    allowed_domains = ["www.vogue.com"]
    start_urls = ["https://www.vogue.com/fashion/trends"]

    rules = (
        Rule(LinkExtractor(allow="article"), callback="parse_article", follow=True),
    )
    
    def parse_article(self, response):
        # Extract article content
        article_title = response.css("h1::text").get()
        article_date = response.css("time::attr(datetime)").get()
        article_content = response.css("p::text").getall() + response.css("p a::text").getall()

        yield {
            "title": article_title,
            "date": article_date,
            "content": article_content,
        }

# scrapy crawl vogueArticles -O vogueArticles.json

class ElleArticlesSpider(CrawlSpider):
    name = "elleArticles"
    allowed_domains = ["www.elle.com"]
    start_urls = ["https://www.elle.com/fashion/"]

    rules = (
        Rule(LinkExtractor(allow=r"trend-reports/"), callback="parse_article", follow=True),
    )
    
    def parse_article(self, response):
        # Extract article content
        article_title = response.css("h1::text").get()
        article_date = response.css("time::text").get()
        article_content = response.css("p::text").getall() + response.css("p a::text").getall()

        yield {
            "title": article_title,
            "date": article_date,
            "content": article_content,
        }

# scrapy crawl elleArticles -O elleArticles.json

class wmagazineArticlesSpider(CrawlSpider):
    name = "wmagazineArticles"
    allowed_domains = ["www.wmagazine.com"]
    start_urls = ["https://www.wmagazine.com/fashion/"]

    rules = (
        Rule(LinkExtractor(allow="fashion/"), callback="parse_article", follow=True),
    )
    
    def parse_article(self, response):
        # Extract article content
        article_title = response.css("h1::text").get()
        article_date = response.css("time::attr(datetime)").get()
        article_content = response.css("p::text").getall() + response.css("p a::text").getall()

        yield {
            "title": article_title,
            "date": article_date,
            "content": article_content,
        }

# scrapy crawl wmagazineArticles -O wmagazineArticles.json

class CosmopolitanArticlesSpider(CrawlSpider):
    name = "cosmopolitanArticles"
    allowed_domains = ["www.cosmopolitan.com"]
    start_urls = ["https://www.cosmopolitan.com/style-beauty/fashion/"]

    rules = (
        Rule(LinkExtractor(allow="fashion/"), callback="parse_article", follow=True),
    )
    
    def parse_article(self, response):
        # Extract article content
        article_title = response.css("h1::text").get()
        article_date = response.css("time::text").get()
        article_content = response.css("p::text").getall() + response.css("p a::text").getall()

        yield {
            "title": article_title,
            "date": article_date,
            "content": article_content,
        }

# scrapy crawl cosmopolitanArticles -O ../data/cosmopolitanArticles.json

class SeventeenArticlesSpider(CrawlSpider):
    name = "seventeenArticles"
    allowed_domains = ["www.seventeen.com"]
    start_urls = ["https://www.seventeen.com/fashion/trends/"]

    rules = (
        Rule(LinkExtractor(allow="fashion/trends"), callback="parse_article", follow=True),
    )
    
    def parse_article(self, response):
        # Extract article content
        article_title = response.css("h1::text").get()
        article_date = response.css("time::text").get()
        article_content = response.css("p::text").getall() + response.css("p a::text").getall()

        yield {
            "title": article_title,
            "date": article_date,
            "content": article_content,
        }

# scrapy crawl seventeenArticles -O ../data/seventeenArticles.json

class FashionmagazineArticlesSpider(CrawlSpider):
    name = "fashionmagazineArticles"
    allowed_domains = ["fashionmagazine.com"]
    start_urls = ["https://fashionmagazine.com/category/style/trends/"]

    rules = (
        Rule(LinkExtractor(allow="style/"), callback="parse_article", follow=True),
    )
    
    def parse_article(self, response):
        # Extract article content
        article_title = response.css("h1::text").get()
        article_date = response.css("p.article-byline__date::text").get()
        article_content = response.css("p::text").getall() + response.css("h2::text").getall()

        yield {
            "title": article_title,
            "date": article_date,
            "content": article_content,
        }

# scrapy crawl fashionmagazineArticles -O ../data/fashionmagazineArticles.json

class HarperbazaarArticlesSpider(CrawlSpider):
    name = "harperbazaarArticles"
    allowed_domains = ["www.harpersbazaar.com"]
    start_urls = ["https://www.harpersbazaar.com/fashion/"]

    rules = (
        Rule(LinkExtractor(allow="fashion/trends/"), callback="parse_article", follow=True),
    )
    
    def parse_article(self, response):
        # Extract article content
        article_title = response.css("h1::text").get()
        article_date = response.css("time::text").get()
        article_content = response.css("p::text").getall() + response.css("p a::text").getall()

        yield {
            "title": article_title,
            "date": article_date,
            "content": article_content,
        }

# scrapy crawl harperbazaarArticles -O ../data/harperbazaarArticles.json

# !bad, many unrelated links

class TeenvogueArticlesSpider(CrawlSpider):
    name = "teenvogueArticles"
    allowed_domains = ["www.teenvogue.com"]
    start_urls = ["https://www.teenvogue.com/fashion/trends"]

    rules = (
        Rule(LinkExtractor(allow="story"), callback="parse_article", follow=True),
    )
    
    def parse_article(self, response):
        # Extract article content
        article_title = response.css("h1::text").get()
        article_date = response.css("time::attr(datetime)").get()
        article_content = response.css("p::text").getall() + response.css("p a::text").getall()

        yield {
            "title": article_title,
            "date": article_date,
            "content": article_content,
        }

# scrapy crawl teenvogueArticles -O ../data/teenvogueArticles.json

# !not working, no date
class FashionunitedArticlesSpider(CrawlSpider):
    name = "fashionunitedArticles"
    allowed_domains = ["fashionunited.com"]
    start_urls = ["https://fashionunited.com/trends/"]

    rules = (
        Rule(LinkExtractor(allow=r"news/fashion/"), callback="parse_article", follow=True),
    )
    
    def parse_article(self, response):
        # Extract article content
        article_title = response.css("h1::text").get()
        article_date = response.css("span::text").get()
        article_content = response.css("p::text").getall() + response.css("h3::text").getall()

        yield {
            "title": article_title,
            "content": article_content,
        }

# scrapy crawl fashionunitedArticles -O ../data/fashionunitedArticles.json
