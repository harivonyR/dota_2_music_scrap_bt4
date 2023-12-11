# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 16:25:24 2023

@author: harivonyratefiarison
"""
######################################################

import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import requests
import re

def download_audio(url, destination):
    try:
        response = requests.get(url, stream=True)

        # check status
        response.raise_for_status()

        # create directory if doesn't exist
        destination_folder = os.path.dirname(destination)
        
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        with open(destination, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"Le fichier audio a été téléchargé avec succès dans {destination}")
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors du téléchargement : {e}")

######################################################

"""

GET principale link

"""


driver = webdriver.Chrome()
driver.get("https://dota2.fandom.com/wiki/Heroes")

javascript_select_links = '''
    var h_list = Array.from(document.querySelectorAll("a"))
                    .map(e => e.href)
                    .filter(e => e.startsWith("https://dota2.fandom.com/wiki/") &&
                                 e !== "https://dota2.fandom.com/wiki/Heroes#" &&
                                 e !== "https://dota2.fandom.com/wiki/Heroes");
    return h_list;
'''

# Execute the JavaScript code and get the result
links = driver.execute_script(javascript_select_links)
filtered_links = [link for link in links if ":"  not in link.rsplit("/", 1)[-1]]


"""
GET secondary (sounds) links

"""

# 
for link in filtered_links :

    link = filtered_links[39]   
    try :
        #driver.get(link)
        driver.get(filtered_links[40])
        WebDriverWait(driver, 120,poll_frequency=5000).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        
        javascript_select_sound = '''
            var s_list = Array.from(document.querySelectorAll("audio > source")).map(e=>e.src)
            return s_list;
        '''
        
        sounds = driver.execute_script(javascript_select_sound)
        sounds
        
        for sound in sounds :
            audio_url = sound
            file_name = re.search(r'/([^/]+)\.mp3/', audio_url).group(1)
            #folder = filtered_links[1].rsplit("/",1)[-1]
            folder = "Music"
            destination_path = r'C:/Users/harivonyratefiarison/Downloads/sounds/'+folder+r'/'+file_name+'.mp3'
            download_audio(audio_url, destination_path)
            
    except :
        print("error on link :"+link)
            
#driver.get(sounds[2])



