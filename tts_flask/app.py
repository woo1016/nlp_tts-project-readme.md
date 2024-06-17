from flask import Flask, render_template, request, jsonify
import boto3
import os
from io import BytesIO

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/synthesize', methods=['POST'])
def synthesize():
    text = request.form['text']
    polly_client = boto3.client('polly')
    response = polly_client.synthesize_speech(
        Text=text,
        OutputFormat='mp3',
        VoiceId='Seoyeon'
    )

    # MP3 데이터를 메모리에 저장하고 재생 가능한 URL로 변환
    audio_stream = response['AudioStream'].read()
    audio_url = save_audio(audio_stream)
    return jsonify({'audio_url': audio_url})

def save_audio(audio_stream):
    # 바이너리 데이터를 static 폴더에 저장
    audio_path = 'static/audio.mp3'
    with open(audio_path, 'wb') as file:
        file.write(audio_stream)
    return audio_path

if __name__ == '__main__':
    app.run(debug=True)