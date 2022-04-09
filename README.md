# Using Selenium with Scrapy

This is a demonstration of how selenium can be used with scrapy.

See the video for demonstration - https://youtu.be/2LwrUu9yTAo

### prepare env
```bash
$ pip3 install -r requirements.txt 
```

# run scrapy
```bash
$ scrapy crawl lazada_sel -O sel_scrapy/output/lazada_sel.json
$ scrapy crawl lazada_sp_manual -O sel_scrapy/output/lazada_sp_manual.json
$ scrapy crawl lazada_splash -O sel_scrapy/output/lazada_splash.json
```