# Python-Music-Metadata-Fetcher
Search up songs, pull metadata from Spotify and Lyrics Wikia, write back to id3 tag
Overview
---
In our example we will use "Jingle Bells" by James Lord Pierpont , a public domain song.
  
<ol>
  <li>Load songs into /Songs folder <br/><img src = "screenshots/before.PNG?raw=true"></img></li>

  <li>Add approrpiate text into blacklist <br/> <img src = "screenshots/blacklist.PNG?raw=true"></img></li>
  <li>Run FetchMetadata.py, resulting in : 
      <br/>
      <img src = "screenshots/middle.PNG?raw=true"></img>
</li>
  <li>Check over songData.csv & Manually fix errors  
    <br/> <img src = "screenshots/csv.PNG?raw=true"></img>
    <br/>
    <br/> <img src = "screenshots/manual add.PNG?raw=true"></img>
  </li>
  <li>Run readCSVEditTags.py and the songs will be converted!

    <br/>
      <img src = "screenshots/jingle%20bell%20before.png?raw=true" height = "640" width = "360"></img>
     <img src = "screenshots/jingle%20bell%20after.png?raw=true" height = "640" width = "360"></img>
  </li>
</ol>
Design & Details
---
Based on a safe assumption that not every song can be automatically identified, this program seeks to modularize the metadata fetching process and have a real human check over the results (the intermediate csv file) before confirming the change.
Given a song with filename A and no other data, the FetchMetadata.py script will retreive A, and strip it of any matching blacklisted text. After the title strip, resulting in A', FetchMetadata executes a search off of the spotify API in hopes of finding matches. It takes the first match and pulls out artist name, album name, song name, and cover art url. It downloads the cover art. It also constructs a new file name, A'' which combines the song name and artist name every time. After the spotify request and cover art is downloaded, FetchMetadata sends another request to lyricswikia in search of lyrics. The request now has the newly acquired spotify response title and artist. If any of the requests from spotfiy or lyricswikia return nothing, we just put an empty string entry into the excel sheet, allowing a user to change if necessary.

After FetchMetadata finishes execution, a user should check over and fill any unfilled entries in the CSV file. 

Then the user should run readCSVEditTags.py and this program will read in row by row of the CSV file and first rename the mp3 file, and then write the id3 tag. 

Alongside the whole export and import from CSV file are encoding and decoding in UTF8. This should allow song names and lyrics in other langauges to be preservered across this CSV bridge. (Has yet to be thoroughly tested)

Dependencies
---
Python 2.7.1


PyLyrics (https://pypi.python.org/pypi/PyLyrics/)
```
pip install PyLyrics
```
Spotipy (https://github.com/plamere/spotipy)
```
pip install spotipy
```
eyed3 (http://eyed3.nicfit.net/)
```
pip install eyeD3
```
Future Features
---
Can be found in the future_features.txt file

Disclaimer
---
Sharing copyrighted content with other people is considered illegal. 

Examples of when file sharing becomes illegal in many places around the world:
- Downloading or sharing a copyrighted movie.
- Sharing copyrighted songs (music) to other people who have not purchased those songs or downloading songs from other people when you've not purchased that song.
- Sharing or downloading computer software (programs, games, etc.).
- Downloading or sharing a copyrighted TV show or program.

(Source: http://www.computerhope.com/issues/ch001042.htm)
