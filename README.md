## 楽曲リコメンドWebアプリ

### 概要

楽曲探索の課題を解決するため、Spotify APIとChatGPT APIを活用した楽曲リコメンドWebアプリを企画・開発しました。ユーザーが好きな楽曲を基に新しい音楽を発見できるアプリケーションです。

### 特徴

- Spotify APIで類似楽曲を推薦

- ChatGPT APIで楽曲の解説を表示

- AWS EC2でクラウド運用

### 使用技術

- Python（Flask、spotipy）

- Spotify API、ChatGPT API

- AWS EC2

### 操作方法

1. 楽曲・アーティスト検索指定URLを開くと「楽曲リコメンドシステム」の画面が表示されます。検索バーで楽曲やアーティストを検索してください。この画面では「ビリー・アイリッシュ」と検索しており、ユーザーは好きなアーティストや楽曲を入力できます。
| ![index_after](https://github.com/user-attachments/assets/d8bb3514-0265-4112-a042-cfd4610dd6e4) |
|:-:|

2. 検索後、5曲程度のリストが表示されます。好みの楽曲を選択し、「推薦を表示」ボタンをクリックします。検索結果には「bad guy」など、入力に基づいた関連楽曲が表示されます。この例では「BIRDS OF A FEATHER」を選択しています。
| ![search_after](https://github.com/user-attachments/assets/9abef3cf-ebce-46ed-ae87-a372abb2b13e) |
|:-:|

3. 選択した楽曲を基に、Spotify APIが類似曲を推薦し、埋め込みされたSpotifyで再生可能です。下にはChatGPTによる詳細な楽曲解説が表示され、楽曲の特徴や魅力を楽しめます。この画面では、Doja Catの「Agora Hills」が推薦されており、Spotifyの埋め込みプレイヤーで再生できます。
| ![recommend](https://github.com/user-attachments/assets/73a22409-871d-45a3-8ffd-c758991a46d7) |
|:-:|

