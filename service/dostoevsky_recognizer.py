from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel

def dostoevsky(data):
    tokenizer = RegexTokenizer()
    tokens = tokenizer.split('всё очень плохо')
    model = FastTextSocialNetworkModel(tokenizer=tokenizer)
    messages = []
    messages.append(data)
    
    results = model.predict(messages, k=5)
    
    for message, sentiment in zip(messages, results):
        return(f'{max(sentiment, key=sentiment.get)}')

