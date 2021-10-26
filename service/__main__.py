from flask import Flask, request
from service.dostoevsky_recognizer import dostoevsky

app = Flask(__name__)


@app.route("/api/v1/predict", methods=['POST'])
def predict_slow():
    data = request.json
    print(data)
    emotion = dostoevsky(data['text'])
    print(emotion)
    return {'emotions': [emotion]}


if __name__ == '__main__':
    app.run(debug=True)
