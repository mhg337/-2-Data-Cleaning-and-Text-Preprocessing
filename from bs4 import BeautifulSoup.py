from bs4 import BeautifulSoup
import re

data = "<p>초등학교 입학을 축하합니다.~~~^^;<br/></p>"
soup = BeautifulSoup(data, "lxml")
remove_tag = soup.get_text()
result_text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》;]', '', remove_tag)
print(result_text)