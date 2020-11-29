try:
	from pytube import YouTube
	from pytube import Playlist
except Exception as e:
	print("Some modules are missing {}".format(e))


# url of the video to be downloaded
url = "https://www.youtube.com/watch?v=EWD8JhDlZ1s"

#--------- print the video qualities----------#
# ytd = YouTube(url)
# print(ytd)

# for x in ytd.streams.all():
# 	print(x)
#---------------------------------------------#



#--------- downloading the mp4 file-----------#
ytd = YouTube(url).streams.first().download()
print(ytd)
#---------------------------------------------#




#--------- downloading the webm file----------#
ytd = YouTube(url)
print(ytd.streams.filter(only_audio=True, subtype='webm', abr='160kbps').first().download())
#---------------------------------------------#
