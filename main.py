from codes.spotify_stare import *

def main():
    s = SpotifyStare()
    result = s.search(type = 'artist', q='the%201975')
    print(result.json())

if __name__ == '__main__':
    main()