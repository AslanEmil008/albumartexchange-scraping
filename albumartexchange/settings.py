# #Custom Proxy Settings
# PROXY_HOST = "45.63.98.192"
# PROXY_PORT = "22226"
# PROXY = f"http://{PROXY_HOST}:{PROXY_PORT}"

# # Enable User-Agent spoofing
# USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

# # Set Up Proxy in Downloader Middleware
# DOWNLOADER_MIDDLEWARES = {
#     'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 1,
#     'albumartexchange.middlewares.ProxyMiddleware': 2,
# }

# # Increase concurrency settings for fast scraping
# CONCURRENT_REQUESTS = 200  # Increase this value to make more requests in parallel
# CONCURRENT_REQUESTS_PER_DOMAIN = 100  # Limit to 100 concurrent requests per domain
# CONCURRENT_REQUESTS_PER_IP = 100  # Limit to 100 concurrent requests per IP

# # Disable AutoThrottle for maximum speed (remove throttling)
# AUTOTHROTTLE_ENABLED = False  # Disable AutoThrottle
# DOWNLOAD_DELAY = 0  # Set to 0 to have no delay between requests (fastest)
# DOWNLOAD_TIMEOUT = 220  # Set a higher timeout for requests to avoid timing out

# # Set up the Image Pipeline to download images efficiently
# ITEM_PIPELINES = {
#     'scrapy.pipelines.images.ImagesPipeline': 1,
# }

# # Set the directory to save images
# IMAGES_STORE = 'downloaded_images3'

# # Enable image thumbnails (optional, for smaller images)
# IMAGES_THUMBS = {'small': (100, 100), 'big': (250, 250)}

# # Retry and user agent settings to handle blocks and retries
# RETRY_ENABLED = True
# RETRY_TIMES = 3  # Retry 3 times if a request fails
# USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"

# # Optionally, set up the proxy middleware (if needed for scraping)
# # HTTP_PROXY = 'http://your-proxy.com'
# DOWNLOADER_MIDDLEWARES = {
#    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 1,
# }
# SPIDER_MODULES = ['albumartexchange']





# # Custom Proxy Settings
# PROXY_HOST = "45.63.98.192"  # Replace with your actual proxy host
# PROXY_PORT = "22226"  # Replace with your actual proxy port
# PROXY = f"http://{PROXY_HOST}:{PROXY_PORT}"

# # Enable User-Agent spoofing
# USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

# # Set Up Proxy in Downloader Middleware
# DOWNLOADER_MIDDLEWARES = {
#     'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 1,  # Enables HTTP Proxy Middleware
#     'albumartexchange.middlewares.ProxyMiddleware': 2,  # Your custom proxy middleware
# }

# # Increase concurrency settings for fast scraping
# CONCURRENT_REQUESTS = 200  # Increase the number of concurrent requests
# CONCURRENT_REQUESTS_PER_DOMAIN = 100  # Limit concurrent requests per domain
# CONCURRENT_REQUESTS_PER_IP = 100  # Limit concurrent requests per IP

# # Disable AutoThrottle to maximize speed (optional for fast scraping)
# AUTOTHROTTLE_ENABLED = False  # Disable AutoThrottle for faster scraping
# DOWNLOAD_DELAY = 2  # No delay between requests
# DOWNLOAD_TIMEOUT = 220  # Timeout set higher to handle slow connections

# # Set up the Image Pipeline to download images efficiently
# ITEM_PIPELINES = {
#     'scrapy.pipelines.images.ImagesPipeline': 1,
# }

# # Set the directory to save images
# IMAGES_STORE = 'downloaded_images3(1)'

# # Enable image thumbnails (optional, for smaller images)
# IMAGES_THUMBS = {'small': (100, 100), 'big': (250, 250)}

# # Retry and user agent settings to handle blocks and retries
# RETRY_ENABLED = True  # Enable retries for failed requests
# RETRY_TIMES = 3  # Retry 3 times in case of failure

# # Optionally, set up the proxy middleware if needed
# HTTP_PROXY = f'http://{PROXY_HOST}:{PROXY_PORT}'  # Use the proxy in requests

# # Example of middlewares, customize it as per your need
# # DOWNLOADER_MIDDLEWARES = {
# #    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 1,
# #    'albumartexchange.middlewares.ProxyMiddleware': 2,
# # }
# SPIDER_MODULES = ['albumartexchange']


