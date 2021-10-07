from flask import Flask
from recognizer import emotion_recognizer

app = Flask(__name__)

@app.route("/api/v1/predict", methods = ['POST'])
def predict():
    return emotion_recognizer('Привет, это прекрасный продукт, рекоммендую !')

if __name__ == '__main__':
    app.run(host='0.0.0.0')