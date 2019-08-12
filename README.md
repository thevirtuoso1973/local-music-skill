# <img src='https://raw.githack.com/FortAwesome/Font-Awesome/master/svgs/solid/music.svg' card_color='#42ECE8' width='50' height='50' style='vertical-align:bottom'/> Local Music Player
Play downloaded mp3 files on your `~/Music` path with MycroftAI on Linux.

## About
This is a 'skill'/add-on for the MycroftAI assistant that lets you play mp3 files on your computer.

Mycroft currently looks through the files in `~/Music` (`/home/Music`) path to see if the song mentioned is present.
You can edit the code in `__init__.py` if you want it to look through another directory.

It compares the filenames to the user's request and plays the matching song, if a match is confident enough.

N.B. you can put a bunch of mp3 files in a folder and ask it to play _folder name_ and it'll play all the songs in that folder. Great for albums!

## Examples
* "Play Money by Pink Floyd"
* "Pause"
* "Resume"

## Credits
@thevirtuoso1973

## Supported Devices 
platform_picroft platform_plasmoid 

## Category
Entertainment
IoT
**Music**
Media

## Tags
#music
#linux
#listen
#downloaded
