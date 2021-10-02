def emotion_recognizer(text):
    import pandas as pd
    words_df = pd.read_csv('kartaslovsent.csv', encoding = 'utf-8', sep=';')
    words_df = words_df[['term', 'tag', 'pstv', 'ngtv', 'neut']]

    negative_words = words_df[words_df['tag'] == 'NGTV']
    negative_words = negative_words.sort_values(by='ngtv', ascending = False)
    positive_words = words_df[words_df['tag'] == 'PSTV']
    positive_words = positive_words.sort_values(by='pstv', ascending = False)
    neutral_words = words_df[words_df['tag'] == 'NEUT']
    neutral_words = neutral_words.sort_values(by='neut', ascending = False)

    '''Принимает текст, оценивает его эмоциональную окраску.
    Возвращает positive/negative/neutral'''
    
    negative_color, positive_color, neutral_color = 0, 0, 0
    text = text.lower()
    text = text.strip(',').split(' ')
    for word in text:
        if len(word) < 3: #чтобы исключить союзы и предлоги
            continue
        for check_word in list(negative_words['term']):
            if word in check_word: 
                negative_color +=1
                continue
        for check_word in list(positive_words['term']):
            if word in check_word: 
                positive_color +=1
                continue
        for check_word in list(neutral_words['term']):
            if word in check_word: 
                neutral_color +=1
                continue
                
    if negative_color > positive_color and negative_color > neutral_color:
        return 'negative'
    elif positive_color > negative_color and positive_color > neutral_color:
        return 'positive'
    elif neutral_color > negative_color and neutral_color > positive_color:
        return 'neutral'