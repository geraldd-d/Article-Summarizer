import fitz
import os
from PIL import Image
from io import BytesIO
import glob

async def extractImages(file):
    # Define minimum width and height for images
    min_width = 200
    min_height = 200
    
    pdf_file = fitz.open(stream=file.read())

    #Calculate number of pages in PDF file
    page_nums = len(pdf_file)

    #Create empty list to store images information
    images_list = []
    images_path = './frontend/public/media'

    #Extract all images information from each page
    for page_num in range(page_nums):
        page_content = pdf_file[page_num]
        images_list.extend(page_content.get_images())

    for i, image in enumerate(images_list, start=1):
        #Extract the image object number
        xref = image[0]
        #Extract image
        base_image = pdf_file.extract_image(xref)
        #Store image bytes
        image_bytes = base_image['image']
        #Store image extension
        image_ext = base_image['ext']
        #Generate image file name
        image_name = str(i) + '.' + image_ext
        img = Image.open(BytesIO(image_bytes))
        width, height = img.size
        if width >= min_width and height >= min_height:
            # Save image
            print(width, height)
            with open(os.path.join(images_path, image_name) , 'wb') as image_file:
                image_file.write(image_bytes)
                image_file.close()


images_path = './frontend/public/media'

async def delete_files():
    # Get a list of all files in the images directory
    files = glob.glob(os.path.join(images_path, '*'))

    # Loop over all files in the directory and delete them
    for file in files:
        os.remove(file)