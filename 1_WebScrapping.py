
#---------------------------------------------------------------------------------
# >>>>> Steps to folow while programming :-

# Step 1  Understand the problem statement
# Step 2  Write the algorithm
# Step 3  Decide the programming language
# Step 4  Write the program
# Step 5  Test the program
#---------------------------------------------------------------------------------

#---------------------------------------------------------------------------------
# Auto Image Downloader using Web Scrapping.
#---------------------------------------------------------------------------------

from bs4 import *
import requests
import os

#---------------------------------------------------------------------------------
# Function Name : folder_create
# Description : Create the Folder
# Author : Bade Vikas Vasudeo
# Date : 01/01/2023
#---------------------------------------------------------------------------------

def folder_create(images):
    try:
        folder_name = input("Enter Folder Name :- ")
        os.mkdir(folder_name)

    except:
        print("Folder Exist with that name!")
        folder_create()
    
    # for downloaded images put in this folder
    download_images(images, folder_name)

#---------------------------------------------------------------------------------
# Function Name : download_images
# Description : Download the images in this folder
# Author : Bade Vikas Vasudeo
# Date : 01/01/2023
#---------------------------------------------------------------------------------

def download_images(images, folder_name):
    count = 0

    print(f"Total {len(images)} Image Found!")

    if len(images) != 0:
        for i, image in enumerate(images):
            try:
                image_link = image["data-srcset"]
            except:
                try:
                    image_link = image["data-src"]
                except:
                    try:
                        image_link = image["data-fallback-src"]
                    except:
                        try:
                            image_link = image["src"]
                        except:
                            pass
            try:
                r = requests.get(image_link).content
                try:
                    r = str(r, 'utf-8')
                except UnicodeDecodeError:
                    with open(f"{folder_name}/image{i+1}.jpg","wb+") as f:
                        f.write(r)
                        count += 1
            except:
                pass

        if count == len(images):
            print("All Images Downloaded!")

        else:
            print(f"Total {count} Images Downloaded Out of {len(images)}")            

#---------------------------------------------------------------------------------
# Function Name : main
# Description : main function from where execution starts
# Author : Bade Vikas Vasudeo
# Date : 01/01/2023
#---------------------------------------------------------------------------------

def main():
    print("------------------------------- By Vikas Bade --------------------------------")
    print("------------------ Application Name : Auto Image Downloader ------------------")


    url = input("Enter URL from where you want to download images :- ")

    # Using the requests methode
    r = requests.get(url)

    # Used Beautiful Soup
    soup = BeautifulSoup(r.text, 'html.parser')

    images = soup.findAll('img')
    
    folder_create(images)

#---------------------------------------------------------------------------------
    # Application Starter
#---------------------------------------------------------------------------------

if __name__ == "__main__":
    main()