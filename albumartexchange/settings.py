# settings.py

# Set higher concurrency for faster scraping
# Scrapy settings for albumartexchange project
# Scrapy settings for your project

# Set the User-Agent to mimic a real browser (can be random or fixed)
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'

# Enable or disable downloader middlewares
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 1,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 2,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': 3,
    'albumartexchange.middlewares.ProxyMiddleware': 400,  # Custom ProxyMiddleware
}
# Proxy and authentication credentials
PROXY = 'http://your_proxy_address:proxy_port'  # Replace with your actual proxy URL
PROXY_USER_PASS = 'username:password'    # Replace with your actual proxy username and password


# Set the number of concurrent requests
CONCURRENT_REQUESTS = 128  # Adjust based on proxy/server performance

# Reduce delay to speed up scraping (Be careful with rate-limiting)
DOWNLOAD_DELAY = 0.1  # Time to wait between requests (low value for faster scraping)

# Enable AutoThrottle to adjust the request rate based on server response
AUTOTHROTTLE_ENABLED = True #kargavoruma requestenry avtomat kerpov
AUTOTHROTTLE_START_DELAY = 0.1  # Minimum delay between requests
AUTOTHROTTLE_MAX_DELAY = 1  # Maximum delay between requests
AUTOTHROTTLE_TARGET_CONCURRENCY = 2.0  # Set to 2 requests per second on average
#mijinum miajamanak 2 hat requesta uxarkum
# Retry failed requests
RETRY_TIMES = 3  # Number of retries for failed requests
RETRY_HTTP_CODES = [500, 502, 503, 504, 408]  # Retry on these HTTP codes

# Set the maximum timeout for requests (increase if needed)
DOWNLOAD_TIMEOUT = 30  # Time to wait before timing out

# Logging settings to monitor the scraping process
LOG_LEVEL = 'DEBUG'  # Adjust log level to capture debugging information

# If you want to save the scraped data, configure pipelines for exporting:
FEED_FORMAT = 'json'
FEED_URI = 'output.json'

# Disable cookies if the website doesn't require them
COOKIES_ENABLED = False

# Set the spider modules (if needed for your project)
SPIDER_MODULES = ['albumartexchange']
