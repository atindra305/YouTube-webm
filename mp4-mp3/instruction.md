# Simple Script to convert any video of format mp4 to mp3
 
# Requirements:
 - "lame"
 - "ffmpeg"
 
# If the libraries are not installed just run the following command in your terminal:
- On Mac(OS X): brew install lame ffmpeg
- On Linux(Ubuntu): sudo apt-get install lame ffmpeg
 
# How to use the script:
Just run the following command within your terminal replacing "NAME_OF_THE_VIDEO.mp4" by the name of your video file:
$ python mp4_mp3.py NAME_OF_THE_VIDEO.mp4

# Example: 

     $ python mp4_mp3.py Coding.mp4
     
### Note.- The video must be within the same directory of the python script, otherwise provide the full path.
