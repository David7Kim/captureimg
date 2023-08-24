import datetime
import requests
import base64
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import os
from io import BytesIO
from urllib.request import urlopen

#Requirments to be name
def today_date():
    now = datetime.datetime.now()
    n_year = str(now.year)
    n_month = str(now.month)
    n_day = str(now.day)
    n_date = n_year+'-'+n_month+'-'+n_day

    return n_date


def textPath_reader(textPath):
    with open(textPath, 'r',encoding='UTF-8') as file:
        filePath = file.readline()

    return filePath

def download_image_from_html(imgUrl, savePath, today):
    #text file read 
    url = imgUrl
    try:
        response = requests.get(url)
        
        soup = BeautifulSoup(response.content, 'html.parser')
        img_tag = soup.find('meta',property='og:image')
        if img_tag:
            #getting meta content's attributes 
            img_url = img_tag.get('content')
            if img_url:
                    print(savePath)
                    print(today)
                    os.system("curl " + img_url +">" +savePath+today+"_Bplus_menu.jpg")
                    os.startfile(savePath+today+"_Bplus_menu.jpg")
            elif img_tag == '':
                print("Image URL not found in the HTML.")
            elif savePath =='':
                print("Path is not set")
        else:
            print("Image tag not found in the HTML.")
    except Exception as e:
        print("Error : {e}")

#main 
today = today_date()
imgUrl = textPath_reader(os.getcwd()+"\\config\\url.txt")
savePath = textPath_reader(os.getcwd()+"\\config\\path.txt")
download_image_from_html(imgUrl,savePath,today)
