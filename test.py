import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

my_id ='74922f440a8a4df6911f8e367923222b' #client ID
my_secret = '5d4097fa4e244851bbdbb989dfb5d6ae' #client secret
ccm = SpotifyClientCredentials(client_id = my_id, client_secret = my_secret)
spotify = spotipy.Spotify(client_credentials_manager = ccm)
results = spotify.artist_top_tracks(lz_uri)

for track in results['tracks'][:10]:
    print('track    : ', track['name'])
    print('audio    : ',track['preview_url'])
    print('cover art: ' ,track['album']['images'][0]['url'])
    print()