# 104.238.170.71:22226
# 104.238.170.71:22225
# 192.248.157.230:22223
# 192.248.157.230:22222


# Custom Proxy Settings
# PROXY_HOST = "45.63.98.192"
# PROXY_PORT = "22226"
# PROXY = f"http://{PROXY_HOST}:{PROXY_PORT}"

# # Enable User-Agent spoofing
# USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

# # Default request headers (Fixes 406 error)
# DEFAULT_REQUEST_HEADERS = {
#     "User-Agent": USER_AGENT,
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#     "Accept-Language": "en-US,en;q=0.5",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Referer": "https://albumartexchange.com",
# }

# # Proxy Middleware Setup
# DOWNLOADER_MIDDLEWARES = {
#     'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 1,
#     'albumartexchange.middlewares.ProxyMiddleware': 2,
#     'scrapy.downloadermiddlewares.retry.RetryMiddleware': 550,  # Ensure retries are handled properly
# }

# # High Concurrency for Fast Scraping
# CONCURRENT_REQUESTS = 200  
# CONCURRENT_REQUESTS_PER_DOMAIN = 100  
# CONCURRENT_REQUESTS_PER_IP = 100  

# # Reduce blocking risk (use random delays instead of fixed)
# AUTOTHROTTLE_ENABLED = False  
# DOWNLOAD_DELAY = 0.5  # Keep it low for speed, but not 0 to avoid bans
# RANDOMIZE_DOWNLOAD_DELAY = True  # Randomize delay to avoid pattern detection
# DOWNLOAD_TIMEOUT = 220  

# # Set up the Image Pipeline
# ITEM_PIPELINES = {
#     'scrapy.pipelines.images.ImagesPipeline': 1,
# }

# # Set the directory to save images
# IMAGES_STORE = 'downloaded_images3(t)'

# # Enable image thumbnails (optional)
# IMAGES_THUMBS = {'small': (100, 100), 'big': (250, 250)}

# # Retry settings (To recover from failures)
# RETRY_ENABLED = True
# RETRY_TIMES = 3  # Retry only twice to avoid wasting time

# # Spider settings
# SPIDER_MODULES = ['albumartexchange']



# # Custom Proxy Settings
# PROXIES = [
#     "http://45.63.98.192:22226",  # Proxy 1
#     "http:///192.248.168.217:22226",    # Proxy 2
#     "http:///192.248.168.217:22225",     # Proxy 3
# ]

# # Enable User-Agent spoofing
# USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

# # Default request headers (Fixes 406 error)
# DEFAULT_REQUEST_HEADERS = {
#     "User-Agent": USER_AGENT,
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#     "Accept-Language": "en-US,en;q=0.5",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Referer": "https://albumartexchange.com",
# }

# # Proxy Middleware Setup
# DOWNLOADER_MIDDLEWARES = {
#     'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 1,
#     'albumartexchange.middlewares.ProxyMiddleware': 2,
#     'scrapy.downloadermiddlewares.retry.RetryMiddleware': 550,  # Ensure retries are handled properly
# }

# # High Concurrency for Fast Scraping
# CONCURRENT_REQUESTS = 200  
# CONCURRENT_REQUESTS_PER_DOMAIN = 100  
# CONCURRENT_REQUESTS_PER_IP = 100  

# # Reduce blocking risk (use random delays instead of fixed)
# AUTOTHROTTLE_ENABLED = False  
# DOWNLOAD_DELAY = 0.5  # Keep it low for speed, but not 0 to avoid bans
# RANDOMIZE_DOWNLOAD_DELAY = True  # Randomize delay to avoid pattern detection
# DOWNLOAD_TIMEOUT = 220  

# # Set up the Image Pipeline
# ITEM_PIPELINES = {
#     'scrapy.pipelines.images.ImagesPipeline': 1,
# }

# # Set the directory to save images
# IMAGES_STORE = 'downloaded_images3'

# # Enable image thumbnails (optional)
# IMAGES_THUMBS = {'small': (100, 100), 'big': (250, 250)}

# # Retry settings (To recover from failures)
# RETRY_ENABLED = True
# RETRY_TIMES = 3  # Retry up to 3 times before switching proxies

