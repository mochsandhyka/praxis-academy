a = len("string")
b = "don\'t"
c = "\"Yes\",they said"
d = "c:yui\name"
e = r"c:yui\name"
f = """\
selamat
    menunaikan
     ibadah
    puasa"""

g = 3 * "wa" + "hing"
h = "Py" "thon"
i = h + " 3.01"
j = "Python"

#from left
print(j[0])

#from right
print(j[-1])

#from 0 to 2(Exclude)
print(j[0:2])

#from begining to position 2(ex)
print(j[:2])

#from 2 to end
print(j[2:])

#from 2 terakhir to end
print(j[-2:])

k = 256 * 2
print("The value of k is",k)

l = f"{b} let your mother gone"
m = "{0} let your mother gone".format(b)
 
print(m,l)