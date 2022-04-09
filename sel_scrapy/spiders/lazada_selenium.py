import scrapy
from selenium import webdriver
from sel_scrapy.items import LaptopItem
from webdriver_manager.chrome import ChromeDriverManager


class LazadaSeleniumSpider(scrapy.Spider):
    name = 'lazada_sel'

    def start_requests(self):
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(
            ChromeDriverManager().install(), options=options
        )
        driver.get('https://www.lazada.com.ph/shop-laptops/')
        link_elements = driver.find_elements_by_xpath(
            '//*[@data-qa-locator="product-item"]//a[text()]'
        )

        for link in link_elements:
            yield scrapy.Request(link.get_attribute('href'), callback=self.parse)

        driver.quit()

    def parse(self, response, **kwargs):
        item = LaptopItem(
            name=response.css(
                '.breadcrumb_item_anchor.breadcrumb_item_anchor_last ::text').get(),
            price=response.css('.pdp-price ::text').get()
        )

        yield item
