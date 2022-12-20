from pytube import YouTube
import time
import os, winshell, win32com.client, pythoncom
import PySimpleGUI as sg
import ffmpeg
import subprocess
import random
import output





desk = winshell.desktop()
f = ("Arial", 14, "underline", 'bold')
f2 = ("Comic Sans", 12,)
rf = ('Comic Sans Ms', 10, 'underline')


path = os.path.join(desk, 'YT Downloader.lnk')
target = r'Youtube-Downloader-With-GUI-master\dist\ytdownload.exe'
icon = f'{desk}\Youtube-Downloader-With-GUI-master\dist\ytdownload.exe'

shell = win32com.client.Dispatch('WScript.Shell')
shortcut = shell.CreateShortCut(path)
shortcut.Targetpath = target
shortcut.IconLocation = icon
shortcut.save()

layout = [
    [sg.Text('Video URL:', font=f2),sg.Input(key='-INPUT-'), sg.DropDown(['144p','240p', '360p','720p', '1080p', '1440p', '2160p', '4320p' ], key='-RES-', font=rf)],
        [sg.Button('Download', key='Download', font=f2)],
        
        ]

iconlol = output.YtIcon
window = sg.Window('YouTube Downloader', layout, resizable=False, use_custom_titlebar=True, titlebar_icon=iconlol, titlebar_font=f)



while True:
    
    try:
        event, values = window.read()

        
        
        if event == sg.WIN_CLOSED:
            break
        
        if event == 'Download' and values['-RES-'] == '144p' or '240p' or '360p' or '480p' or '720p' or '1080p' or '1440p' or '2160p' or '4320p':
            try:

                input_value = values['-INPUT-']
                yt = YouTube(input_value)
                res_value = values['-RES-']
                vid = yt.streams.filter(only_video=True, resolution=res_value).first().download(output_path='C:\Temp',filename='Vid.mp4')
                aud = yt.streams.filter(only_audio=True).first().download(output_path='C:\Temp', filename='Aud.mp4')
                
                
                
                
            
                
                subprocess.run(f'ffmpeg -i C:\Temp\Vid.mp4 -i C:\Temp\Aud.mp4 -c copy {desk}\Youtube\EpikDownloadFromMyEpikDownloader{random.randint(1,99)}.mp4',  shell=True)
                sg.popup('Download Complete!')
                os.remove('C:\Temp\Vid.mp4')
                os.remove('C:\Temp\Aud.mp4')
                os.remove(f'{desk}\Youtube\{yt.title}.mp4')
            
            
            except Exception as error:
                print(error)
            
            
        
            
            
      

            
           
            
        window.refresh()
            
    except Exception as e:
        print(e)           
            
            
            
                
            
                
            

        
        

