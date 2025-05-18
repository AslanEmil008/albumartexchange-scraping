# import scrapy
# import random
# import time
# from scrapy.http import HtmlResponse
# from bs4 import BeautifulSoup
# import aiofiles
# import os
# import ssl

# ssl._create_default_https_context = ssl._create_unverified_context


# class AlbumSpider(scrapy.Spider):
#     name = "albumartexchange"
    
    
#     # Start URL for scraping specific pages (1250 to 1260)
#     start_urls = [f'https://albumartexchange.com/covers?page={i}' for i in range(19954,29954)]
    
#     # Create a directory to save images if it doesn't exist
#     if not os.path.exists('downloaded_images3(1)'):
#         os.makedirs('downloaded_images3(1)')
    
#     # Prepare CSV file for saving image data
#     csv_file = 'image_details3(1).csv'
#     csv_headers = ['Image URL', 'Resolution', 'File Size', 'Cover URL', 'Image Name']
    
#     # Write CSV header
#     def write_csv(self, headers):
#         with open(self.csv_file, mode='w', newline='', encoding='utf-8') as file:
#             file.write(','.join(headers) + '\n')
    
#     def __init__(self, *args, **kwargs):
#         super(AlbumSpider, self).__init__(*args, **kwargs)
#         self.write_csv(self.csv_headers)  # Write headers to CSV at the start
    
#     # Scrape images and details from the page
#     def parse(self, response):
#         page_number = int(response.url.split('=')[-1])  # Extract the page number from URL
        
#         # Calculate img_counter based on the page number (page 1250 => 10001, page 1251 => 10009, etc.)
#         img_counter = (page_number) * 8 + 1  # Adjust based on 8 images per page
        
#         # Get the cover URL (the current page URL)
#         cover_url = response.url
        
#         soup = BeautifulSoup(response.body, 'html.parser')
#         img_boxes = soup.find_all('div', class_='img-box')
        
#         for img_box in img_boxes:
#             style = img_box.get('style', '')
#             if 'background-image' in style:
#                 img_url = style.split('url(')[1].split(')')[0].strip('"\'')
#                 full_img_url = 'https://www.albumartexchange.com' + img_url

#                 # Extract image dimensions and file size
#                 image_info = img_box.find_next('p', class_='image-info')
#                 if image_info:
#                     dimensions = image_info.find('span', class_='dimensions')
#                     file_size = image_info.find('span', class_='file-size')

#                     if dimensions and file_size:
#                         image_dimensions = dimensions.get_text(strip=True)
#                         image_file_size = file_size.get_text(strip=True)

#                         # Find the correct cover URL from the <a> tag with class 'view-details-link'
#                         detail_link = img_box.find('a', class_='view-details-link')
#                         if detail_link:
#                             # Construct the cover URL using the href from the link
#                             detail_url = detail_link.get('href', '')
#                             cover_url = 'https://albumartexchange.com' + detail_url

#                         # Save image details to CSV
#                         self.save_to_csv(full_img_url, image_dimensions, image_file_size, cover_url, img_counter)
                
#                 # Download the image (Scrapy handles download automatically)
#                 yield scrapy.Request(full_img_url, callback=self.download_image, meta={'img_counter': img_counter})
                
#                 img_counter += 1  # Increment the counter for each image on the current page
    
#     # Save image details to CSV
#     def save_to_csv(self, img_url, dimensions, file_size, cover_url, img_counter):
#         img_name = f"{img_counter:08d}.png"  # Format the image name with leading zeros
#         with open(self.csv_file, mode='a', newline='', encoding='utf-8') as file:
#             file.write(f"{img_url},{dimensions},{file_size},{cover_url},{img_name}\n")
    
#     # Download image using Scrapy's built-in `FilesPipeline`
#     def download_image(self, response):
#         img_counter = response.meta['img_counter']
#         img_name = f"{img_counter:08d}.png"
#         img_path = os.path.join('downloaded_images3(1)', img_name)
        
