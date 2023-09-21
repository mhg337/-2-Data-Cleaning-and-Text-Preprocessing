from bs4 import BeautifulSoup
import re

data = "<p>초등학교 입학을 축하합니다.~~~^^;<br/></p>"
soup = BeautifulSoup(data, "lxml")
remove_tag = soup.get_text()
result_text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》;]', '', remove_tag)
print(result_text)

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

# NLTK의 문장 토큰화
nltk.download('punkt')  # 필요한 데이터 다운로드

text = "NLTK는 자연어 처리를 위한 강력한 라이브러리입니다. 문장과 단어 토큰화가 가능합니다."
sentences = sent_tokenize(text)  # 문장 토큰화
words = word_tokenize(text)  # 단어 토큰화

print("문장 토큰화 결과:", sentences)
print("단어 토큰화 결과:", words)
