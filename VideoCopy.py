import yt_dlp


def downloader(url, path):
    ydl_opts = {
        'outtmpl': path,
        'format': 'best[height<=720]',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

url_lst = []
while True:
	url_inpt = input("Enter the YouTube url: ")
	if url_inpt == '': 
		break
	else:
		url_lst.append(url_inpt)
try:
	
	if len(url_lst) == 1:
		path_inpt = input("Enter the path and filename: ")
		downloader(url_lst[0],path_inpt)

	if len(url_lst) >1:
		path_inpt = input("Enter the path: ")
		for i in range(len(url_lst)):
			downloader(url_lst[i],path_inpt+f"{i}.mp4")
	if len(url_lst) == 0:
		print("Something went wrong!")

except:
	print("Some errors occured :[ ")
