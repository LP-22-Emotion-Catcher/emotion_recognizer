from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel
from service.config import RELEVANT_EMOTION_THRESHOLD, DIFF_SCORE_THRESHOLD


def dostoevsky(msg):
    tokenizer = RegexTokenizer()
    model = FastTextSocialNetworkModel(tokenizer=tokenizer)
    result = model.predict([msg], k=5)
    positive = result[0]['positive']
    negative = result[0]['negative']
    diff_score = abs(positive - negative)
    if positive > negative:
        if diff_score < float(DIFF_SCORE_THRESHOLD):
            score = float(f'{positive:.3f}')
            if score < float(RELEVANT_EMOTION_THRESHOLD):
                return
            return(['positive', score])
        else:
            score = float(f'{negative:.3f}')
            if score < float(RELEVANT_EMOTION_THRESHOLD):
                return
            return(['negative', score])
    else:
        score = float(f'{negative:.3f}')
        if diff_score < float(DIFF_SCORE_THRESHOLD):
            score = float(f'{negative:.3f}')
            if score < float(RELEVANT_EMOTION_THRESHOLD):
                return
            return(['negative', score])
        else:
            score = float(f'{positive:.3f}')
            if score < float(RELEVANT_EMOTION_THRESHOLD):
                return
            return(['positive', score])
