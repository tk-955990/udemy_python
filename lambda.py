# lambda式

l = ["Mon", "tue", "Wed", "Thu", "fri", "sat", "Sun"]

# リスト内の要素を出力


def change_words(words, func):
    for word in words:
        print(func(word))

# lambda式を使わない場合

# 最初の文字を大文字に変換する関数
# def sample_func(word):
#     return word.capitalize()

# change_words(l, sample_func)


# lambda式を使用した場合
# lambda 引数: 戻り値(関数)

change_words(l, lambda s: s.capitalize())


# def counter(num=10):
#     for _ in range(num):
#         yield 'run'


# def greeting():

#     yield "Good morning"
#     yield "Good afternoon"
#     yield "Good night"


# g = greeting()
# c = counter()

# print(next(g))

# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))

# print(next(g))

# print(next(c))
# print(next(c))

# print(next(g))

# print(next(c))
# print(next(c))
# print(next(c))
