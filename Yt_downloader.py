import yt_dlp
import os

input_url = input("Enter the viddeo url :  ")

ydl_opts = {}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([input_url])

print("Video Donwloaded Sucessfully ! at: ")
current_file_directory = os.path.dirname(os.path.realpath(__file__))
print(current_file_directory)
