import feedparser
import json
import time


def main():
    while(True):
        with open('feeds.json','r') as fp:
            feeds = json.load(fp)['feeds']

        d = []
        for feed in feeds:
            t = feedparser.parse(feed['url'])
            t['name'] = feed.get('name')
            t.pop('bozo_exception', None)
            d.append(t)
        #d = [(feed['name'], feedparser.parse(feed['url'])) for feed in feeds]

        with open('/shared/data.json', 'w+') as fp:
            json.dump(d, fp)
        time.sleep(5 * 60)

if __name__ == "__main__":
    main()
