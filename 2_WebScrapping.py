
#---------------------------------------------------------------------------------
# >>>>> Steps to folow while programming :-

# Step 1  Understand the problem statement
# Step 2  Write the algorithm
# Step 3  Decide the programming language
# Step 4  Write the program
# Step 5  Test the program
#---------------------------------------------------------------------------------

#---------------------------------------------------------------------------------
# Links (URL) Extractor using Web Scrapping
#---------------------------------------------------------------------------------


import os
import bs4
import requests
from sys import *

#---------------------------------------------------------------------------------
# Function Name : LinksDisplay
# Description : Display the all URLs in this website
# Author : Bade Vikas Vasudeo
# Date : 01/01/2023
#---------------------------------------------------------------------------------

def LinksDisplay(URL):
    res = requests.get(URL)
    print(type(res))

    soup = bs4.BeautifulSoup(res.text, 'lxml')
    print(type(soup))

    links = soup.find_all('a', href = True)
    
    return links

#---------------------------------------------------------------------------------
# Function Name : main
# Description : main function from where execution starts
# Author : Bade Vikas Vasudeo
# Date : 01/01/2023
#---------------------------------------------------------------------------------

def main():
    print("------------------------------------- By Vikas Bade --------------------------------------")
    print("-------------- Application Name : Links (URL) Extractor using Web Scrapping --------------")
    print("--------------------------------- File Name : "+argv[0]+" ---------------------------------")


    if(len(argv) == 2):
        if(argv[1] == "-h") or (argv[1] == "-H"):
            print("This Script is used to fetch links from wikipedia file")
            exit()

        if(argv[1] == "-u") or (argv[1] == "-U"):
            print("Usage : ApplicationName")
            exit()

    # This URLs which is Scrapping the links
    url = input("Enter URL from where you want to download images :- ")
    # url = " https://www.w3schools.com/"
    
    arr = LinksDisplay(url)

    print("Links are  ")

    for element in arr:
        if "#" not in element['href']:
            print(element['href'])

#---------------------------------------------------------------------------------
    # Application Starter
#---------------------------------------------------------------------------------

if __name__ == "__main__":
    main()