# # Spider settings
#SPIDER_MODULES = ['albumartexchange']



# List of rotating proxies
# ROTATING_PROXY_LIST = [
    #er "http://78.141.247.188:22226",
    #er "http://78.141.247.188:22225",
    #er "http://95.179.206.200:22226",
#    er "http://95.179.206.200:22225",
#     "http://185.224.196.115:22225",
#     "http://192.248.157.230:22226",
#     "http://192.248.157.230:22225"
#     "http://185.150.196.156:22225",
#     "http://185.224.196.91:22225",

    
    
# ]

# # Enable User-Agent spoofing
# USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

# # Default request headers (Fixes 406 error)
# DEFAULT_REQUEST_HEADERS = {
#     "User-Agent": USER_AGENT,
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#     "Accept-Language": "en-US,en;q=0.5",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Referer": "https://albumartexchange.com",
# }

# # Enable Proxy Middleware (with rotation)
# DOWNLOADER_MIDDLEWARES = {
#     'scrapy.downloadermiddlewares.retry.RetryMiddleware': 550,  
#     'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
#     'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
#     'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 700,  
# }

# # High Concurrency for Fast Scraping (adjust if necessary)
# CONCURRENT_REQUESTS = 300  
# CONCURRENT_REQUESTS_PER_DOMAIN = 150  
# CONCURRENT_REQUESTS_PER_IP = 150

# # Reduce blocking risk (random delays)
# AUTOTHROTTLE_ENABLED = True  
# DOWNLOAD_DELAY = 0.5  
# RANDOMIZE_DOWNLOAD_DELAY = True  
# DOWNLOAD_TIMEOUT = 220  

# # Set up the Image Pipeline
# ITEM_PIPELINES = {
#     'scrapy.pipelines.images.ImagesPipeline': 1,
# }

# # Set the directory to save images
# IMAGES_STORE = 'downloaded_images3(te)'
# import random
# import logging

# class ProxyMiddleware:
#     def __init__(self, settings):
#         self.proxies = settings.getlist("ROTATING_PROXY_LIST", [])
#         self.request_count = 0
#         self.change_proxy_after = 200  # Change proxy every 5 requests

#         if not self.proxies:
#             logging.warning("ProxyMiddleware: No proxies found in ROTATING_PROXY_LIST!")

#     @classmethod
#     def from_crawler(cls, crawler):
#         return cls(crawler.settings)

#     def process_request(self, request, spider):
#         """Assign a new proxy to each request after N requests."""
#         if self.request_count % self.change_proxy_after == 0 or 'proxy' not in request.meta:
#             request.meta['proxy'] = random.choice(self.proxies)
#         self.request_count += 1

#     def process_response(self, request, response, spider):
#         """Handle blocked responses (403, 429) by switching proxies."""
#         if response.status in [403, 429]:
#             new_proxy = random.choice(self.proxies)
#             logging.warning(f"Proxy {request.meta['proxy']} blocked! Switching to {new_proxy}")
#             request.meta['proxy'] = new_proxy
#             return request  # Retry the request with a new proxy
#         return response

#     def process_exception(self, request, exception, spider):
#         """Handle connection failures by switching proxies."""
#         new_proxy = random.choice(self.proxies)
#         logging.warning(f"Request failed with {exception}. Switching to {new_proxy}")
#         request.meta['proxy'] = new_proxy
#         return request  # Retry the request with a new proxy


# # Enable image thumbnails (optional)
# IMAGES_THUMBS = {'small': (100, 100), 'big': (250, 250)}

# # Retry settings (recover from failures)
# RETRY_ENABLED = True
# RETRY_TIMES = 3  

# # SSL Certification Handling
# DOWNLOADER_CLIENT_TLS_METHOD = "TLSv1.2"  
# DOWNLOADER_CLIENT_TLS_VERIFY = False  
# SPIDER_MODULES = ['albumartexchange']






# # List of rotating proxies (Make sure they are working proxies)
# ROTATING_PROXY_LIST = [
#         "http": "http://ZhW8jx:fos5p3@177.234.140.25:8000",
        
        
# ]
        
      

# # User-Agent Spoofing
# USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

