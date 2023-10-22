# 2주차 데이터 정제 & 시각화

1. 데이터 수집

어떤 내용의 노래를 자주 듣는지 궁금하여 평소 즐겨듣는 playlist의 노래 20개의 가사를 txt 파일로 저장

2. 한국어 데이터 전처리

- 처음에 txt 파일을 제대로 읽어오지 못해 노래 하나의 가사를 직접 입력하여 전처리를 시도

      import re
      from konlpy.tag import Okt
      import matplotlib.pyplot as plt
      from wordcloud import WordCloud
      from collections import Counter
      import numpy as np
      from PIL import Image

      okt = Okt()

      playlist = """인스타로 몰래 보는 너의 하루들 누가 봐도 헤어진 티를 내 팔로우 다 끊고서 좋아요는 왜 눌렀니? 참 바보 같은 사람이야

      잘 먹지도 못하는 술은 왜 매일 마시고 늘 예쁜 얼굴 많이 야위었어

      혼자 있으면 나도 그래 술이 없으면 못 자고 많이 괴로워해 이럴 거면 우리 미친 척하고 다시 만날까 봐 다시 시작할까 봐

      친구들 만나는 거 그렇게 좋아하면서 집에만 있니, 더 우울하게

      혼자 있으면 나도 그래 누구도 만나기 싫어 숨고만 싶은데 이럴 거면 우리 미친 척하고 다시 만날까 봐 다시 시작할까 봐 워우워

      못 잊을 거야 너와 추억한 지난날들을 난 아직까지도 너무나 선명해 워어 그렇게 선명한 만큼 (선명한 만큼) 지키고픈 우리 기억들이 잊혀지는 게 정말 많이 두려워

      혼자 있으면 나도 그래 늘 혼자 센척했지만 많이 두려워해 이럴 거면 우리 (우리) 미친 척하고 다시 만날까 봐 다시 시작할까 봐

      우리 여기서 끝나면 안 돼
      """

      def preprocess_text(text):
          tokens = okt.morphs(text)

          tokens = [re.sub(r'[^ㄱ-ㅎ가-힣a-zA-Z]', '', token) for token in tokens if len(token) > 1]

          stopwords = ["을", "를", "이", "가", "은", "는", "의"]
          tokens = [token.lower() for token in tokens if token not in stopwords]

          preprocessed_text = " ".join(tokens)
          return preprocessed_text

      preprocesstext = preprocess_text(playlist)
      c = Counter(preprocesstext.split())


3. 단어별 빈도 count 후 wordcloud로 시각화

-가사 20개를 저장한 txt 파일을 전처리 후 wordcloud로 시각화

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

![myplaylistlyrics](https://github.com/mhg337/-2-Data-Cleaning-and-Text-Preprocessing/assets/144089001/072622a4-09b2-4c72-8f65-5bcbbf4f0a15)
