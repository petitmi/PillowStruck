from search import *

def main():
    s = Searcher()
    result = s.search(type = 'artist', q='the%201975')
    print(result.json())

if __name__ == '__main__':
    main()