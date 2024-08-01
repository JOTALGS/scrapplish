import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver (Make sure to replace 'your_path_to_webdriver' with the actual path to your WebDriver)
driver = webdriver.Chrome(executable_path='your_path_to_webdriver/chromedriver')

# Navigate to the page
driver.get('https://www.800florals.com/fresh-flowers.html')

# Wait for the page to load (adjust the sleep time if necessary)
time.sleep(5)

# Find all product-grid-item elements
product_grid_items = driver.find_elements(By.CLASS_NAME, 'product-grid-item')

# Create an 'images' directory if it doesn't exist
os.makedirs('images', exist_ok=True)

# Extract image URLs and titles and download the images
for item in product_grid_items:
    img_element = item.find_element(By.TAG_NAME, 'img')
    img_url = img_element.get_attribute('src')
    title_element = item.find_element(By.CLASS_NAME, 'itemName')
    title = title_element.text
    print(f'Title: {title}, Image URL: {img_url}')
    
    # Download the image
    img_data = requests.get(img_url).content
    img_name = os.path.join('images', img_url.split('/')[-1])
    
    with open(img_name, 'wb') as handler:
        handler.write(img_data)

# Close the WebDriver
driver.quit()
