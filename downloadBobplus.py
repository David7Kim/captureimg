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
now = datetime.datetime.now()
n_year = str(now.year)
n_month = str(now.month)
n_day = str(now.day)
n_date = n_year+'-'+n_month+'-'+n_day

def set_image_path():
    # setImage Path
    file_name = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Image", "*.png"),("JPEG Image", "*.jpg"), ("All Files", "*.*")] ,initialfile=n_date+'_Bplus_menu')
    with open(file_name, 'wb') as file:
        replacedPath = file_name.replace("/","\\")
        url_entry.delete(0 ,'end')
        url_entry.insert(0,replacedPath)

def download_image_from_html():
    #Hard Coding Url
    url = ''

    try:
        response = requests.get(url)
        #response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        img_tag = soup.find('meta',property='og:image')
        if img_tag and url_entry.get() !='':
            #getting meta content's attributes 
            img_url = img_tag.get('content')
            if img_url:
                    os.system("curl " + img_url +">" +url_entry.get())
                    status_label.config(text="completed")
                    os.startfile(url_entry.get())
            elif img_tag == '':
                status_label.config(text="Image URL not found in the HTML.")
            elif url_entry.get() =='':
                status_label.config(text="Path is not set")
        else:
            status_label.config(text="Image tag not found in the HTML.")
    except Exception as e:
        status_label.config(text=f"Error: {e}")

# Create the main application window
app = tk.Tk()
app.title("Downloads B+ Menu")
# Create and place widgets
url_label = tk.Label(app, text="Downloads Menu")
url_label.pack()

#It will used When user write url
url_entry = tk.Entry(app,width=50 )
url_entry.pack()

download_button = tk.Button(app, text="Download Image", command=download_image_from_html)
download_button.pack()

set_path_button = tk.Button(app, text="setPath", command=set_image_path)
set_path_button.pack()

status_label = tk.Label(app, text="")
status_label.pack()

# Start the application's main event loop
app.mainloop()