#         with open(img_path, 'wb') as img_file:
#             img_file.write(response.body)





# import scrapy
# import random
# import time
# from scrapy.http import HtmlResponse
# from bs4 import BeautifulSoup
# import aiofiles
# import os

# class AlbumSpider(scrapy.Spider):
#     name = "albumartexchange"
    
#     # Start URL for scraping specific pages (1250 to 1260)
#     start_urls = [f'https://albumartexchange.com/covers?page={i}' for i in range(31287,32537)] #40581
    
#     # Create a directory to save images if it doesn't exist
#     if not os.path.exists('downloaded_images6'):
#         os.makedirs('downloaded_images6')
    
#     # Prepare CSV file for saving image data
#     csv_file = 'image_details6.csv'
#     csv_headers = ['Image URL', 'Resolution', 'File Size', 'Cover URL', 'Image Name']
    
#     # Write CSV header
#     def write_csv(self, headers):
#         with open(self.csv_file, mode='w', newline='', encoding='utf-8') as file:
#             file.write(','.join(headers) + '\n')
    
#     def __init__(self, *args, **kwargs):
#         super(AlbumSpider, self).__init__(*args, **kwargs)
#         self.write_csv(self.csv_headers)  # Write headers to CSV at the start
    
#     # Scrape images and details from the page
#     def parse(self, response):
#         page_number = int(response.url.split('=')[-1])  # Extract the page number from URL
        
#         # Calculate img_counter based on the page number (page 1250 => 10001, page 1251 => 10009, etc.)
#         img_counter = (page_number) * 8 + 1  # Adjust based on 8 images per page
        
#         # Get the cover URL (the current page URL)
#         cover_url = response.url
        
#         soup = BeautifulSoup(response.body, 'html.parser')
#         img_boxes = soup.find_all('div', class_='img-box')
        
#         for img_box in img_boxes:
#             style = img_box.get('style', '')
#             if 'background-image' in style:
#                 img_url = style.split('url(')[1].split(')')[0].strip('"\'')
#                 full_img_url = 'https://www.albumartexchange.com' + img_url

#                 # Extract image dimensions and file size
#                 image_info = img_box.find_next('p', class_='image-info')
#                 if image_info:
#                     dimensions = image_info.find('span', class_='dimensions')
#                     file_size = image_info.find('span', class_='file-size')

#                     if dimensions and file_size:
#                         image_dimensions = dimensions.get_text(strip=True)
#                         image_file_size = file_size.get_text(strip=True)

#                         # Find the correct cover URL from the <a> tag with class 'view-details-link'
#                         detail_link = img_box.find('a', class_='view-details-link')
#                         if detail_link:
#                             # Construct the cover URL using the href from the link
#                             detail_url = detail_link.get('href', '')
#                             cover_url = 'https://albumartexchange.com' + detail_url

#                         # Save image details to CSV
#                         self.save_to_csv(full_img_url, image_dimensions, image_file_size, cover_url, img_counter)
                
#                 # Download the image (Scrapy handles download automatically)
#                 yield scrapy.Request(full_img_url, callback=self.download_image, meta={'img_counter': img_counter})
                
#                 img_counter += 1  # Increment the counter for each image on the current page
    
#     # Save image details to CSV
#     def save_to_csv(self, img_url, dimensions, file_size, cover_url, img_counter):
#         img_name = f"{img_counter:08d}.png"  # Format the image name with leading zeros
#         with open(self.csv_file, mode='a', newline='', encoding='utf-8') as file:
#             file.write(f"{img_url},{dimensions},{file_size},{cover_url},{img_name}\n")
    
#     # Download image using Scrapy's built-in FilesPipeline
#     def download_image(self, response):
#         img_counter = response.meta['img_counter']
#         img_name = f"{img_counter:08d}.png"
#         img_path = os.path.join('downloaded_images6', img_name)
        
