import pytube

download_loc = "./"
url = input("Enter Video URL: ")
#example url: https://youtu.be/u9KJ-oJ_gU0

vid = pytube.YouTube(url)
stream = vid.streams.get_highest_resolution()

stream.download()