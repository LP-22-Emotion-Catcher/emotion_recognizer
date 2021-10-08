# poetry add dostoevsky
# python -m dostoevsky download fasttext-social-network-model
from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel

def dostoevsky(data):
    tokenizer = RegexTokenizer()
    tokens = tokenizer.split('всё очень плохо')  # [('всё', None), ('очень', None), ('плохо', None)]
    model = FastTextSocialNetworkModel(tokenizer=tokenizer)
    messages = []
    messages.append(data)
    
    results = model.predict(messages, k=5)
    
    for message, sentiment in zip(messages, results):
    # привет -> {'speech': 1.0000100135803223, 'skip': 0.0020607432816177607}
    # люблю тебя!! -> {'positive': 0.9886782765388489, 'skip': 0.005394937004894018}
    # малолетние дебилы -> {'negative': 0.9525841474533081, 'neutral': 0.13661839067935944}]
    #print(message, '->', sentiment)
        #print(message,end='\n\n')
        return(f'Сообщение: {message} <br> Эмоциональная окраска: {max(sentiment, key=sentiment.get)}')#,  величина: {sentiment[max(sentiment, key=sentiment.get)]}')

