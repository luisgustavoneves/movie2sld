movie2sld
=========

A simple python program that creates an html page from a movie, with snapshots taken from the specified video followed by text taken from its **required** `.srt` file. Ideal for creating review material from video lectures like Khan Academy or Coursera. The html file generated is simple and can be easily edited to trim unnecessary snapshots.

Usage
-----

If the `.srt` file has the same name of the movie file:

`movie2sld.py video_file.mp4`

if the `.srt` file has a different name:

`movie2sld.py video_file.mp4 subtitle_file.stt`

Requirements
------------

- Python 2.7
- ffmpeg or avconv
