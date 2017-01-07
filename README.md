# Python-Music-Metadata-Fetcher
Search up songs, pull metadata from spotify and lyrics wikia, write back to id3 tag
Overview
---
In our example we will use "Jingle Bells" by James Lord Pierpont , a public domain song.
- 1) Load songs into /Songs folder
- 2) Add approrpiate text into blacklist
- 3) Run FetchMetadata.py
- 4) Check over songData.csv && Manually fix errors
- 5) Run readCSVEditTags.py and the songs will be converted!
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
