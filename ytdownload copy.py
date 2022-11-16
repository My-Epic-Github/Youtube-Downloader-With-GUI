from pytube import YouTube
from sys import argv
import time
from pytube.cli import on_progress
import os, winshell, win32com.client, pythoncom



desk = winshell.desktop()

path = os.path.join(desk, 'YT Downloader.lnk')
target = r'YT_Downloader\dist\ytdownload\ytdownload.exe'
icon = f'{desk}\YT_Downloader\dist\ytdownload\ytdownload.exe'

shell = win32com.client.Dispatch('WScript.Shell')
shortcut = shell.CreateShortCut(path)
shortcut.Targetpath = target
shortcut.IconLocation = icon
shortcut.save()
        

def yt():
    
    
    
    
    while True:
        link = input('\nInput the Video Link to Download: \n')
        try: 
            yt = YouTube(link, on_progress_callback=on_progress)
            print('Title:',  yt.title)
            print('Author: ', yt.author)
            print('Views:', yt.views)
            print('Date Published:', yt.publish_date)
            print('Description:', yt.description)
            print(f'Length: {yt.length} Seconds Long')

            yd = yt.streams.get_highest_resolution()

            down = yd.download(f'{desk}\Youtube Downloads')
            down
            def progress_function(stream, chunk, file_handle, bytes_remaining):
                print(round((1-bytes_remaining/link.filesize)*100, 3), '% done...\n')
                time.sleep(1.35)
                yt()
            
            
            



           
            
             


        except Exception as e:
            print(e)
            time.sleep(1)
        
    
while True:
    time.sleep(1.5)
    yt()
    
    
    
    
    
    

    

        

