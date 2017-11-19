import feedparser
import json
import time
import logging
import sys
from os import walk, chdir

def main():
    minutes = int(sys.argv[1])
    # setup log
    logging.basicConfig(filename=sys.argv[0].split('.py')[0]+'.log', format='%(asctime)s %(message)s', level=logging.INFO)



    chdir('/feedlists')

    while(True):

        files = []
        for (dirpath, dirnames, filenames) in walk('./'):
            files.extend(filenames)
            break

        # each f is a file containing a list of feeds
        for f in files:
            with open(f,'r') as fp:
                try:
                    feeds = json.load(fp)['feeds']
                except ValueError:
                    continue

            # make list of all parsed feeds
            d = []
            for feed,i in zip(feeds, range(1,len(feeds)+1)):
                # download the content
                t = feedparser.parse(feed.get('url'))
                # add name
                t['name'] = feed.get('name')
                # add sitelink
                t['site'] = feed.get('site')
                # add an id 
                t['id'] = i
                # remove stuff that crashes the json parser
                t.pop('bozo_exception', None)
                d.append(t)

            # write the data to the /shared directory with a '_data.json' postfix
            with open('/shared/'+f.split('.json')[0]+'_data.json', 'w+') as fp:
                json.dump(d, fp)
            
        logging.info('')
        time.sleep(minutes * 60)


if __name__ == "__main__":
    main()
