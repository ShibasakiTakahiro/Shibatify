from flask import Flask, render_template, request, jsonify
from openai import OpenAI 
import os
app = Flask(__name__)

client=OpenAI(api_key = "OPENAI_API_KEY")


@app.route('/')
def index():
    return render_template('index.html')

@app.route("/send-message", methods=["POST"])
def send_message():
    user_input = request.json.get("user_input")

    # ユーザーのメッセージをChatGPTに送信
    prompt = f"ユーザー: {user_input}\nボット:"

    # response = openai.Completion.create(
    #     model="text-davinci-003",
    #     prompt=prompt,
    #     temperature=0.7,
    #     max_tokens=150
    # )
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
            {"role": "system", "content": "あなたは助けになるアシスタントです。"},
            {"role": "system", "content": "ユーザーに挨拶されたら、最初にニックネームを聞いてください。"},
            {"role": "user", "content": user_input }
        ]
    # messages=[{"role": "user", "content": user_input }]
    # messages=[{"role": "user", "content": "Hello, how are you?"}]

    )

    # ChatGPTの応答を取得
    # bot_response = response.choices[0].text.strip()
    bot_response = response.choices[0].message.content
    # bot_response=response["choices"][0]["message"]["content"]

    return jsonify({"bot_response": bot_response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)