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



