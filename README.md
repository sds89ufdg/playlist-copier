# playlist-copier

Tested on OSX running python 3.6.0

Playlist M3U files were created by exporting a playlist from Swinian, I've not tested any other playlist, but as its just a M3U it should be ok, YMMV.

Problem: how to get audio files onto a USB device for the car, without having to manually copy files or worry about the problem of ALAC files not being supported by BMW. Or some VW units don't support FLAC, so you could change the ffmpeg command for instance for whatever you or just a new function.


### Dependencies

ffmpeg
mediainfo
python3

install the above via brew:
https://brew.sh

brew install ffmpeg
brew install mediainfo
brew install python3


### Usage
usage: playlist.py [-h] -p PLAYLIST -o DESTINATION
playlist.py: error: the following arguments are required: -p/--playlist, -o/--destination

#### example
playlist.py -p ~/Desktop/ALAC.m3u8 -o ~/Volumes/car/

