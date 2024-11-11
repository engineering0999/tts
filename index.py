from flask import Flask, request, send_file
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/tts', methods=['POST'])
def text_to_speech():
    text = request.json.get('text')
    if text:
        tts = gTTS(text=text, lang='te')
        audio_file = 'output.mp3'
        tts.save(audio_file)
        return send_file(audio_file, as_attachment=True)
    else:
        return {"error": "Please provide some text."}, 400

if __name__ == '__main__':
    app.run(debug=True)
