#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
TangDou Downloader
Downloads a TangDou dancing video. 
Using a Mobile User Agent is a very simple way to get file links. 
Usage: tddown.py links | -l <list file> [-t save_path]
Note: you could give multiply links separated by space.

Written by Cinhi Young. Happy New Year!
Licensed under MIT
'''
import os
import sys
import urllib
import urllib2
import re

# user_agent = "Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36"
re_getvideo = r'http[s]*:\/\/aqiniu[share]*\.tangdou\.com\/[0-9A-Z-]*\.mp4(\?sign=[0-9a-z]*&t=[0-9a-z]*)*'
re_getlink = r'^http[s]*://(www\.|m\.)tangdou\.com\/\S*|share\.tangdou\.com\/play\.php\?vid=[0-9]*'
version = 0.1
links = []
vidlinks = {} # "url" : "title"
args = {}
getfromlist = False
links_available = '''
m.tangdou.com
www.tangdou.com
share.tangdou.com
'''
def cprint(text,color=7) : 
    '''
    output colored text if is not in Windows
    '''
    if sys.platform != 'win32' :
        print("\x1b[3" + str(color) + "m" + text + "\x1b[0m")
    else :
        print(text)

def parse_args():
    global getfromlist
    # Prevent mistakes from start
    # Although bugs will still present :)
    args['dest_path'] = '.'
    if len(sys.argv) <=1 :
        cprint("Fatal: No argument given.",1)
        cprint("Usage: tddown.py link | -l <list file> [-t save_path]\nNote: you could give multiply links separated by space.\nLinks available:")
        cprint(links_available)
        exit(1)
    if '-t' in sys.argv :
        try:
          cprint("Will save files to " + str(sys.argv[sys.argv.index('-t')+1])+'/',6)
        except :
            cprint("Fatal: No destination given.",1)
            cprint("Usage: tddown.py link | -l <list file> [-t save_path]\nNote: you could give multiply links separated by space.\nLinks available:")
            cprint(links_available)
            exit(1)   
        args['dest_path'] = (sys.argv[(sys.argv.index("-t")+1)] + '/')
         # Check if the dest_path is available
        try:
            os.listdir(args['dest_path'])
        except :
            try:
                os.mkdir(args['dest_path'])
            except:
                cprint("Fatal: Destination path is not found and unable to create. Exiting.",1)
                exit(1)
        try:
            open(args['dest_path'] + 'tempfile','wb')
        except:
            cprint("Fatal: Destination path is not writable. Make sure you have right permission. Exiting.",1)
            exit(1)
        os.remove(args['dest_path'] + 'tempfile')

    if '-l' in sys.argv :
        try:
          cprint("Will get links from file " + str(sys.argv[sys.argv.index('-l')+1]),6)
        except :
            cprint("Fatal: No list file given.",1)
            cprint("Usage: tddown.py link | -l <list file> [-t save_path]\nNote: you could give multiply links separated by space.\nLinks available:")
            cprint(links_available)
            exit(1)
        args['list_file'] = sys.argv[(sys.argv.index("-l")+1)]
        getfromlist = True
    for arg in sys.argv: # Collect links
        if re.search(pattern=re_getlink,string=arg):
            links.append(arg)

def get_links():
    global links
    cprint("Getting links from file " + str(sys.argv[sys.argv.index('-l')+1]),6)
    try: 
        listfile = open(args["list_file"],'r')
    except:
        cprint("Fatal: Error occured when opening file " +args["list_file"] + ". Exiting.",1)
        exit(1)
    rawdata = listfile.read().split('\n')
    for line in rawdata :
        if re.search(pattern=re_getlink,string=line):
            links.append(line.replace('aqiniushare','aqiniu'))
    listfile.close()
    del listfile

def parse_links():
    # downloader = urllib2.build_opener()
    # downloader.addheaders = [('User-Agent',user_agent)]
    for link in links:
        try:
            cprint("\nGetting data from " + link + "...",6)
            rawdata = urllib2.urlopen(link).read()
        except:
            cprint("Error: Unable to access " + link + '. Ignoring.\n')
            continue
        try:
            tmpurl = re.search(pattern=re_getvideo, string=rawdata).group()
        except:
            cprint("Video link not found in " + link + '.')
            continue
        tmptitle = unicode(re.sub(pattern=ur'<\/*title>',repl=' ',string=(re.search(pattern=r'<title>[\s\S]*<\/title>',string=rawdata).group())) + u'.mp4')
        vidlinks[tmpurl] = tmptitle
        print vidlinks


def download(dl_link,name):
    cprint("Downloading " + name + "...")
    try:
        urllib.urlretrieve(dl_link,args['dest_path'] + name)
    except :
        cprint('Unable to download file. Ignoring.',1)
        try:
            os.remove(args['dest_path'] + name)
        except :
            a = 'a'
        return
    cprint("Finished downloading " + name + '.',6)
    return
        
def main() :
    print("TangDou Downloader v"+str(version) + '\n')
    parse_args()
    if getfromlist :
        get_links()
    if len(links) == 0 :
            cprint("Fatal: No links found.",1)
            cprint("Usage: tddown.py link | -l <list file> [-t save_path]\n")
            exit(1)
    parse_links()
    if len(vidlinks) < 1:
        cprint("No video found. Exiting.",1)
        exit(1)
    for item in vidlinks :
        cprint("Added video " + vidlinks[item] )

    for video in vidlinks:
        download(video,vidlinks[video])

if __name__ == "__main__" :
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
