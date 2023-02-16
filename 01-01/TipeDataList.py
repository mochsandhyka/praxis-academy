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

#("aris",20),("sandi",28)
a = ("aris","sandi")
b = (20,28)
zip(a,b)

append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list

