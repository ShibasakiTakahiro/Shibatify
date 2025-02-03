from flask import Flask, request, render_template
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy_anon import SpotifyAnon

app = Flask(__name__)

# Spotify APIの認証設定
# client_id = '74922f440a8a4df6911f8e367923222b'  # ここにあなたのクライアントIDを入力
# client_secret = '97601c685ab9417da4e3d1904d308f6a'  # ここにあなたのクライアントシークレットを入力
# sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

sp = spotipy.Spotify(auth_manager=SpotifyAnon())
def search_tracks(query):
    results = sp.search(q=query, type='track', limit=5)
    tracks = results['tracks']['items']
    return [{'name': track['name'], 'id': track['id'], 'artist': track['artists'][0]['name'],'album_art': track['album']['images'][0]['url']} for track in tracks]

# 類似楽曲の推薦
def recommend_tracks(seed_track):
    recommendations = sp.recommendations(seed_tracks=[seed_track], limit=1)
    if recommendations['tracks']:
        track = recommendations['tracks'][0]
        return {'name': track['name'], 'artist': track['artists'][0]['name'], 'id': track['id']}
    else:
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    tracks = search_tracks(query)
    return render_template('search.html', tracks=tracks)

@app.route('/recommend', methods=['POST'])
def recommend():
    selected_track = request.form.get('selected_track')
    if not selected_track:
        error_message = "1曲を選択してください。"
        return render_template('search.html', tracks=[], error=error_message)
    recommendation = recommend_tracks(selected_track) # 推薦された楽曲の情報を取得
    if recommendation:
        return render_template('recommend.html', track=recommendation)
    else:
        error_message="楽曲が見つかりませんでした"
        return render_template('recommend.html', track=None, error=error_message)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)