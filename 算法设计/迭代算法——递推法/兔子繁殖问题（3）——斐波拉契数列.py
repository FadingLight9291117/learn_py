'''
    算法3：无需引入第三个变量c
'''
a = 1
b = 1
print(a)
print(b)
for i in range(5):
    a = a+b
    print(a)
    b = a+b
    print(b)
