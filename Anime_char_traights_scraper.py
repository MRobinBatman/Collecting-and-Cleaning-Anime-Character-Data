#-*- coding: utf-8 -*-
"""
Scraping data about anime characters and their traights for use in future cosplay suggestion bot project
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
from tqdm import tqdm

headers = { 
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36', 
'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
'Accept-Language' : 'en-US,en;q=0.5',
'Accept-Encoding' : 'gzip', 
'DNT' : '1', # Do Not Track Request Header 
'Connection' : 'close'
}

start_url = 'https://www.anime-planet.com/characters/all'

page = 8227 
url = f"https://www.anime-planet.com/characters/all?page={page}"

master_list = pd.DataFrame(columns=["Names","Gender","Hair_Color","Tags","Anime","Manga"])

def gen_soup(url):
    r= requests.get(url, headers=headers)

    content = r.content
    soup = BeautifulSoup(content, features='html.parser')
    #print(soup)
    # print(soup.prettify)
    return soup

# gen_soup(url)

count = 0

#Testing tqdm progress bar

runs = 7435
pbar = tqdm(total = runs)

while page <15662:
    # print(url)
    s = gen_soup(url)
    table = s.find("table", attrs={"class":"pure-table stickyHeader striped"})
    for row in table.findAll("tr"):
        # print(f"\n\nRow #: {count}")
        cells = row.findAll("td")
        name = row.find("a", attrs={"class":"name"}).text
        
        # print(name)
        ul = row.findAll("ul")
        traights  = ul[0]
        
        
        
        #Get the tags list if applicable
        if( len(ul) >1):
            tags = ul[1]
        else:
            tags= ""
            
        # Get hair color and gender if applicable
        gen_hair = []
        g = traights.findAll("li")
        for each in g:
            gen_hair.append(each.text)
        # print(gen_hair)
        gender = gen_hair[0]
        if(len(gen_hair)>1):
            hair_color = gen_hair[1]
        else:
            hair_color = ""
        
        
        # Get Tags
        if tags != "":
            t = tags.findAll("li")
            tags = []
            for each in t:
                tags.append(each.text)
            # print(tags)
            # print(ul[2].text)
            
        # Get anime if applicable
        if len(ul)>2:
            anime = ul[2]
            a = anime.findAll("li")
            anime = []
            for each in a:
                anime.append(each.text)
            # print(type(anime))
        else:
            anime = ""
        
        #Get manga if applicable
        if len(ul) >3:
            manga = ul[3]
            m = manga.findAll("li")
            manga = []
            for each in m:
                manga.append(each.text)
        else:   
            manga = ""
        entry = [name,gender,hair_color,tags,anime,manga]
        master_list.loc[len(master_list)] = entry
        
        count +=1
    
    #Upp
    pbar.update(1)
    page +=1
    url = f"https://www.anime-planet.com/characters/all?page={page}"
pbar.close()
master_list = master_list.drop_duplicates()

master_list.to_csv("anime_chars2.csv")