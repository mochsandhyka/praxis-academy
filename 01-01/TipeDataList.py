a = [1,2,3,4,5,6]
b = a[-3:]
c = [7,8,9]
d = a + c
a[0] = 0
#menambah data array
a.append(199)
a.append(2**2)
e = [a,c]
#array ke 0 1
f = e[0][1]

#lenght dari array
g = ["a","b","c","d"]

#print(len(g))

#nested list (array dalam array)
h = [a,b]
#print(h)
"""
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b
"""