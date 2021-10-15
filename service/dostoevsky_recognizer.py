from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel
from service.config import EMOTION_THRESHOLD

def dostoevsky(msg) -> str:
    emotion_threshold = float(EMOTION_THRESHOLD) #if recognition result exceed it will return positive or negative. Else return negative
    tokenizer = RegexTokenizer()
    model = FastTextSocialNetworkModel(tokenizer=tokenizer)
    result = model.predict([msg], k=5)
    for emotion in result[0]:
        if emotion == 'positive' or emotion == 'negative':
            score = result[0][emotion]
            if score >= emotion_threshold:
                return(emotion)
            return(f'low level {emotion}')
        else: 
            continue
