<p align="center">
<img  src="https://miro.medium.com/max/500/1*yWFQiGjlgHUVYeh4ELELyw.jpeg" />
</p>

# Web-Scraping/Data-Cleaning Anime Character Data

This is a repository that showcases the data cleansing process I used to curate a dataset of all of the most popular characters in anime. There is a lot of fan-created content perfect to be mined for my future project hosted on [Anime-Planet.com](https://www.anime-planet.com/characters/all); when I actually saw how much data on individual characters was present I realized I would make a good practice dataset for me. I plan to use this data later to create a cosplay-suggestion bot. This project was good practice doing some practial data collection and cleaning. During this project, I did some of the data-cleaning in python and the rest using tableau prep-builder since I was using Tableau for a class at the time and found it useful. I saved copies of my '.csv' files as I went to show the progress I made as I worked through each step.

## Step 1
First I wrote a simple python bs4 scraper to go and collect the data on anime characters off of Anime-Planet.com into a '.csv' file so that I could store the data in a usable format for later. The script I wrote worked well, however the sheer amount of data I was scraping became an issue and my program crashed part-way through being completed. This lead to step 2.

## Step 2
Step 2 was decidedly not to abandon the data-collection progress made during step 1. Since I was using the 'tqdm' python library, I was able to clearly see how far through my program had executed before it forcibly stopped. I made a few small changes in the code, causing it to pick up from the page it had crashed on, and continue from there. This  process continued  until I had all of the data from the website. Once completed I realized that a lot of the data I had collected was not formatted in a way that I would be able to find useful. The resulting '.csv' files from this process are located in the '/Scraped data from each run' folder.This lead me on to step 3.

## Step 3
This step was to consolidate the data from several '.csv' files into one file. I did this using some simple joins in Tableau Prep-builder, and this was saved as . The resulting file is named 'Step3.csv'.

## Step 4
The next step was simply to delete the columns that were unneccessary that were an artifact of how I iterated through a loop to combine the files. I named the new file 'Step4.csv' as I saved the results.

## Step 5
Next, I removed a few empty rows, and fixed where in some places the tags/Gender/Hair_Color column's contents were in the wrong column. This was done using joins in Tableau Prep-Builder.
