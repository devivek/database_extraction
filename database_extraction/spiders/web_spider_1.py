import scrapy
class ExtractUrls(scrapy.Spider):
    name = "extract" #name of our crawler
  
    # request function
    def start_requests(self):
        urls = [ "https://www.studyadda.com/question-bank/jee-main-advanced/chemistry/some-basic-concepts-of-chemistry-%E0%A4%B0%E0%A4%B8%E0%A4%AF%E0%A4%A8-%E0%A4%95-%E0%A4%95%E0%A4%9B-%E0%A4%AE%E0%A4%B2%E0%A4%AD%E0%A4%A4-%E0%A4%85%E0%A4%B5%E0%A4%A7%E0%A4%B0%E0%A4%A3%E0%A4%8F/topic-test-some-basic-concepts-of-chemistry-8-5-21/5959569", ]
          
        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse)
  
    # Parse function
    def parse(self, response):
          
        for elements in  response.css('li.element-item.singlechoice'):
            yield {
                'question' : elements.get(),
            }