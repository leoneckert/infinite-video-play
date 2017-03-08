import os
import random
from pyfiglet import Figlet
import subprocess

def playRandomVideo():
    videos = list()
    for path in os.listdir("videos"):
        if path.startswith(".DS_Store"):
            continue
        videos.append(path)
    ran_path = random.choice(videos) 
    print "\n"*10
    print ran_path
    print videos
    print "\n"*10

    f = Figlet(font='banner', width=1000)
    print f.renderText('add to poopoo@gmail.com')
    subprocess.call(["ffplay", "-autoexit", os.path.join("videos", ran_path)])
    print "done"

while True:
    playRandomVideo()