# # Default request headers (Fixes 406 error)
# DEFAULT_REQUEST_HEADERS = {
#     "User-Agent": USER_AGENT,
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#     "Accept-Language": "en-US,en;q=0.5",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Referer": "https://albumartexchange.com",
# }

# # Enable Proxy Middleware (Custom middleware added)
# DOWNLOADER_MIDDLEWARES = {
#     'scrapy.downloadermiddlewares.retry.RetryMiddleware': 550,
#     'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 600,
#     'albumartexchange.middlewares.ProxyMiddleware': 610,
# }

# # Adjust concurrency (lower it to avoid bans)
# CONCURRENT_REQUESTS = 200
# CONCURRENT_REQUESTS_PER_DOMAIN = 100
# CONCURRENT_REQUESTS_PER_IP = 100

# # Reduce blocking risk (random delays)
# AUTOTHROTTLE_ENABLED = True
# DOWNLOAD_DELAY = 1  # Slow down requests
# RANDOMIZE_DOWNLOAD_DELAY = True
# DOWNLOAD_TIMEOUT = 220

# # Set up the Image Pipeline
# ITEM_PIPELINES = {
#     'scrapy.pipelines.images.ImagesPipeline': 1,
# }

# # Directory to save images
# IMAGES_STORE = 'downloaded_images(test)'

# # Enable thumbnails (optional)
# IMAGES_THUMBS = {'small': (100, 100), 'big': (250, 250)}

# # Retry settings (Increase retry attempts)
# RETRY_ENABLED = True
# RETRY_TIMES = 3  # Retry 5 times before failing

# # SSL Handling
# DOWNLOADER_CLIENT_TLS_METHOD = "TLSv1.2"
# DOWNLOADER_CLIENT_TLS_VERIFY = False

# SPIDER_MODULES = ['albumartexchange']



# Set the proxy URL (Correct proxy format)

# ROTATING_PROXY_LIST = [
#     "http://ZhW8jx:fos5p3@177.234.140.25:8000",  # Your proxy URL
# ]

# # User-Agent Spoofing
# USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

# # Default request headers (Fixes 406 error)
# DEFAULT_REQUEST_HEADERS = {
#     "User-Agent": USER_AGENT,
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#     "Accept-Language": "en-US,en;q=0.5",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Referer": "https://albumartexchange.com",
# }

# # Enable Proxy Middleware (Custom middleware added)
# DOWNLOADER_MIDDLEWARES = {
#     'scrapy.downloadermiddlewares.retry.RetryMiddleware': 550,  # Retry middleware
#     'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 600,  # Proxy middleware
#     'albumartexchange.middlewares.ProxyMiddleware': 610,  # Make sure this middleware is implemented correctly
# }

# # Define Proxy Authentication in settings
# HTTP_PROXY_AUTH = 'ZhW8jx:fos5p3'  # Authentication in 'username:password' format

# # Adjust concurrency (lower it to avoid bans)
# CONCURRENT_REQUESTS = 300
# CONCURRENT_REQUESTS_PER_DOMAIN = 150
# CONCURRENT_REQUESTS_PER_IP = 150

# # Reduce blocking risk (random delays)
# AUTOTHROTTLE_ENABLED = True
# DOWNLOAD_DELAY = 0.2  # Slow down requests
# RANDOMIZE_DOWNLOAD_DELAY = True
# DOWNLOAD_TIMEOUT = 220

# # Set up the Image Pipeline
# ITEM_PIPELINES = {
#     'scrapy.pipelines.images.ImagesPipeline': 1,
# }

# # Directory to save images
# IMAGES_STORE = 'downloaded_images(test)'

# # Enable thumbnails (optional)
# IMAGES_THUMBS = {'small': (100, 100), 'big': (250, 250)}

# # Retry settings (Increase retry attempts)
# RETRY_ENABLED = True
# RETRY_TIMES = 5  # Retry 5 times before failing (you can adjust this)
# RETRY_HTTP_CODES = [403, 429, 500, 502, 503, 504]  # Common retryable errors

# # SSL Handling (if needed)
# DOWNLOADER_CLIENT_TLS_METHOD = "TLSv1.2"
# DOWNLOADER_CLIENT_TLS_VERIFY = False

# # Set Spider Modules
# SPIDER_MODULES = ['albumartexchange']




