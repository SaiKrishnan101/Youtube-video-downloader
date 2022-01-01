from pytube import YouTube
from pytube import Playlist

def YouTubeDownloader(video_url, path):
    yt = YouTube(video_url)
    print(f'Downloading:{yt.title}')
    yt = yt.streams.get_highest_resolution()
    yt.download(path)


def YouTubeDownloaderPlaylist(video_url,path):
    p = Playlist(video_url)
    Len = p.length
    cnt = 0
    for video in p.videos:
        print(f'Downloading: {video.title}')
        video = video.streams.get_highest_resolution()
        video.download(path)
        print(f'Remaining:{Len-cnt}')
        print()
        cnt += 1


print("---------Welcome To Youtube Downloader-------")

Choice = int(input("Enter 0 For Single Video Or 1 For A Playlist:"))
print()
if Choice==0:
    Link = input("Enter The Link Of The Video: ")
    print()
    SAVE_PATH = input("Enter The Path To Save The Video: ")
    YouTubeDownloader(Link, SAVE_PATH)

elif Choice==1:
    Link = input("Enter Playlist Link of the video: ")
    print()
    SAVE_PATH = input("Enter Path to save the video: ")
    YouTubeDownloaderPlaylist(Link, SAVE_PATH)
else:
    print("Enter a Valid Choice.")




print("---------TASK COMPLETED!---------")
