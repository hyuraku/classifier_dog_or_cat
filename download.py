from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os
import time
import sys

from config import config

# APIの情報
key = config.key
secret = config.secret
wait_time = 1

animalname = sys.argv[1]
savedir = "./{}".format(animalname)

flickr = FlickrAPI(key, secret, format="parsed-json")
result = flickr.photos.search(
    text=animalname,
    per_page=400,
    madia='photos',
    sort='relevance',
    safe_search=1,
    extras='url_q,licence'
)

photos=result['photos']
# pprint(photos)
for i ,photo in enumerate(photos['photo']):
    url_q=photo['url_q']
    filepath=savedir+"/"+photo["id"]+".jpg"
    if os.path.exists(filepath): continue
    urlretrieve(url_q,filepath)
    time.sleep(wait_time)
