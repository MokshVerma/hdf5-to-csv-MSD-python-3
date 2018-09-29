
# coding: utf-8

# In[69]:


import pandas as pd
import numpy as np
import csv
import re
import urllib,json
from musixmatch import Musixmatch
musixmatch=Musixmatch('e5e7719b47f96c02f10ecc01d2025414')  #Musixmatch authentication


# In[70]:


df = pd.read_csv('SongCSV.csv')  #DataFrame
df.head()
songNameList = df['Title'].values.tolist()  #Creating a list of the songName column
artistNameList = df['ArtistName'].values.tolist()  #Creating a list of the artistName column
albumNameList = df['AlbumName'].values.tolist()  #Creating a list of the albumName column


# In[49]:


songNameList[0] = re.sub(r'\([^)]*\)', '', songNameList[0])  #Removes anything that's in the parenthesis of song name. for example Mr. Brightside (Remix). The bracket part gets removed.
songNameList[0]


# In[68]:


lyricsList = []


# In[39]:


#Trying out how the loop would work for one song lyrics
# lyrics = musixmatch.matcher_lyrics_get(songNameList[0], artistNameList[0])
# print(lyrics)

# lyricsList.append(lyrics['message']['body']['lyrics']['lyrics_copyright'])
# lyricsList


# In[72]:



for i in range(0, 10000):
    songNameList[i] = re.sub(r'\([^)]*\)', '', songNameList[i])  ##Removes anything that's in the parenthesis of song name. for example Mr. Brightside (Remix). The bracket part gets removed.
    if(songNameList[i].startswith('b')):  #Some song names have the letter 'b' in the starting of their names. This removes that.
        songNameList[i] = songNameList[i][1:]

    print(f'Song Name: {songNameList[i]} \nArtist Name: {artistNameList[i]}')
    lyricsQ = musixmatch.matcher_lyrics_get(songNameList[i], artistNameList[i])
    if(lyricsQ['message']['header']['status_code'] == 200):  #status code 200 means successful query. And we will append the result to the end of our lyricsList
        lyricsList.append(lyricsQ['message']['body']['lyrics']['lyrics_body'])
    else:  #In case of an unsuccessful query, append empty string
        lyricsList.append('')
        print('Lyrics not found!')
    print(lyricsList)


# In[77]:


print(len(lyricsList)) #Tells us how many lyrics have we gotten.


# In[81]:


csv_input = pd.read_csv('SongCSV.csv')  #Reads csv
csv_input['Lyrics']=lyricsList  #Creates a new
csv_input.to_csv('output.csv')  #New output file


# In[78]:


csv_input = pd.read_csv('SongCSV.csv')
csv_input['Lyrics'] = lyricsList
csv_input.to_csv('output.csv')

