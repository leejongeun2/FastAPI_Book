# 웹 크롤링: 검색 엔진의 구축 등을 위해 특정한 방법으로 웹 페이지를 수집하는 프로그래밍
# 웹 스크래핑: 웹에서 데이터를 수집하는 프로그램
# 둘이 비슷한 의미

from bs4 import BeautifulSoup


soup = BeautifulSoup(html_doc, "html.parser")
# html해석해서 가공해서 사용할 수 있도록
