import re
from konlpy.tag import Okt

# KoNLPy를 초기화합니다.
okt = Okt()

# 예시로 사용할 한국어 텍스트 데이터
korean_text = "한국어 텍스트 데이터를 전처리하는 예시 코드입니다. 특수 문자나 숫자는 제거하고, 불용어도 제거합니다."

# 문장을 토큰화하고 불용어를 제거하는 함수
def preprocess_korean_text(text):

    tokens = okt.morphs(text)

    tokens = [re.sub(r'[^ㄱ-ㅎ가-힣a-zA-Z]', '', token) for token in tokens if len(token) > 1]

    stopwords = ["하고","하는", "합니다", "입니다","을", "를", "이", "가", "은", "는", "의"]
    tokens = [token.lower() for token in tokens if token not in stopwords]

    preprocessed_text = " ".join(tokens)
    return preprocessed_text

# 전처리된 결과를 출력
preprocessed_text = preprocess_korean_text(korean_text)
print(preprocessed_text)