# # Custom Proxy Settings
# PROXY_HOST = "177.234.140.25"
# PROXY_PORT = "8000"
# PROXY_USER = "ZhW8jx"
# PROXY_PASS = "fos5p3"
# PROXY = f"http://{PROXY_USER}:{PROXY_PASS}@{PROXY_HOST}:{PROXY_PORT}"

# # Enable User-Agent spoofing
# USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

# # Set Up Proxy in Downloader Middleware
# DOWNLOADER_MIDDLEWARES = {
#     'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 1,
#     'albumartexchange.middlewares.ProxyMiddleware': 2,
# }

# # Increase concurrency settings for fast scraping
# CONCURRENT_REQUESTS = 300  # Increase this value to make more requests in parallel
# CONCURRENT_REQUESTS_PER_DOMAIN = 150  # Limit to 100 concurrent requests per domain
# CONCURRENT_REQUESTS_PER_IP = 150  # Limit to 100 concurrent requests per IP

# # Disable AutoThrottle for maximum speed (remove throttling)
# AUTOTHROTTLE_ENABLED = False  # Disable AutoThrottle
# DOWNLOAD_DELAY = 0  # Set to 0 to have no delay between requests (fastest)
# DOWNLOAD_TIMEOUT = 220  # Set a higher timeout for requests to avoid timing out

# # Set up the Image Pipeline to download images efficiently
# ITEM_PIPELINES = {
#     'scrapy.pipelines.images.ImagesPipeline': 1,
# }

# # Set the directory to save images
# IMAGES_STORE = 'downloaded_images5'

# # Enable image thumbnails (optional, for smaller images)
# IMAGES_THUMBS = {'small': (100, 100), 'big': (250, 250)}

# # Retry and user agent settings to handle blocks and retries
# RETRY_ENABLED = True
# RETRY_TIMES = 2  # Retry 3 times if a request fails
# USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"

# # Optionally, set up the proxy middleware (if needed for scraping)
# SPIDER_MODULES = ['albumartexchange']



















# Custom Proxy Settings
# PROXY_HOST = "177.234.140.25"
# PROXY_PORT = "8000"
# PROXY_USER = "ZhW8jx"
# PROXY_PASS = "fos5p3"

# # Enable User-Agent spoofing
# USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

# # Set Up Proxy in Downloader Middleware
# DOWNLOADER_MIDDLEWARES = {
#     'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 1,
#     'albumartexchange.middlewares.ProxyMiddleware': 2,
# }

# # Increase concurrency settings for fast scraping
# CONCURRENT_REQUESTS = 200  # Increase this value to make more requests in parallel
# CONCURRENT_REQUESTS_PER_DOMAIN = 100  # Limit to 100 concurrent requests per domain
# CONCURRENT_REQUESTS_PER_IP = 100  # Limit to 100 concurrent requests per IP

# # Disable AutoThrottle for maximum speed (remove throttling)
# AUTOTHROTTLE_ENABLED = False  # Disable AutoThrottle
# DOWNLOAD_DELAY = 0 # Set to 0 to have no delay between requests (fastest)
# DOWNLOAD_TIMEOUT = 180  # Set a higher timeout for requests to avoid timing out

# # Set up the Image Pipeline to download images efficiently
# ITEM_PIPELINES = {
#     'scrapy.pipelines.images.ImagesPipeline': 1,
# }

# # Set the directory to save images
# IMAGES_STORE = 'downloaded_images6'

# # Enable image thumbnails (optional, for smaller images)
# IMAGES_THUMBS = {'small': (100, 100), 'big': (250, 250)}

# # Retry and user agent settings to handle blocks and retries
# RETRY_ENABLED = True
# RETRY_TIMES = 2  # Retry 3 times if a request fails
# USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"

# # Set Spider Modules
# SPIDER_MODULES = ['albumartexchange']


















# Custom Proxy Settings
# PROXY_HOST = "177.234.140.25"
# PROXY_PORT = "8000"
# PROXY_USER = "ZhW8jx"
# PROXY_PASS = "fos5p3"
# settings.py


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
PROXY = 'http://177.234.140.25:8000'  # Replace with your actual proxy URL
PROXY_USER_PASS = 'ZhW8jx:fos5p3'    # Replace with your actual proxy username and password



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
