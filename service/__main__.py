from flask import Flask, request, abort
from service.dostoevsky_recognizer import dostoevsky
from pydantic import ValidationError

import logging
logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route("/api/v1/predict", methods=['POST'])
def predict_slow():
    try:
        data = request.json
    except ValidationError as e:
        logger.info('validation issues noted')
        abort(400, str(e))

    emotion = dostoevsky(data['text'])
    logger.info('Recieved a new emotion color for this text. Sending back the data')
    return {'emotions': [emotion]}


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app.run(debug=True)
    logger.info('Emotion recogniser service started')
