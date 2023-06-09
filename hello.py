# 세션 유지 > 세션 안에서 reuqest를 통해 데이터 긁어오기
import requests  # 동기적코드
import time


def fetcher(session, url):
    with session.get(url) as response:
        return response.text


def main():
    urls = ["https://naver.com", "https://google.com", "https://instagram.com"] * 10

    with requests.Session() as session:
        result = [fetcher(session, url) for url in urls]  # with이 파일열고 닫아줌
        print(result)


# fetcher는 해당하는 세션에 url을 보내고, 데이터를 가져옴

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)  # 12
