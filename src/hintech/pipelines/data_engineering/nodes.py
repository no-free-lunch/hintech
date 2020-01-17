import  pandas as pd
from nltk.corpus import stopwords
import string
import re

stop = set(stopwords.words('english'))
def word_count(text: str):
    try:
        text = text.lower()
        regex = re.compile('[' + re.escape(string.punctuation) + '0-9\\r\\t\\n]')
        txt = regex.sub(" ", text)
        # tokenize
        # words = nltk.word_tokenize(clean_txt)
        # remove words in stop words
        words = [w for w in txt.split(" ") \
                 if not w in stop and len(w) > 3]
        return len(words)
    except:
        return 0


def preprocess_train(train: pd.DataFrame) -> pd.DataFrame:
    train['desc_len'] = train['item_description'].apply(word_count)
    return train
