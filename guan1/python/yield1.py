def f():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


a = f()
for i in range(10):
    print(a.__next__(), end=' ')