#         with open(img_path, 'wb') as img_file:
#             img_file.write(response.body)
#^^^^^^^^^^^^^^^^^






import scrapy
import os
from scrapy.http import HtmlResponse
from bs4 import BeautifulSoup
import aiofiles

class AlbumSpider(scrapy.Spider):
    name = "albumartexchange"
    
    # Start URL for scraping specific pages (1250 to 1260)
    start_urls = [f'https://albumartexchange.com/covers?page={i}' for i in range(1, 101)] 
    
    if not os.path.exists('downloaded_images14'): 
        os.makedirs('downloaded_images14')
    
    csv_file = 'image_details14.csv' #8
    csv_headers = ['Image URL', 'Resolution', 'File Size', 'Cover URL', 'Image Name']

    def write_csv(self, headers):
        with open(self.csv_file, mode='w', newline='', encoding='utf-8') as file:
            file.write(','.join(headers) + '\n')
    
    def __init__(self, *args, **kwargs):
        super(AlbumSpider, self).__init__(*args, **kwargs)
        self.write_csv(self.csv_headers)  # Write headers to CSV at the start
    
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, meta={'proxy': 'http://ZhW8jx:fos5p3@177.234.140.25:8000'})
    
    def parse(self, response):
        page_number = int(response.url.split('=')[-1])  # Extract the page number from URL
        
        # Calculate img_counter based on the page number (page 31287 => 10001, page 31288 => 10009, etc.)
        img_counter = (page_number) * 8 + 1  # Adjust based on 8 images per page
        
        # Get the cover URL (the current page URL)
        cover_url = response.url
        
        soup = BeautifulSoup(response.body, 'html.parser')
        img_boxes = soup.find_all('div', class_='img-box')
        
        for img_box in img_boxes:
            style = img_box.get('style', '')
            if 'background-image' in style:
                img_url = style.split('url(')[1].split(')')[0].strip('"\'')
                full_img_url = 'https://www.albumartexchange.com' + img_url

                # Extract image dimensions and file size
                image_info = img_box.find_next('p', class_='image-info')
                if image_info:
                    dimensions = image_info.find('span', class_='dimensions')
                    file_size = image_info.find('span', class_='file-size')

                    if dimensions and file_size:
                        image_dimensions = dimensions.get_text(strip=True)
                        image_file_size = file_size.get_text(strip=True)

                        detail_link = img_box.find('a', class_='view-details-link')
                        if detail_link:
                            detail_url = detail_link.get('href', '')
                            cover_url = 'https://albumartexchange.com' + detail_url

                        self.save_to_csv(full_img_url, image_dimensions, image_file_size, cover_url, img_counter)
                
                yield scrapy.Request(full_img_url, callback=self.download_image, meta={'img_counter': img_counter, 'proxy': 'http://username:password@your_proxy_address:proxy_port'})
                
                img_counter += 1
    
    def save_to_csv(self, img_url, dimensions, file_size, cover_url, img_counter):
        img_name = f"{img_counter:08d}.png"
        with open(self.csv_file, mode='a', newline='', encoding='utf-8') as file:
            file.write(f"{img_url},{dimensions},{file_size},{cover_url},{img_name}\n")
    
    def download_image(self, response):
        img_counter = response.meta['img_counter']
        img_name = f"{img_counter:08d}.png"
        img_path = os.path.join('downloaded_images14', img_name) #8
        
        with open(img_path, 'wb') as img_file:
            img_file.write(response.body)














# import scrapy
# import os
# from scrapy.http import HtmlResponse
# from bs4 import BeautifulSoup

# class AlbumSpider(scrapy.Spider):
#     name = "albumartexchange"
    
#     # Start URL for scraping pages (Modify range if needed)
#     start_urls = [f'https://albumartexchange.com/covers?page={i}' for i in range(19954, 20579)]
    
#     # Create directory for images if it doesn't exist
#     image_folder = 'downloaded_images(test)'
#     if not os.path.exists(image_folder):
#         os.makedirs(image_folder)
    
