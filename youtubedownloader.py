from pytube import YouTube
from pprint import pprint
yt=YouTube()
yt.url=raw_input("Url:")
yt.filename=raw_input("Save as:")
print("Avilabe Formats:")
pprint(yt.videos)
length=len(yt.videos)
flag=0
while length:
    length=length-1
    frmt=raw_input("Format:")
    resolution=raw_input("Resolution:")
    try:
        video=yt.get(frmt,resolution)
        to=raw_input("Download to:")
        print("CTRL+D to cancel download")
        video.download(to)
        print("Download Complete")
        flag=1
        break
    except Exception:
        print("All Videos cannot be downloaded")
        print("Please try a another format or resolution")
    except EOFError:
    	print("Downloading cancelled!!!!!!!")
if flag==0:
    print("Sorry the requested video cannot be downloaded")
    
