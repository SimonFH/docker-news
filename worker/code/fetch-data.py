import feedparser
import json
import time
import logging
import sys

def main():
    minutes = int(sys.argv[1])
    # setup log
    logging.basicConfig(filename=sys.argv[0].split('.py')[0]+'.log', format='%(asctime)s %(message)s', level=logging.INFO)
    
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
        
        logging.info('')
        time.sleep(minutes * 60)

if __name__ == "__main__":
    main()