#     # CSV File Setup
#     csv_file = 'image_details(test).csv'
#     csv_headers = ['Image URL', 'Resolution', 'File Size', 'Cover URL', 'Image Name']
    
#     # Custom Scrapy Settings (Anti-bot and SSL Fixes)
#     custom_settings = {
#         "DOWNLOADER_CLIENTCONTEXTFACTORY": "scrapy.core.downloader.contextfactory.BrowserLikeContextFactory",
#         "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
#         "DOWNLOAD_DELAY": 2,  # Prevent bans
#         "RANDOMIZE_DOWNLOAD_DELAY": True,
#     }

#     # Write CSV header
#     def write_csv(self, headers):
#         with open(self.csv_file, mode='w', newline='', encoding='utf-8') as file:
#             file.write(','.join(headers) + '\n')
    
#     def __init__(self, *args, **kwargs):
#         super(AlbumSpider, self).__init__(*args, **kwargs)
#         self.write_csv(self.csv_headers)  # Write headers to CSV at the start
    
#     # Scrape images and details from the page
#     def parse(self, response):
#         page_number = int(response.url.split('=')[-1])  # Extract the page number from URL
#         img_counter = (page_number) * 8 + 1  # Adjust based on 8 images per page

#         soup = BeautifulSoup(response.text, 'html.parser')
#         img_boxes = soup.find_all('div', class_='img-box')
        
#         for img_box in img_boxes:
#             style = img_box.get('style', '')
#             if 'background-image' in style:
#                 img_url = style.split('url(')[1].split(')')[0].strip('"\'')
#                 full_img_url = 'https://www.albumartexchange.com' + img_url

#                 # Extract image dimensions and file size
#                 image_info = img_box.find_next('p', class_='image-info')
#                 if image_info:
#                     dimensions = image_info.find('span', class_='dimensions')
#                     file_size = image_info.find('span', class_='file-size')

#                     if dimensions and file_size:
#                         image_dimensions = dimensions.get_text(strip=True)
#                         image_file_size = file_size.get_text(strip=True)

#                         # Find cover URL from the 'view-details-link' <a> tag
#                         detail_link = img_box.find('a', class_='view-details-link')
#                         cover_url = 'https://albumartexchange.com' + detail_link['href'] if detail_link else response.url

#                         # Save image details to CSV
#                         self.save_to_csv(full_img_url, image_dimensions, image_file_size, cover_url, img_counter)

#                         # Immediately download the image as soon as it's found
#                         yield scrapy.Request(full_img_url, callback=self.download_image, meta={'img_counter': img_counter})
                
#                 img_counter += 1  # Increment the counter for each image

#     # Save image details to CSV
#     def save_to_csv(self, img_url, dimensions, file_size, cover_url, img_counter):
#         img_name = f"{img_counter:08d}.png"  # Format image name with leading zeros
#         with open(self.csv_file, mode='a', newline='', encoding='utf-8') as file:
#             file.write(f"{img_url},{dimensions},{file_size},{cover_url},{img_name}\n")

#     # Download image using Scrapy's built-in pipeline
#     def download_image(self, response):
#         img_counter = response.meta['img_counter']
#         img_name = f"{img_counter:08d}.png"
#         img_path = os.path.join(self.image_folder, img_name)

#         if response.status == 200:
#             with open(img_path, 'wb') as img_file:
#                 img_file.write(response.body)
#             self.logger.info(f"✅ Downloaded: {img_name}")
#         else:
#             self.logger.warning(f"⚠️ Failed to download {img_name}: HTTP {response.status}")





# import scrapy
# import os
# from scrapy.http import HtmlResponse
# from bs4 import BeautifulSoup

# class AlbumSpider(scrapy.Spider):
#     name = "albumartexchange"
    
#     # Start URL for scraping pages (Modify range if needed)
#     start_urls = [f'https://albumartexchange.com/covers?page={i}' for i in range(19954, 20579)]
    
