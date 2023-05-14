import requests  # 동기적코드
import time
import os  # 현재 프로세스 id  / 스레드
import threading


def fetcher(session, url):
    print(f"{os.getpid()} process | {threading.get_ident()} url : {url}")
    with session.get(url) as response:
        return response.text


def main():
    urls = ["https://google.com", "https://apple.com"] * 50

    with requests.Session() as session:
        result = [fetcher(session, url) for url in urls]  # with이 파일열고 닫아줌
        print(result)


# fetcher는 해당하는 세션에 url을 보내고, 데이터를 가져옴

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)  # 12
