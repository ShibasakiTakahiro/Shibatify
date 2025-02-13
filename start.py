import spotipy
from spotipy_anon import SpotifyAnon

sp = spotipy.Spotify(auth_manager=SpotifyAnon())

results = sp.search(q='weezer', limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])