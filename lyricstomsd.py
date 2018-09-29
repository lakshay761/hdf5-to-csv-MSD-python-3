
# coding: utf-8

# In[69]:


import pandas as pd
import numpy as np
import csv
import re
import urllib,json
from musixmatch import Musixmatch
musixmatch=Musixmatch('e5e7719b47f96c02f10ecc01d2025414')


# In[70]:


df = pd.read_csv('SongCSV.csv')
df.head()
songNameList = df['Title'].values.tolist()
artistNameList = df['ArtistName'].values.tolist()
albumNameList = df['AlbumName'].values.tolist()


# In[49]:


songNameList[0] = re.sub(r'\([^)]*\)', '', songNameList[0])
songNameList[0]


# In[68]:


lyricsList = []


# In[39]:


lyrics = musixmatch.matcher_lyrics_get(songNameList[0], artistNameList[0])
print(lyrics)

lyricsList.append(lyrics['message']['body']['lyrics']['lyrics_copyright'])
lyricsList


# In[72]:



for i in range(0, 10000):
#     songNameList[i] = songNameList[i].strip('"')
#     songNameList[i] = songNameList[i].replace('_', '')
#     songNameList[i] = songNameList[i].replace(albumNameList[i], '')
    songNameList[i] = re.sub(r'\([^)]*\)', '', songNameList[i])
    if(songNameList[i].startswith('b')):
        songNameList[i] = songNameList[i][1:]
#     artistNameList[i] = artistNameList[i].strip('&')
#     artistNameList[i] = artistNameList[i].replace('_', '')
    print(f'Song Name: {songNameList[i]} \nArtist Name: {artistNameList[i]}')
    lyricsQ = musixmatch.matcher_lyrics_get(songNameList[i], artistNameList[i])
    if(lyricsQ['message']['header']['status_code'] == 200):
        lyricsList.append(lyricsQ['message']['body']['lyrics']['lyrics_body'])
    else:
        lyricsList.append('')
        print('Lyrics not found!')
    print(lyricsList)


# In[77]:


print(len(lyricsList))


# In[81]:


csv_input = pd.read_csv('SongCSV.csv')
csv_input['Lyrics']=lyricsList
csv_input.to_csv('output.csv')


# In[78]:


csv_input = pd.read_csv('SongCSV.csv')
csv_input['Lyrics'] = lyricsList
csv_input.to_csv('output.csv')

