from flask import Flask, request, render_template,jsonify
import spotipy
from dotenv import load_dotenv
import os
from openai import OpenAI
# from spotipy.oauth2 import SpotifyClientCredentials
from spotipy_anon import SpotifyAnon

app = Flask(__name__)

load_dotenv()  # .env の読み込み
client=OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

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
    
#推薦楽曲の解説
def song_description(song_name,artist_name):
    try:
        prompt=f"楽曲「{song_name}（アーティスト：{artist_name}）の特徴や魅力を簡潔に説明して下さい。」"
        # response = client.chat.completions.create(
        #     model="gpt-4o-mini",
        #     messages=[
        #             {"role": "system", "content": "あなたは助けになる音楽評論家です。"},
        #             # {"role": "system", "content": "ユーザーに楽曲のことについて教えて、と言われたら200字程度でレビューしてください"},
        #             {"role": "user", "content": prompt }
        #         ]
        # )
        # return response.choices[0].message.content
        return "楽曲「サニー」（アーティスト：w.o.d.）は、リズミカルなビートとキャッチーなメロディーが特徴的です。エネルギッシュなサウンドは聴く人の心を躍らせ、前向きなメッセージが込められています。特に、アーティスト独自のスタイルが反映されており、ジャンルを超えたアプローチが魅力です。歌詞の中にある温かな感情や日常の中の小さな幸せを描写することで、リスナーに共感を呼び起こします。全体的に、ポジティブな雰囲気が漂い、聴く者に明るい気持ちをもたらす楽曲です。"
    except Exception as e:
        print(f"OpenAI API Error: {e}")
        return "解説の取得に失敗しました。"

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

    if not recommendation:
            return jsonify({"error": "推薦楽曲の取得に失敗しました。"})

    song_name = recommendation['name']
    artist_name = recommendation['artist']
    
    # ChatGPT APIで解説を取得
    description = song_description(song_name, artist_name)

    return render_template('recommend.html',track=recommendation, description=description)
    # if recommendation:
    #     return render_template('recommend.html', track=recommendation)
    # else:
    #     error_message="楽曲が見つかりませんでした"
    #     return render_template('recommend.html', track=None, error=error_message)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)