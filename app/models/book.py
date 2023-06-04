from odmantic import Model


# 하나의 데이터
class BookModel(Model):
    keyword: str
    publisher: str
    price: int
    image: str

    class Config:
        collection = "books"
