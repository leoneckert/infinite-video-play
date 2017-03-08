import os, sys
import random
from pyfiglet import Figlet
import subprocess

main_dir = "/Users/itpstudent/Google Drive/TNO" 
fflay = "./ffplay"

videos = list()

# for dev on my mac, use call with argument: $ python tnovideoscript.py dev
try:
    if sys.argv[1] == "dev":
        main_dir = "./videos"
        ffplay = "ffplay"
except: IndexError

def rechargeVideos():
    global videos
    for path in os.listdir(main_dir):
        if path.startswith(".DS_Store") or path.endswith(".txt"):
            continue
        videos.append(path)
    random.shuffle(videos)

def playRandomVideo():
    global videos
    if len(videos) == 0:
        rechargeVideos()

    ran_path = videos[-1]
    videos = videos[:-1]

    text = ""
    for line in open(os.path.join(main_dir, "banner.txt")):
	line = line.strip()
	text += "\n" + line	
    f = Figlet(font='banner', width=1000)
    print f.renderText(text)
    subprocess.call([ffplay, "-autoexit", os.path.join(main_dir, ran_path)])

while True:
    playRandomVideo()
