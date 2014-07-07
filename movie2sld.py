# -*- coding: utf-8
import subprocess as sp
import os
import sys
import shutil


if sys.platform == 'win32':
    ffmpeg = '"C:\\Program Files\\ffmpeg-2.2.3-win64-static\\bin\\ffmpeg.exe"'
else:
    ffmpeg = '/usr/bin/avconv'

movie = sys.argv[1]
ext = movie.split('.')[-1]
name = movie[:-4]

cmd_model = '%s -i "%s"' % (ffmpeg, movie)

try:
    shutil.rmtree( name+ '_FILES')
except:
    pass

os.mkdir(name+ '_FILES')
shutil.copy('jquery.js', name+ '_FILES')
shutil.copy('unslider.min.js', name+ '_FILES')
shutil.copy('style.css', name+ '_FILES')

if len(sys.argv)>2:
    srt = sys.argv[2]
else:
    srt = name +'.srt'
    

arq_srt = open(srt,'r')

html = open(name+'.html', 'w')
html.write('''<!doctype html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">	
        <script src="%s_FILES/jquery.js"></script>
        <script src="%s_FILES/unslider.min.js"></script>
        <link rel="stylesheet" href="%s_FILES/style.css">
        </head>
    <body>
        <div class="banner">
            <ul>
''' % (name, name, name) )
    
text = arq_srt.readlines()
i = 0
cmds = []
cmd = cmd_model

for l in text:
    a = l.split('-->')
    if len(a)>1:
        a = a[0].split(',')
        content = '<br><li><img height="auto" width="1000px" src="%s_FILES/%d.jpg"/>\n' % (name,i)
        sp.call('%s -ss "%s" -i "%s" -vframes 1 "%s/%d.jpg"' % (ffmpeg, a[0], movie, name+'_FILES',  i) , shell=True) 
        html.write(content)
        i = i+1
    else:
        html.write('<h3>'+ l + '</h3>')

html.write('''
            </div>
            
        <script>
            $(function() {
                $('.banner').unslider({
                    speed: 0,               //  The speed to animate each slide (in milliseconds)
                    delay: 30000,              //  The delay between slide animations (in milliseconds)
                    complete: function() {},  //  A function that gets called after every slide animation
                    keys: true,               //  Enable keyboard (left, right) arrow shortcuts
                    dots: true,               //  Display dot navigation
                    fluid: false              //  Support responsive design. May break non-responsive designs
                });
            });
        </script>
    </body>
</html>
''')
html.close()
