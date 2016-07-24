# Uses Spotipy to authenticate and change to desired playlist, offline mode, shuffle. shell script changes volume for game voice
import os
import sys
import spotipy
import spotipy.util as util
import pprint
import simplejson as json
#SPOTIPY_CLIENT_ID = '316f236d1d004db48b3a024feb4b279a'
#SPOTIPY_REDIRECT_URI = '7f952e500196404db61a3c198bebcdb7'
#export SPOTIPY_REDIRECT_URI='your-app-redirect-url'


#runs shell script
#os.system('./dotaGame.sh')


# Shows the top artists for a user

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

scope = 'user-top-read'
token = util.prompt_for_user_token(username, scope, client_id='316f236d1d004db48b3a024feb4b279a', client_secret='7f952e500196404db61a3c198bebcdb7', redirect_uri='127.0.0.1/callback')

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    ranges = ['short_term', 'medium_term', 'long_term']
    for range in ranges:
        print "range:", range
        results = sp.current_user_top_artists(time_range=range, limit=50)
        for i, item in enumerate(results['items']):
            print i, item['name']
        print
else:
    print("Can't get token for", username)