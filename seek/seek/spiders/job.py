import scrapy


class JobSpider(scrapy.Spider):
    name = 'job'
    allowed_domains = ['www.seek.com.au']

    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"

    def start_requests(self):
        yield scrapy.Request(
            url='http://www.seek.com.au/jobs/',
            callback=self.parse,
            headers={'User-Agent': self.user_agent}
        )

    def parse(self, response):
        for job in response.xpath("(//div[@data-automation='searchResults']/div/div)[2]/div[position() > 1]"):
            location = job.xpath(".//a[@data-automation='jobLocation']/text()").get()
            area = job.xpath(".//a[@data-automation='jobArea']/text()").get()
            if area:
                location = location + " - " + area
            yield {
                'title': job.xpath(".//a[@data-automation='jobTitle']/text()").get(),
                'company': job.xpath(".//a[@data-automation='jobCompany']/text()").get(),
                'description': job.xpath(".//span[@data-automation='jobShortDescription']/span/text()").get(),
                'location': location,
                'pay': job.xpath(".//span[@data-automation='jobSalary']/span/text()").get(),
                'job_type': job.xpath(".//a[@data-automation='jobSubClassification']/text()").get(),
                'job_category': job.xpath(".//a[@data-automation='jobClassification']/text()").get(),
            }

        next_page = response.xpath("//a[@data-automation='page-next']/@href").get()
        if next_page:
            yield scrapy.Request(
                url=response.urljoin(next_page),
                callback=self.parse,
                headers={'User-Agent': self.user_agent}
            )
