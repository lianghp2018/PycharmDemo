def test(a):
    print(a)
    print(id(a))

    a += a
    print(a)
    print(id(a))


# 不可变
b = 100
test(b)

# 可变
c = [11, 22]
test(c)
