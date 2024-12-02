class Book:
    def __init__(self, titel, author, price):
        self.titel = titel
        self.author = author
        self.price = price

    def display_info(self):                                        #출력하는 메서드
        print("titel   = ", self.titel)
        print("author   = ", self.author)
        print("price   = ", self.price)

    def __eq__(self, other):
        if self.price == other.price:                               #내 책 가격이랑 다른책 가격 비교
            print(True)
        else:
            print(False)



book1 = Book("aaaa","bbbb",4000)                #정보를 입력하는
book2 = Book("cccc", "ddddd", 7890)
book1.display_info
book2.display_info                                                 #  나 이 기능 쓸게? 이런 뜻

print(book1 == book2)                                                  #이건 왜 실행이 안되노....

