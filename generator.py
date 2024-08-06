l = ["Good morning", "Good afternoon", "Good night"]

for i in l:
    print(i)

print("*************************")


def greeting():

    yield "Good morning"
    for i in range(10000):
        print(i)
    yield "Good afternoon"
    for i in range(10000):
        print(i)
    yield "Good night"


for g in greeting():
    print(g)

print("*************************")

g = greeting()
print(next(g))

print("@@@@@")

print(next(g))

print("@@@@@")
print(next(g))

print("@@@@@")

print("*************************")


def counter(num=10):
    for _ in range(num):
        yield 'run'


g = greeting()
c = counter()

print(next(g))

print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print(next(g))

print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print(next(g))
