import nltk
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import re
translator = str.maketrans('', '', string.punctuation)
stemmer = PorterStemmer()
stop_words = set(stopwords.words("english"))
def data_preprocessing(data):
    data = data.lower()
    data = re.sub(r'\d+', '', data)
    data = data.translate(translator)
    data = " ".join(data.split())
    data = word_tokenize(data)
    stem = [stemmer.stem(word) for word in data]
    data = [word for word in stem if word not in stop_words]
    # return data #The return type is list of words. And not  a sentence, I have not changed it for a purpose.
    ans = " ".join(data)
    return ans