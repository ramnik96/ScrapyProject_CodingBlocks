import scrapy

class MySpider(scrapy.Spider):
	name="flipkart_spider"
	
	def start_requests(self):
	
		urls = [
		"https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy%2C4io&marketplace=FLIPKART&otracker=product_breadCrumbs_Mi+Mobiles&page=1",
		]
		for url in urls:
			yield scrapy.Request(url=url,callback=self.parse)
			
	def parse(self,response):
		page_id = response.url.split('=')[-1]
		page_id=int(page_id)+1;
		
		mobiles = response.css("div._1UoZlX")
		nextpage="https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy%2C4io&marketplace=FLIPKART&otracker=product_breadCrumbs_Mi+Mobiles&page="+str(page_id)
		next_page =response.urljoin(nextpage)
		
		for mobile in mobiles:
			name=mobile.css("div._3wU53n::text").get()
			price=mobile.css("div._1vC4OE._2rQ-NK::text").get()
			rating=mobile.css("div.hGSR34::text").get()
			
			
			yield {
			"name":name,
			"price":price,
			"rating":rating,
			}
			
			
			
			if page_id < 6: yield scrapy.Request(next_page,callback=self.parse)
				
			


			
				