#     # Create directory for images if it doesn't exist
#     image_folder = 'downloaded_images(test)'
#     if not os.path.exists(image_folder):
#         os.makedirs(image_folder)
    
#     # CSV File Setup
#     csv_file = 'image_details(test).csv'
#     csv_headers = ['Image URL', 'Resolution', 'File Size', 'Cover URL', 'Image Name']
    
#     # Custom Scrapy Settings (Anti-bot and SSL Fixes)
#     custom_settings = {
#         "DOWNLOADER_CLIENTCONTEXTFACTORY": "scrapy.core.downloader.contextfactory.BrowserLikeContextFactory",
#         "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
#         "DOWNLOAD_DELAY": 2,  # Prevent bans
#         "RANDOMIZE_DOWNLOAD_DELAY": True,
#     }

#     # Write CSV header
#     def write_csv(self, headers):
#         with open(self.csv_file, mode='w', newline='', encoding='utf-8') as file:
#             file.write(','.join(headers) + '\n')
    
#     def __init__(self, *args, **kwargs):
#         super(AlbumSpider, self).__init__(*args, **kwargs)
#         self.write_csv(self.csv_headers)  # Write headers to CSV at the start
    
#     # Scrape images and details from the page
#     def parse(self, response):
#         page_number = int(response.url.split('=')[-1])  # Extract the page number from URL
#         img_counter = (page_number) * 8 + 1  # Adjust based on 8 images per page

#         soup = BeautifulSoup(response.text, 'html.parser')
#         img_boxes = soup.find_all('div', class_='img-box')
        
#         for img_box in img_boxes:
#             style = img_box.get('style', '')
#             if 'background-image' in style:
#                 img_url = style.split('url(')[1].split(')')[0].strip('"\'')
#                 full_img_url = 'https://www.albumartexchange.com' + img_url

#                 # Extract image dimensions and file size
#                 image_info = img_box.find_next('p', class_='image-info')
#                 if image_info:
#                     dimensions = image_info.find('span', class_='dimensions')
#                     file_size = image_info.find('span', class_='file-size')

#                     if dimensions and file_size:
#                         image_dimensions = dimensions.get_text(strip=True)
#                         image_file_size = file_size.get_text(strip=True)

#                         # Find cover URL from the 'view-details-link' <a> tag
#                         detail_link = img_box.find('a', class_='view-details-link')
#                         cover_url = 'https://albumartexchange.com' + detail_link['href'] if detail_link else response.url

#                         # Save image details to CSV
#                         self.save_to_csv(full_img_url, image_dimensions, image_file_size, cover_url, img_counter)

#                         # Immediately download the image as soon as it's found
#                         yield scrapy.Request(full_img_url, callback=self.download_image, meta={'img_counter': img_counter})
                
#                 img_counter += 1  # Increment the counter for each image

#     # Save image details to CSV
#     def save_to_csv(self, img_url, dimensions, file_size, cover_url, img_counter):
#         img_name = f"{img_counter:08d}.png"  # Format image name with leading zeros
#         with open(self.csv_file, mode='a', newline='', encoding='utf-8') as file:
#             file.write(f"{img_url},{dimensions},{file_size},{cover_url},{img_name}\n")

#     # Download image using Scrapy's built-in pipeline
#     def download_image(self, response):
#         img_counter = response.meta['img_counter']
#         img_name = f"{img_counter:08d}.png"
#         img_path = os.path.join(self.image_folder, img_name)

#         if response.status == 200:
#             with open(img_path, 'wb') as img_file:
#                 img_file.write(response.body)
#             self.logger.info(f"✅ Downloaded: {img_name}")
#         else:
#             self.logger.warning(f"⚠️ Failed to download {img_name}: HTTP {response.status}")




# import scrapy
# import os
# from scrapy.http import HtmlResponse
# from bs4 import BeautifulSoup

# class AlbumSpider(scrapy.Spider):
#     name = "albumartexchange"
    
