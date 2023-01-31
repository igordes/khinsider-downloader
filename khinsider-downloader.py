from selenium import webdriver
import os
import urllib.parse
import requests
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.edge.options import Options
import sys
console_url = str(sys.argv[1])
chromium_options = Options()
chromium_options.add_argument('--disable-extensions')
chromium_options.add_argument('--disable-gpu')
chromium_options.add_argument('--headless')
chromium_options.add_argument('--mute-audio')
driver = webdriver.Edge(options=chromium_options)
driver.get(console_url)
#driver.get('https://downloads.khinsider.com/game-soundtracks/album/flower-sun-and-rain-water-for-relaxing-time')
def counting_songs():
    n_songs = 0
    while True:
        try:
            driver.find_element(By.XPATH,"//*[@id='songlist']/tbody/tr[" + str(n_songs+2) + "]/td[1]/div/div")
        except:
            break
        n_songs = n_songs + 1
    print("Number of tracks: " + str(n_songs))
    return n_songs

def getLink(songsNumber):
    print("Getting track links...")
    music = [0] * songsNumber
    for i in range(songsNumber):
        stringPath = str("//*[@id='songlist']/tbody/tr[" + str(i+2) + "]/td[1]/div/div")
        driver.find_element(By.XPATH,stringPath).click()
        music[i] = driver.find_element(By.ID,'audio1').get_attribute('src')
    return music

def download_Album(songsNumber,trackList):
    OST_title = driver.find_element(By.XPATH, '//*[@id="pageContent"]/h2[1]').text
    print("Downloading album: " + OST_title)
    driver.close()
    driver.quit()
    if not os.path.exists(OST_title):
        os.mkdir(OST_title)
    ostDir = './' + OST_title + '/'
    for i in range(0,songsNumber):
        url = trackList[i]
        filename = url.split('/')[-1]
        filename = urllib.parse.unquote(filename)
        response = requests.get(url)
        if os.path.exists(ostDir + filename):
            print('"' + filename + '" already exists! Skipping to next track.')
        else:
            print('Downloading track ' + str(i+1) + ': "' + filename + '"')
            open(ostDir + filename, 'wb').write(response.content)
    print("Downloading complete!")

#MAIN

countTracks = counting_songs()
songsList = getLink(countTracks)
download_Album(countTracks,songsList)


