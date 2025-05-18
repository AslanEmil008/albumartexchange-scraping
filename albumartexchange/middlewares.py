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
