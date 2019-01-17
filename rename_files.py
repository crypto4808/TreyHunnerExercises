"""Using the concept of HARDLINKS 
#touch x
#ls -l x
#ln x y

#Automate creating hardlinks in shell
#mkdir backup
#for a in *; do ln $a backup/$a; done """

""" STEP1: GET filesnames into Python 
ls > x.py
Throw triple quotes around the filenames so you 
have one giant string LOL!!
Edit and remove the backup directory any x.py. 

use 
str.lstrip()
str.rstrip()
str.strip()

str.split([s])


"""

files = """ list of files 
""".strip().split('\n')

pyweek game installer
https://github.com/larryhastings/pyweek24

install.my.sincerest.apologies.on.ubuntu.17.10.py


Python multimedia tagging library
pip install pytaglib 

decant.bandcamp.py
decant.cdbaby.py
decant.google.py


automate everything instead of separate

make random-named directory
os.system("unzip", + zipfile)
flatten_directory()
read_all_metadata()
if we have all the metadata we need 
    titlecase and clean up artist/album/titlecase
    rename media files to "{title}{{artist}}.{ext}"
    write"{artist}-{album}.m3u"
    rename directory to "artist-album"



