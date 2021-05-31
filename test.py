###
# 리디북스 베스트셀러 크롤링하기
###

# requests : 요청해서 txt를 가져오는 라이브러리
import requests

# BeautifulSoup : 크롤링 한 txt를 보기 편하게 가공
from bs4 import BeautifulSoup

# 타겟 url
url = 'https://ridibooks.com/category/new-releases/2200'
response = requests.get(url)
response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'html.parser')

# 크롤링한 데이터의 title_text 클래스를 선택
bookservices = soup.select('.title_text')

# enumerate 넘버링해서 출력해주는 built-in function
# strip() 앞, 뒤 공백을 없애줌
for no, book in enumerate(bookservices, 1):
    print(no, book.text.strip())
