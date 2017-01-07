import os #to get all files in directory
import spotipy #to get artist , album, songname
import csv #to export data to csv 
from PyLyrics import * # to download pyrics from lyrics.wikia.com
import urllib #to download album art from web
import sys



sp = spotipy.Spotify()
text_file = open('Blacklist.txt', 'r')
blacklistWords = text_file.read().splitlines();     
blacklistWords = [word.lower() for word in blacklistWords]
os.chdir('./Songs');    
with open('songData.csv', 'wb') as csvfile:
    fieldnames = [u'filenameOld',u'filenameNew',u'songName', u'artistName', u'albumName', u'coverArtFileName', u'lyrics']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()


    for filename in os.listdir('.'):
        
        if "mp3" in filename or "m4a" in filename:
            
            searchText = filename[0:-4];    
            extension = filename[-4:];    
            for word in filename.split('.')[0].split(' '):
                if word.lower() in blacklistWords:
                    searchText = searchText.replace(word, '');

            
            results = sp.search(searchText , limit=1)
            #if no results found for that file
            if(len(results['tracks']['items'])==0):
                writer.writerow({'filenameOld': filename})
            else:
                for track in results['tracks']['items']:
                    song = track['name'].encode('utf-8')
                    artist = track['artists'][0]['name'].encode('utf-8')
                    album =  track['album']['name'].encode('utf-8')
                    filenameNew = song + ' - ' + artist #unicode format
                    albumartURL = track['album']['images'][0]['url']

                    #print artist.decode('utf-8');                    
                    try:
                        albumArtFilename = "albumArt " + filenameNew.encode('utf-8') + ".jpg"
                        urllib.urlretrieve(albumartURL, albumArtFilename);
                    except:
                        sys.stderr.write('Cant download artwork @' + albumartURL+'\n') 
                        albumArtFilename = '';
                        pass                    
                    try:
                        lyrics = PyLyrics.getLyrics(artist , song).encode('utf-8');
                    except:
                        sys.stderr.write('Cant find ' + filenameNew.decode('utf-8') + ' on lyrics.wikia.com\n')
                        lyrics = '';
                        pass
                        
                    writer.writerow({'filenameOld': filename.decode('utf-8') ,
                                     'filenameNew': filenameNew.decode('utf-8'),
                                     'songName': song.decode('utf-8'),
                                     'artistName': artist.decode('utf-8'),
                                     'albumName': album.decode('utf-8'),
                                     'coverArtFileName': albumArtFilename.decode('utf-8'),
                                     'lyrics': lyrics.decode('utf-8')})



