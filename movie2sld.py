import subprocess as sp
import os
import sys
import shutil

if sys.platform == 'win32':
    ffmpeg = '"C:\\Program Files\\ffmpeg-2.2.3-win64-static\\bin\\ffmpeg.exe"'
else:
    ffmeg = '/usr/bin/avconv'

movie = sys.argv[1]
ext = movie.split('.')[-1]
name = movie[:-4]

try:
    shutil.rmtree( name+ '_FILES')
except:
    pass

os.mkdir(name+ '_FILES')


if len(sys.argv)>2:
    srt = sys.argv[2]
else:
    srt = name +'.srt'
    

arq_srt = open(srt,'r')

html = open(name+'.html', 'w')
html.write('<html><body>\n')
    
text = arq_srt.readlines()
i = 0
for l in text:
    a = l.split('-->')
    if len(a)>1:
        a = a[0].split(',')
        i = i+1
        sp.call('%s -i "%s" -ss "%s" -vframes 1 "%s/%d.jpg"' % (ffmpeg, movie, a[0],name+'_FILES',  i) , shell=True) 
        html.write('<img src ="%s_FILES/%d.jpg"/>\n' % (name,i))
    else:
        html.write('<h3>'+ l + '</h3>')
        
html.write('</body></html>')
html.close()
