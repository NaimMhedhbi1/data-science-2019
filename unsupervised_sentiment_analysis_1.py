#https://www.kdnuggets.com/2018/08/emotion-sentiment-analysis-practitioners-guide-nlp-5.html
import nltk
nltk.download()
import pandas as pd
from nltk.corpus import sentiwordnet as swn
df = pd.read_excel('C:/Users/Naim/Desktop/scraped_data/nessma_comments.xlsx')
df['message']=df['message'].apply(str)
article1 = nltk.corpus.gutenberg.words('C:/Users/Naim/Desktop/.spyder-py3/text1.txt')



def predict_sentiment(article):
    article = nltk.word_tokenize(article)
    
    tagged_text = nltk.pos_tag(article)
    pos_score = neg_score = token_count = obj_score = 0
    for word, tag in tagged_text:
        word = word.lower()
        tag_list = ['NN', 'VB', 'JJ', 'RB']
        if tag not in tag_list:
            continue

        ss_set = list(swn.senti_synsets(word))
        if len(ss_set) == 0:
            continue

        ss_set = ss_set[0]

        pos_score += ss_set.pos_score()
        neg_score += ss_set.neg_score()
        obj_score += ss_set.obj_score()
        token_count += 1

    # aggregate final scores
    final_score = pos_score - neg_score
    norm_final_score = round(float(final_score) / token_count, 2)
    norm_obj_score = round(float(obj_score) / token_count, 2)
    norm_pos_score = round(float(pos_score) / token_count, 2)
    norm_neg_score = round(float(neg_score) / token_count, 2)

    return norm_obj_score, norm_pos_score, norm_neg_score, norm_final_score

predict_sentiment(article1)
