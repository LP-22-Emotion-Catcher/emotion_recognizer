from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel

def dostoevsky(msg):
    emotion_thresold = 2.0
    tokenizer = RegexTokenizer()
    model = FastTextSocialNetworkModel(tokenizer=tokenizer)
    result = model.predict([msg], k=5)
    for message, sentiment in zip([msg], result):
        positive = sentiment['positive']
        negative = sentiment['negative']
        if negative * emotion_thresold < positive:
            return 'positive'
        elif positive * emotion_thresold < negative:
            return 'negative'
        else:
            return 'neutral'