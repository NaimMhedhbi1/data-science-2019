import urllib.request as urllib
import urllib3
import json
import datetime
import csv
import time

app_id = "145282886794640"
app_secret = "7cc260766b0b2cbeb93241caf048d980" # DO NOT SHARE WITH ANYONE!

access_token = app_id + "|" + app_secret
#page_id = '88036787794'
page_id = 'Nessma'

def testFacebookPageData(page_id, access_token):
    
    # construct the URL string
    base = "https://graph.facebook.com/v2.4"
    node = "/" + page_id
    parameters = "/?access_token=%s" % access_token
    url = base + node + parameters
    
    # retrieve data
    req = urllib.Request(url)
    response = urllib.urlopen(req)
    data = json.loads(response.read())
    print (json.dumps(data, indent=4, sort_keys=True))
    

testFacebookPageData(page_id, access_token)
