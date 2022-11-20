from pytube import YouTube
from sys import argv
import time
from pytube.cli import on_progress
import os, winshell, win32com.client, pythoncom
import PySimpleGUI as sg
import ffmpeg
sg.theme('DarkGrey1')

desk = winshell.desktop()
path1 = f'{desk}\Youtube Downloads'
path2 = f'{desk}\Youtube Downloads'

path = os.path.join(desk, 'YT Downloader.lnk')
target = r'Youtube-Downloader-With-GUI-master\dist\ytdownload.exe'
icon = f'{desk}\Youtube-Downloader-With-GUI-master\dist\ytdownload.exe'

shell = win32com.client.Dispatch('WScript.Shell')
shortcut = shell.CreateShortCut(path)
shortcut.Targetpath = target
shortcut.IconLocation = icon
shortcut.save()

layout = [
    [sg.Text('Video URL:'),sg.Input(key='-INPUT-'), sg.DropDown(['144p', '360p','720p', '1080p' ], key='-RES-' )],
        [sg.Button('Download', key='Download'), sg.Checkbox(('Download Without Video'), enable_events=True, default=False, key='box')],
        
        

]

window = sg.Window('YouTube Downloader', layout)



while True:
    try:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        
        if event == 'Download' and values['box'] == False and values['-RES-'] == '1080p' or '1440p' or '2160p':
        
            input_value = values['-INPUT-']
            yt = YouTube(input_value)
            res_value = values['-RES-']
            vid = yt.streams.filter(only_video=True, resolution=res_value).first().download(output_path='C:\Temp',filename='Vid.mp4')
            
            aud = yt.streams.filter(only_audio=True).first().download(output_path='C:\Temp', filename='Aud.mp3')
            
            video = ffmpeg.input(f'C:\Temp\Vid.mp4')
            audio = ffmpeg.input(f'C:\Temp\Aud.mp3')
            merged_audio = ffmpeg.filter([video.audio, audio], 'amix')
            ffmpeg.concat(video, merged_audio, v=1, a=1).output(f'{desk}\Youtube Downloads') ,sg.popup('Download Complete')
            
            
                
        if event == 'Download' and values['box'] == False and values['-RES-'] == '144p' or '360p' or '720':
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
                vid = yt.streams.filter(only_audio=True,).first().download(f'{desk}\Youtube Downloads')
                sg.popup('Download Complete!')
        if values['box'] == True:
            window['-RES-'].update(visible=False)
        else:
            window['-RES-'].update(visible=True)
            
           
            
        window.refresh()
            
            
            
            
                
            
                
            

        
        


    except Exception as e:
        sg.popup_error(e)



