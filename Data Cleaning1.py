import re
from konlpy.tag import Okt

# KoNLPy를 초기화합니다.
okt = Okt()

# 예시로 사용할 한국어 텍스트 데이터
korean_text = "한국어 텍스트 데이터를 전처리하는 예시 코드입니다. 특수 문자나 숫자는 제거하고, 불용어도 제거합니다."

# 문장을 토큰화하고 불용어를 제거하는 함수
def preprocess_korean_text(text):
    # 한국어 문장을 띄어쓰기 단위로 토큰화합니다.
    tokens = okt.morphs(text)
    
    # 특수 문자와 숫자를 제거하고, 한 글자 단어도 제거합니다.
    tokens = [re.sub(r'[^ㄱ-ㅎ가-힣a-zA-Z]', '', token) for token in tokens if len(token) > 1]
    
    # 불용어를 제거하고, 모든 단어를 소문자로 변환합니다.
    stopwords = ["하고","하는", "합니다", "입니다","을", "를", "이", "가", "은", "는", "의"]  # 불용어 사전을 자신의 필요에 맞게 확장하세요.
    tokens = [token.lower() for token in tokens if token not in stopwords]
    
    # 전처리된 문장을 반환합니다.
    preprocessed_text = " ".join(tokens)
    return preprocessed_text

# 전처리된 결과를 출력합니다.
preprocessed_text = preprocess_korean_text(korean_text)
print(preprocessed_text)