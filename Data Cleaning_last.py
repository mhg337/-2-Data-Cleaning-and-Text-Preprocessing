import re
from konlpy.tag import Okt
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
import numpy as np
from PIL import Image

okt = Okt()

file_path = r'C:\Users\PC\OneDrive\문서\GitHub\Data-Cleaning-and-Text-Preprocessing\lyric.txt'
with open(file_path, "r", encoding="utf-8") as file:
    playlist = file.read()

def preprocess_text(text):
    tokens = okt.morphs(text)
    
    tokens = [re.sub(r'[^ㄱ-ㅎ가-힣a-zA-Z]', '', token) for token in tokens if len(token) > 1]

    stopwords = ["을", "를", "이", "가", "은", "는", "의"]
    tokens = [token.lower() for token in tokens if token not in stopwords]

    preprocessed_text = " ".join(tokens)
    return preprocessed_text

preprocesstext = preprocess_text(playlist)
c = Counter(preprocesstext.split())

wc = WordCloud(font_path='malgun', width=400, height=400, scale=2.0, max_font_size=250)
gen = wc.generate_from_frequencies(c)
plt.figure()
plt.imshow(gen)
wc.to_file('myplaylistlyrics.png')