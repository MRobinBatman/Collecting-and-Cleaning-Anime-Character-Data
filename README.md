<p align="center">
<img  src="https://miro.medium.com/max/500/1*yWFQiGjlgHUVYeh4ELELyw.jpeg" />
</p>

# Web-Scraping/Data-Cleaning Anime Character Data

This is a repository that showcases the data cleansing process I used to curate a dataset of all of the most popular characters in anime. There is a lot of fan-created content perfect to be mined for my future project hosted on [Anime-Planet.com](https://www.anime-planet.com/characters/all); when I actually saw how much data on individual characters was present I realized it would make a good practice dataset for me. I plan to use this data later to create a cosplay-suggestion bot. This project was good practice doing some practial data collection and cleaning. During this project, I did some of the data-cleaning in python and the rest using tableau prep-builder since I was using Tableau for a class at the time and found it useful. I saved copies of my '.csv' files as I went to show the progress I made as I worked through each step.

## Step 1
First I wrote a simple python bs4 scraper to go and collect the data on anime characters off of Anime-Planet.com into a '.csv' file so that I could store the data in a usable format for later. The script I wrote worked well, however the sheer amount of data I was scraping became an issue and my program crashed part-way through being completed.

## Step 2
I decided not to abandon the data-collection progress I had made when my program crashed since it took several hours to complete. Since I was using the 'tqdm' python library, I was able to clearly see how far through my program had executed before it forcibly stopped. I made a few small changes in the code, causing it to pick up from the page it had crashed on, and continue from there. This  process continued  until I had all of the data from the website. Once completed I realized that a lot of the data I had collected was not formatted in a way that I would be able to find useful. The resulting '.csv' files from this process are located in the '/Step2' folder.

## Step 3
The first thing I did to organize things once all the data was collected was to consolidate the data from several '.csv' files into one file. I did this using some simple joins in Tableau Prep-builder.

## Step 4
The next step was simply to delete the columns that were unneccessary that were an artifact of how I iterated through a loop to combine the files.

## Step 5
Number the order of the characters to help preserve their order and make popular characters easier to sort.

## Step 6
Next, I removed a few empty rows, and fixed where in some places the tags/Gender/Hair_Color column's contents were in the wrong column. This was done using joins in Tableau Prep-Builder.

## Step 7
I next removed many of the characters that were missing 3 or more columns of data. This removed a couple thousand entries at the tail end of the dataset as ranked by the popularity of each  character.

## Step 8
Here, I simply removed the old copy of each column that had been formatted poorly. I then renamed the leftover columns to a more easy-to-read format.

# Finish
My dataset has been refactored into a more useful format and I cut down on the file size a bit in the process. I think the resulting dataset will be useful in a futrue project.
