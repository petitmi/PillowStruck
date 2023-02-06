
# Overview

PillowStruck uses spotify APIs and musixmatch web crawling to implement a API wrapper for analysis of specific artists, albums and tracks with pyhton.
- Group name: **PillowStruck**
- Members of the group: **Nyx Zhang, Tia Wang**  
To be more impressing on user interaction, we deployed a website on AWS with free tier: [PillowStruck](http://13.56.81.102:8080/).  

**Note:** *However, lyrics acquirement and sentiment analysis can only run on private server instead of the above web server, due to financial and time restrictions. Because the free web server is so under-configured that it can't run deep learning that it cannot run Sentiment Analysis. In addition the main contributors, who still have tons of assaignments and upcoming quizzes, do not have time to write anti-block script for web crawling of musixmatch, by whom our AWS public IPs were blocked.*

# Quick Start

## Web
<table>
<tr><th>Step 1: Search any keyword, including the "track", "artist" Object. </th> <th>Step 2: Get the results contain tracks and artists list.</th>

</tr>
<tr>
<td><img width="350" alt="image" src="https://user-images.githubusercontent.com/43694291/216788363-defccfbb-1a9f-4d71-a86d-7ec73a55e600.png">   </td>
<td><img width="350" alt="image" src="https://user-images.githubusercontent.com/43694291/216788454-f9506c73-f65f-4935-8490-7be47ae9f9eb.png">  </td>
</tr>
</table>

**Step 3.1: Click Tracks' "explore" to read track's detail, or click "home" to back to the search page. 

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

**Step 3.2:** Click Artists' "explore" to read artist detail, or click "home" to back to the search page. 
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

## Installation guides
to be completed...
 
## Usage
```
$ cd apps
$ python app.py
```

### Code structure
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
# Reference 
To be completed...

