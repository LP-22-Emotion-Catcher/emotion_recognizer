from flask import Flask
from recognizer import emotion_recognizer, neutral_words, negative_words, positive_words
from dostoevsky_recognizer import dostoevsky

app = Flask(__name__)

# Функция Николая с натренированной моделью
@app.route("/api/v1/predict/slow", methods = ['GET'])
def predict_slow():
    return dostoevsky('Она любит шоколадки. Я точно знаю!')

# Функция Дмитрия, дописанная слегка
@app.route("/api/v1/predict/fast", methods = ['GET'])
def predict_fast():
    return emotion_recognizer('Она любит шоколадки. Я точно знаю!', neutral_words, negative_words, positive_words)


if __name__ == '__main__':
    app.run()#host='0.0.0.0'