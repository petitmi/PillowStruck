
# Overview

PillowStruck uses spotify APIs and musixmatch web crawling to implement a API wrapper for analysis of specific artists, albums and tracks with pyhton.
- Group name: **PillowStruck**
- Members of the group: **Nyx Zhang, Tia Wang**  

**Motivation:** We listen to music either for a rest to the soul or primal passion of human nature. Some of us enjoy more on the melodies or rhythms, some focus more on the lyrics, and some who can't be ignored are there to support their favorite artists. In this API, we will present both the features of the musical part and lyrical part for users to dive deep into the songs or the artisit they are interested.


# Quick Start

## User Interface

To be more impressing on user interaction, we deployed a [website](http://13.56.81.102:8080/) on AWS with free tier.

<table>
<tr><th>Step 1: Search any keyword, including the "track", "artist" Object. </th> <th>Step 2: Get the results contain tracks and artists list.</th>

</tr>
<tr>
<td><img width="350" alt="image" src="https://user-images.githubusercontent.com/43694291/216788363-defccfbb-1a9f-4d71-a86d-7ec73a55e600.png">   </td>
<td><img width="350" alt="image" src="https://user-images.githubusercontent.com/43694291/216788454-f9506c73-f65f-4935-8490-7be47ae9f9eb.png">  </td>
</tr>
</table>

**Step 3.1: Explore Tracks** Click Tracks' "explore" to read track's detail, or click "home" to back to the search page. 

<table>
<tr><th>lyrics word cloud </th><th>sentiment analysis</th><th>lyrics txt detail</th></tr>
   <tr>
      <td rowspan="11">  
         <img width="200" alt="image" src="https://user-images.githubusercontent.com/43694291/216788712-2865711e-697b-4e98-97e0-0f394f083157.png">     
      </td>
      <td rowspan="11">  
         <img width="200" alt="image" src="https://user-images.githubusercontent.com/43694291/216788726-4a1272fb-e26c-4fa2-bb47-ae76515223a1.png">      
      </td>
      <td>
         <img width="200" alt="image" src="https://user-images.githubusercontent.com/43694291/216788565-70abbff6-892c-4e9f-9d28-5297cf1d9158.png"> 
      </td>
   </tr>
 </table>

**Step 3.2: Explore Artists** Click Artists' "explore" to read artist detail, or click "home" to back to the search page. 
<table>
<tr><th>artist activity analysis </th><th>Top tracks list</th><th>latest album list</th></tr>
   <tr>
      <td rowspan="11">  
         <img width="200" alt="image" src="https://user-images.githubusercontent.com/43694291/216788666-0fed05a5-3165-459a-bd9a-2a0a341ad461.png">  
      </td>
      <td rowspan="11">  
         <img width="200" alt="image" src="https://user-images.githubusercontent.com/43694291/216788686-3ce4a52f-19f7-445c-930c-61b05a0a7bc5.png">    
      </td>
      <td>
         <img width="200" alt="image" src="https://user-images.githubusercontent.com/43694291/216788705-4946936d-0a6d-47ac-8af0-9ae10fa5d428.png">
      </td>
   </tr>
 </table>
    
> **Note:** *However, lyrics acquirement and sentiment analysis can only run on private server instead of the above web server, due to financial and time restrictions. Because the free web server is so under-configured that it can't run deep learning that it cannot run Sentiment Analysis. In addition the main contributors, who still have tons of assaignments and upcoming quizzes, do not have time to write anti-block script for web crawling of musixmatch, by whom our AWS public IPs were blocked.*  

## Installation guides
to be completed...
 
## Usage
```
PillowStruck
|
│   README.md
│   cofig.yaml
│   main.py
|   requirements.txt
|   documents
└───apps
    │
    │   spotify_stare.py
    │   lyrics_rub.py
    │   lyrics_struck.py
    │   artist_struck.py
    └───[model apps]
    |
    |   app.py
    |   templates
    |   statics
    └───[web apps]
```

Users can input a keyword, PillowStruck will call Spotify APIs to get search results, results will contain "Tracks" and "Artists" pandas.DataFrames. The "Tracks" df contains features like `track name`, `release_date`, `popularity`, `artist` and `album`, and "Artists" df contains features like `artist name`, `followers` and `genres`. PillowStruck also give a choice for users to explore specific track or artist details.   

In the "Track" detail, it shows `wordcloud` and `Sentiment Analysis` of lyrics. The wordcloud uses package wordcloud to compute and visualize, while Sentiment Analysis uses package tweetnlp to compute and uses package altair to visualize. Sentiment analysis shows the sentiment label and its score.   
In the "Artist" detail, it shows the `activity degree` along years of this artist by the count of their released tracks. Also it shows airtist's `top 10 tracks` and `latest 10 albums`.  

**Run the website**  
```bash
$ cd apps
$ python app.py
```

**Search keyword**  
```python
from spotify_stare import SpotifyStare
q='David%20Bowie' #replace to your keyword
search_results = SpotifyStare(q)
artists, albums, tracks = search_results.search() # the results DataFrame of artists, albums, tracks individually.
```

**Get track lyrics**   
```python
q='David%20Bowie' #replace to your keyword
lyrics_file = get_lyrics(q) # write the lyrics in a file apps/lyrics/{Artist}_{Track}.txt
```   

**Generate track wordcloud picture and sentiment analysis**   
```python
from lyrics_struck import LyricsStruck
lyrics_analysis = LyricsStruck(lyrics_file)
lyrics_analysis.wordcloud() # wordcloud picture in apps/static/wordcloud_{Artist}_{Track}.png
lyrics_analysis.visualize_sentiment() # sentiment analysis picture in apps/static/lyrics_{Artist}_{Track}.png
```

**Generate artist activity analysis and more**  
```python
from artist_struck import ArtistStruck
ats = ArtistStruck()
at_name = ats.get_artist_track_numbers_for_years(q) # artist activity analysis  picture in apps/static/{artist}.png
pop_tracks = ats.get_artist_top_tracks_by_name(q) # get top 10 popular tracks
pop_albums = ats.get_artist_albums_by_name(q) # get latest 10 albums
```


# References

**Spotify APIs:** The Spotify APIs provides developers with a wealth of data, such as information about musicians and song albums, users' search history, song lists, and more. We can use this vast amount of data to build our own systems.    
**Musicmatch APIs and Scraping:** Musicmatch APIs mainly provide the lyrics of songs.