#     # Start URL for scraping pages (Modify range if needed)
#     start_urls = [f'https://albumartexchange.com/covers?page={i}' for i in range(19954, 20579)]
    
#     # Create directory for images if it doesn't exist
#     image_folder = 'downloaded_images(test)'
#     if not os.path.exists(image_folder):
#         os.makedirs(image_folder)
    
#     # CSV File Setup
#     csv_file = 'image_details(test).csv'
#     csv_headers = ['Image URL', 'Resolution', 'File Size', 'Cover URL', 'Image Name']
    
#     # Custom Scrapy Settings (Anti-bot and SSL Fixes)
#     custom_settings = {
#         "DOWNLOADER_CLIENTCONTEXTFACTORY": "scrapy.core.downloader.contextfactory.BrowserLikeContextFactory",
#         "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
#         "DOWNLOAD_DELAY": 2,  # Prevent bans
#         "RANDOMIZE_DOWNLOAD_DELAY": True,
#     }

#     # Write CSV header
#     def write_csv(self, headers):
#         with open(self.csv_file, mode='w', newline='', encoding='utf-8') as file:
#             file.write(','.join(headers) + '\n')
    
#     def __init__(self, *args, **kwargs):
#         super(AlbumSpider, self).__init__(*args, **kwargs)
#         self.write_csv(self.csv_headers)  # Write headers to CSV at the start
    
#     # Scrape images and details from the page
#     def parse(self, response):
#         page_number = int(response.url.split('=')[-1])  # Extract the page number from URL
#         img_counter = (page_number) * 8 + 1  # Adjust based on 8 images per page

#         soup = BeautifulSoup(response.text, 'html.parser')
#         img_boxes = soup.find_all('div', class_='img-box')
        
#         for img_box in img_boxes:
#             style = img_box.get('style', '')
#             if 'background-image' in style:
#                 img_url = style.split('url(')[1].split(')')[0].strip('"\'')
#                 full_img_url = 'https://www.albumartexchange.com' + img_url

#                 # Extract image dimensions and file size
#                 image_info = img_box.find_next('p', class_='image-info')
#                 if image_info:
#                     dimensions = image_info.find('span', class_='dimensions')
#                     file_size = image_info.find('span', class_='file-size')

#                     if dimensions and file_size:
#                         image_dimensions = dimensions.get_text(strip=True)
#                         image_file_size = file_size.get_text(strip=True)

#                         # Find cover URL from the 'view-details-link' <a> tag
#                         detail_link = img_box.find('a', class_='view-details-link')
#                         cover_url = 'https://albumartexchange.com' + detail_link['href'] if detail_link else response.url

#                         # Save image details to CSV
#                         self.save_to_csv(full_img_url, image_dimensions, image_file_size, cover_url, img_counter)

#                         # Immediately download the image as soon as it's found
#                         yield scrapy.Request(full_img_url, callback=self.download_image, meta={'img_counter': img_counter})
                
#                 img_counter += 1  # Increment the counter for each image

#     # Save image details to CSV
#     def save_to_csv(self, img_url, dimensions, file_size, cover_url, img_counter):
#         img_name = f"{img_counter:08d}.png"  # Format image name with leading zeros
#         with open(self.csv_file, mode='a', newline='', encoding='utf-8') as file:
#             file.write(f"{img_url},{dimensions},{file_size},{cover_url},{img_name}\n")

#     # Download image using Scrapy's built-in pipeline
#     def download_image(self, response):
#         img_counter = response.meta['img_counter']
#         img_name = f"{img_counter:08d}.png"
#         img_path = os.path.join(self.image_folder, img_name)

#         if response.status == 200:
#             with open(img_path, 'wb') as img_file:
#                 img_file.write(response.body)
#             self.logger.info(f"✅ Downloaded: {img_name}")
#         else:
#             self.logger.warning(f"⚠️ Failed to download {img_name}: HTTP {response.status}")
