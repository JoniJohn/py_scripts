import pytube as pt

# specify the storage path of video
path = "C:\\Downloads"

# Download video
def download_video(url, path):
    pt.YouTube(url).streams.get_highest_resolution().download(path)

# TODO: make function download mp3
def download_mp3(url, path):
    pt.YouTube(url).streams.get_audio_only().download(path)

# Ask for the youtube url of video
url = input("Please video url: ")

option = input("""
Do you want to download Video or Mp3?\n 
1. Enter 1 for Video
2. Enter 2 for mp3
""")

if option == "1":
    download_video(url, path)
elif option == "2":
    download_mp3(url, path)
else:
    print("Sorry, we did not recoginize the option")






