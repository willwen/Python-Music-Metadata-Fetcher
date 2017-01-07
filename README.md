# Python-Music-Metadata-Fetcher
Search up songs, pull metadata from spotify and lyrics wikia, write back to id3 tag
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

Disclaimer
---
Sharing copyrighted content with other people is considered illegal. 

Examples of when file sharing becomes illegal in many places around the world:
- Downloading or sharing a copyrighted movie.
- Sharing copyrighted songs (music) to other people who have not purchased those songs or downloading songs from other people when you've not purchased that song.
- Sharing or downloading computer software (programs, games, etc.).
- Downloading or sharing a copyrighted TV show or program.

(Source: http://www.computerhope.com/issues/ch001042.htm)
