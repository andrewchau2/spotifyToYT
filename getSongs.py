import spotipy
import secret
from spotipy.oauth2 import SpotifyOAuth

def getSpotifySongs(spotPlaylistID):
    ########################################
    #Advanced Options

    fileLoc = "songs.txt"
    ########################################

    acc = ["user-library-read", "playlist-read-private"]

    #Replace your spotify key here
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id= secret.SpotifySecret().spotID,
                                                   client_secret=secret.SpotifySecret().spotSEC,
                                                   redirect_uri=secret.SpotifySecret().spotRED,
                                                   scope=acc))



    playlists = sp.playlist_items(playlist_id=spotPlaylistID)
    ofstrm = open(fileLoc,'w',encoding='utf-8')

    for idx, item in enumerate(playlists['items']):
       track = item['track']
       ofstrm.write(track['artists'][0]['name'] +  " " + track['name'] + '\n')

    ofstrm.close()
    print("Songs parsed and saved to", fileLoc)
