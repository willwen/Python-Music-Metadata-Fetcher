import eyed3 #to modify the id3 tag
import csv #to export data to csv 
import os #to get all files in directory
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
blacklistedChars = [':', '\\', '/', '*', '?', '\"', '<' ,'>' ,'|']
os.chdir('./Songs');    
with open('songData.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    #fieldnames = ['filenameOld','filenameNew','songName', 'artistName', 'albumName', 'coverArtFileName', 'lyrics']
    for row in reader:
        filenameOld = row['filenameOld'];
        extension = filenameOld[-4:];
        if(row['filenameNew'] != ''):
            filenameNew = row['filenameNew'] + extension;
            #windows filenames cannot contain ':' '\' '/' '*' '?' '"' '<' '>' or '|'
            filenameNewSafe = filenameNew;
            for char in filenameNew:
                if(char in blacklistedChars):
                    filenameNewSafe=filenameNewSafe.replace(char, ' ')
            try:
                os.rename(filenameOld, filenameNewSafe)
            except:
                print "can't rename file " + filenameOld
                #filenameNew = filenameOld
                pass
        else:
            filenameNewSafe = filenameOld;
        songName = row['songName'];
        artistName = row['artistName'];
        albumName = row['albumName'];
        coverArtFileName = row['coverArtFileName'];
        lyrics = row['lyrics'];
        

        #Start Writing to ID3 Tag
        songfd = eyed3.load(filenameNewSafe);
        #None is returned when the file type (i.e. mime-type) is not recognized
        tag = songfd.tag;
        if tag is not None:
            try: 
                if songName is not '':
                    tag.title = songName.decode('utf-8')
                if artistName is not '':
                    tag.artist = artistName.decode('utf-8')
                if albumName is not '':
                    tag.album = albumName.decode('utf-8')
                if coverArtFileName is not '':
                    imagedata = open(coverArtFileName,"rb").read()
                    tag.images.set(3,imagedata,"image/jpeg")

                # append image to tags
                if lyrics is not None:
                    tag.lyrics.set(lyrics.decode('utf-8','ignore'));
            except:
                pass;
            tag.save();

