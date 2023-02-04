.. _overview:
# Overview
========
PillowStruck uses spotify APIs and musixmatch web crawling to implement a API wrapper for analysis of specific artists, albums and tracks with pyhton.
- Group name: **PillowStruck**
- Members of the group: **Nyx Zhang, Tia Wang**

And to be more impressing on user interaction, we deployed a website on AWS with free tier: [PillowStruck](http://13.56.81.102:8080/).
<img width="800" alt="image" src="https://user-images.githubusercontent.com/43694291/216788268-4cbf6bcf-c458-4b39-9fee-66d0c9518552.png">


# Quick Start
========
## Web
Step 1: Search any keyword, including the "track", "artist" Object.
<img width="800" alt="image" src="https://user-images.githubusercontent.com/43694291/216788363-defccfbb-1a9f-4d71-a86d-7ec73a55e600.png">
Step 2: Get the results contain tracks and artists list. 
<img width="800" alt="image" src="https://user-images.githubusercontent.com/43694291/216788454-f9506c73-f65f-4935-8490-7be47ae9f9eb.png">
Step 3.1:Click Tracks' "explore" to read track's detail, or click "home" to back to the search page.
     3.1.1: lyrics word cloud 
     ![image](https://user-images.githubusercontent.com/43694291/216788712-2865711e-697b-4e98-97e0-0f394f083157.png)
     3.1.2: sentiment analysis
     ![image](https://user-images.githubusercontent.com/43694291/216788726-4a1272fb-e26c-4fa2-bb47-ae76515223a1.png)
     3.1.2: lyrics txt detail
     <img width="800" alt="image" src="https://user-images.githubusercontent.com/43694291/216788565-70abbff6-892c-4e9f-9d28-5297cf1d9158.png">
Step 3.2: Click Artists' "explore" to read artist detail, or click "home" to back to the search page.
     3.2.1: artist activity analysis
     ![image](https://user-images.githubusercontent.com/43694291/216788666-0fed05a5-3165-459a-bd9a-2a0a341ad461.png)
     3.2.2: Top tracks list
     <img width="800" alt="image" src="https://user-images.githubusercontent.com/43694291/216788686-3ce4a52f-19f7-445c-930c-61b05a0a7bc5.png">
     3.2.3: latest album list
     <img width="800" alt="image" src="https://user-images.githubusercontent.com/43694291/216788705-4946936d-0a6d-47ac-8af0-9ae10fa5d428.png">

## API Wrapper
### Installation guides



```
PillowStruck
|
│   README.md
│   cofig.yaml
│   main.py
|   requirements.txt
|
└───app
    │   extract input keywords
    │   web crawl the lyrics
    │   get the spotify features
    │   analyze artist
    │   analyze track lyrics 
    │
    └───computation|
    |
    |   apps
    |   templates
    |   statics
    └───web│
```
# Reference 
========
To be completed...

# Releases
========
To be completed...


