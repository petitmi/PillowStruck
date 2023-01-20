# 534 project - PillowStruck proposal 
## Group information
- Group name: **PillowStruck**
- Members of the group: **Nyx Zhang, Tia Wang**

## Description and Motivation of the API
- Motivation to work on the API
  
  We listen to music either for a rest to the soul or primal passion of human nature. Some of us enjoy more on the melodies or rhythms, some focus more on the lyrics, and some who can't be ignored are there to support their favorite artists.
  In this API, we will present both the features of the musical part and lyrical part for users to dive deep into the songs or the artisit they are interested. 

- Description of the APi
  
  Users can input a keyword and a type value of artist or track. If the input is about artist, the API will locate the most likely top M artist and output all their albums, all the tracks from each album and output the top selling albums and the most played songs. Otherwise if the typy value is track, it will locate the most likely top M songs and output the features like key, beat of the song, and the lyrics.
  
  [**Spotify APIs**](https://developer.spotify.com/documentation/web-api/reference/#/): The Spotify APIs provides developers with a wealth of data, such as information about musicians and song albums, users' search history, song lists, and more. We can use this vast amount of data to build our own systems.
  
  proposed functions: If the input is about artist or track, our PillowStruck API will use the search, track and artist of the Spotify API to get the artist information and music features.
  
  [**Musicmatch APIs**](https://developer.musixmatch.com/): Musicmatch APIs mainly provide the lyrics of songs.
  
  proposed functions: From the track information we will acquire from the input and Spotify APIs, we get the lyrics through Musicmatch APIs.

## Intended users and outcome
- Artists, music platform users and anyone interested in analyzing music data are our potential users.

- API wrappers can effectively simplify the process of obtaining information for the user. The simplified data can be easily accessed through functions, so that the python code can be used to further analyze the acquired data. With this wrapper, users can easily analyze the information of music platform artists and songs, and in later development, we can also help users to further obtain their account information and personal song preferences.
