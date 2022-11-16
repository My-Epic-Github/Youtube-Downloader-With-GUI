from pytube import YouTube
from sys import argv
import time
from pytube.cli import on_progress
import os, winshell, win32com.client, pythoncom
import PySimpleGUI as sg
import ffmpeg


desk = winshell.desktop()
path1 = f'{desk}\Youtube Downloads'
path2 = f'{desk}\Youtube Downloads'

path = os.path.join(desk, 'YT Downloader.lnk')
target = r'YT_Downloader\dist\ytdownload.exe'
icon = f'{desk}\YT_Downloader\dist\ytdownload.exe'

shell = win32com.client.Dispatch('WScript.Shell')
shortcut = shell.CreateShortCut(path)
shortcut.Targetpath = target
shortcut.IconLocation = icon
shortcut.save()

layout = [[sg.Input(key='-INPUT-'), sg.DropDown(['144p', '360p','720p', ], key='-RES-' )], 
        [sg.Button('Download', key='Download'), sg.Checkbox(('Download Without Video'), enable_events=True, default=False, key='box')],
        
        

]
sg.theme('Dark2')
window = sg.Window('YT to MP4', layout)



while True:
    try:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        
        if event == 'Download' and values['box'] == False:
            input_value = values['-INPUT-']
            res_value = values['-RES-']
            filetype = '.3gpp'
            yt = YouTube(input_value)
            vid = yt.streams.filter(resolution=res_value).first().download(f'{desk}\Youtube Downloads' )
            sg.popup(f'Download Complete!')

        if values['box'] == True and event == 'Download':
            if event == 'Download':
                input_value = values['-INPUT-']
                
                filetype = '.mp3'
                yt = YouTube(input_value)
                res_value = values['-RES-']
                vid = yt.streams.filter(only_audio=True).first().download(f'{desk}\Youtube Downloads')
                sg.popup('Download Complete!')
        if values['box'] == True:
            window['-RES-'].update(visible=False)
        else:
            window['-RES-'].update(visible=True)
            
           
            
        window.refresh()
            
            
            
            
                
            
                
            

        
        


    except Exception as e:
        sg.popup_error(e)



