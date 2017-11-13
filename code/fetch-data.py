import feedparser
import json

def main():
    with open('feeds.json','r') as fp:
        feeds = json.load(fp)['feeds']

    d = []
    for feed in feeds:
        t = feedparser.parse(feed['url'])
        t['name'] = feed.get('name')
        t.pop('bozo_exception', None)
        d.append(t)
    #d = [(feed['name'], feedparser.parse(feed['url'])) for feed in feeds]

    with open('data.json', 'w+') as fp:
        json.dump(d, fp)

if __name__ == "__main__":
    main()
