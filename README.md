# Music Search

## Author
Dane (Sara) Wright


## Description
This is a Tkinter program that searches a directory for Artists, Albums, and Song metadata.
Made with the intent of tracking down which Artists/Albums/Songs from my collection of Music has broken metadata

Outputs metadata to a .csv file that is delimited with the TAB character.

The music_search.py file can be ran by itself from a terminal.
The actual GUI is the music_search_app.py file.

### Notes
Program will look for data in the root directory of your choosing.

In that directory it will look for songs following a file structure like this:
ArtistName1\
ArtistName1\Album1
ArtistName1\Album2
ArtistName1\Album2\song1.m4a


## Known Problems, Issues, And/Or Errors in the Program
Tested on Linux Mint 20.3, Pop!_OS 22.04, and Windows 11 23H2.
It works, but in Linux, it will print the tracks out of order, but grouped together.


