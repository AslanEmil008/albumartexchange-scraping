# # middlewares.py
# from scrapy import signals

# class ProxyMiddleware:
#     def process_request(self, request, spider):
#         # Set the proxy for each request
#         request.meta['proxy'] = spider.settings.get('PROXY')


# middlewares.py


#104.238.170.71:22226
# 104.238.170.71:22225
# 192.248.157.230:22223
# 192.248.157.230:22222
        

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




# import random
# import logging
# import base64

# class ProxyMiddleware:
#     def __init__(self, settings):
#         self.proxies = settings.getlist("ROTATING_PROXY_LIST", [])
#         self.request_count = 0
#         self.change_proxy_after = 200  # Change proxy every 200 requests

#         if not self.proxies:
#             logging.warning("ProxyMiddleware: No proxies found in ROTATING_PROXY_LIST!")

#     @classmethod
#     def from_crawler(cls, crawler):
#         return cls(crawler.settings)

#     def process_request(self, request, spider):
#         """Assign a new proxy to each request after N requests."""
#         # Use only the first proxy in the list
#         if self.request_count % self.change_proxy_after == 0 or 'proxy' not in request.meta:
#             request.meta['proxy'] = self.proxies[0]  # Use only the first (and in your case, only) proxy
#             # Set the Proxy Authentication header
#             proxy = request.meta['proxy']
#             if 'http' in proxy:
#                 proxy_user_pass = proxy.split('@')[0].replace('http://', '')
#                 request.headers['Proxy-Authorization'] = 'Basic ' + base64.b64encode(proxy_user_pass.encode()).decode()
#         self.request_count += 1

#     def process_response(self, request, response, spider):
#         """Handle blocked responses (403, 429) by switching proxies."""
#         if response.status in [403, 429]:
#             logging.warning(f"Proxy {request.meta['proxy']} blocked! Retrying with the same proxy.")
#             return request  # Retry the request with the same proxy (since you are using one)
#         return response

#     def process_exception(self, request, exception, spider):
#         """Handle connection failures by switching proxies."""
#         logging.warning(f"Request failed with {exception}. Retrying with the same proxy.")
#         return request  # Retry the request with the same proxy

# middlewares.py
# from scrapy import signals
# import base64

# class ProxyMiddleware:
#     def process_request(self, request, spider):
#         # Set the proxy for each request
#         proxy = spider.settings.get('PROXY')
#         request.meta['proxy'] = proxy
        
#         # Add authentication headers for the proxy
#         if proxy:
#             request.headers['Proxy-Authorization'] = 'Basic ' + base64.b64encode(f"{spider.settings.get('PROXY_USER')}:{spider.settings.get('PROXY_PASS')}".encode('utf-8')).decode('utf-8')




























# # middlewares.py
# import base64

# class ProxyMiddleware:
#     def process_request(self, request, spider):
#         proxy = "http://177.234.140.25:8000"  # Replace with your proxy IP and port
#         username = "ZhW8jx"  # Replace with your username
#         password = "fos5p3"  # Replace with your password

#         # Encode the credentials
#         creds = f"{username}:{password}"
#         encoded_creds = base64.b64encode(creds.encode()).decode()

#         # Set proxy
#         request.meta['proxy'] = proxy

#         # Set authentication header
#         request.headers['Proxy-Authorization'] = f'Basic {encoded_creds}'














import base64

class ProxyMiddleware:
    def __init__(self, proxy, proxy_user_pass):
        self.proxy = proxy
        self.proxy_user_pass = proxy_user_pass

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        # Get the proxy and credentials from settings
        proxy = crawler.settings.get('PROXY')
        proxy_user_pass = crawler.settings.get('PROXY_USER_PASS')
        return cls(proxy, proxy_user_pass)

    def process_request(self, request, spider):
        # Set the proxy for the request
        request.meta['proxy'] = self.proxy
        # Add proxy authentication if needed
        encoded_credentials = base64.b64encode(self.proxy_user_pass.encode()).decode()
        request.headers['Proxy-Authorization'] = f'Basic {encoded_credentials}'
