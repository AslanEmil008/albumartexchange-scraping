# albumartexchange-scraping

# Introduction
This repository is for downloading images and scraping data about images from the website albumartexchange.com.
It is a Scrapy project that uses an proxy to scrape the website.
This code can scrape and download up to 10,000 images in about one hour.
The scraped data includes Image name, image URL, image resolution, and the URL of the page from which the image was scraped.
You can customize the number of images to download and filter results based on your needs.
The images are downloaded into a folder, and the data about each image is saved in a CSV file.



# Getting started
## Usage

**1.** Clone the Repository
```bash
git clone https://github.com/AslanEmil008/albumartexchange-scraping.git
cd albumartexchange-scraping
```
**2.** Then install requirments.txt
```bash
pip install -r requirements.txt
```

## How to run
**1.** To run Scrapy, go to the spiders folder and open albumart.py, then locate the proxy section.
```bash
def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, meta={'proxy':''http://username:password@your_proxy_address:proxy_port'})
```
<b>Change this `http://username:password@your_proxy_address:proxy_port` to your proxy server</b>

> [!NOTE]
> Not every proxy works with this site, and some VPNs may also be blocked.
> To avoid being blocked, use residential proxies

**2.** In the same file, find:
```bash
yield scrapy.Request(full_img_url, callback=self.download_image, meta={'img_counter': img_counter, 'proxy': 'http://username:password@your_proxy_address:proxy_port'})
```
Change this `http://username:password@your_proxy_address:proxy_port` to your proxy server


**3.** Open `settings.py` and find the section related to proxies:
```bash
PROXY = 'http://your_proxy_address:proxy_port'  # Replace with your actual proxy URL
PROXY_USER_PASS = 'username:password'    # Replace with your actual proxy username and password
```
<br>
Replace with your actual proxy URL <br>
Replace with your actual proxy username and password <br>

**4** You can change the page range to specify which pages you want to scrape <br>
In `albumart.py` find this line:
```bash
 start_urls = [f'https://albumartexchange.com/covers?page={i}' for i in range(1, 101)]
```
And change the range(1, 101) to the range you need, for example range(100, 200). <br>

After making this chnages run the spider

**5**Run spider
```bash
scrapy crawl albumartexchange
```


### After running Spider you will get:
Folder name: downloaded_images
- Images saved in a folder, as defined in this part of the code:
  ```bash
  if not os.path.exists('downloaded_images'): 
        os.makedirs('downloaded_images')
  ```
  Csv name: image_details.csv
- A CSV file containing image data, as defined in this part of the code:
  
  ```bash
  csv_file = 'image_details.csv' 
    csv_headers = ['Image URL', 'Resolution', 'File Size', 'Cover URL', 'Image Name']

  ```

  #### What data is in the CSV
  - Image Url
  - Resolution
  - File Size
  - Cover URL(the page url where image is downlaoded)
  - Image Name (e.p 00000001.png, and so on)



> [!NOTE]
> If you want to change the folder where images is downloading or you want to run code twice for different pages and sav images in different folders you can must:
Find this lines in code `albumart.py`
1.
```bash
if not os.path.exists('downloaded_images'): 
        os.makedirs('downloaded_images')
```
Change the folder name to whatever you want
2. Then find this lin in same `albumart.py` file:
```bash
 img_path = os.path.join('downloaded_images', img_name) 
```
Change the same folder name whatever you want 

> [!NOTE]
> If you want change csv name find this part of code in `albumart.py`
```bash
 csv_file = 'image_details14.csv'
```




