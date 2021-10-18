from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel


def dostoevsky(msg):
    tokenizer = RegexTokenizer()
    model = FastTextSocialNetworkModel(tokenizer=tokenizer)
    result = model.predict([msg], k=5)
    for message, sentiment in zip([msg], result):
        return(f'{max(sentiment, key=sentiment.get)}')
