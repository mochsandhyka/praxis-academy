#LIST
#dapat diakses melalui indeks
#slicing data misal ditampilkan dari data ke 2 - 3
#dapat menambah atau menghapus data melalui indeks atau tidak
#menambahkan dengan perintah list.append
listAngka = [1,2,3,16]
#merubah data dari index
listAngka[0] = 0
#menambah data
listAngka.append(4)
#menghapus data
listAngka.remove(16)
del listAngka[0]
#Operator keanggotaan in dan not in akan mengembalikan nilai ke tipe data bool(TRUE OR FALSE)
a = 3 in listAngka
b = 3 not in listAngka
#Perulangan
#print("[LIST ANGKA]")

#for la in listAngka:
 #   print(la)


#TUPLE
#dapat diakses melalui indeks
#slicing data misal ditampilkan dari data ke 2 - 3
#tidak dapat menambah atau menghapus data melalui indeks atau tidak
#tupleAngka = (1,2,3)
#tupleAngka2 = tuple(listAngka)

#perulangan
#print("[TUPLE ANGKA]")
#for ta in tupleAngka:
 #   print(ta)

#SET
#tidak dapat diakses melalui indeks
#tidak ada fitur slicing data
#dapat menambah atau menghapus data bukan melalui indeks
#menambah dengan perintah set.add
#setAngka = {1,2,3}
#setAngka.add(4)

#perulangan
#print("[SET ANGKA]")
#for sa in setAngka:
 #   print(sa)


"""
    clear()  Remove all the elements from the dictionary
    copy() Returns a copy of the dictionary
    get() Returns the value of specified key
    items() Returns a list containing a tuple for each key value pair
    keys() Returns a list containing dictionary’s keys
    pop() Remove the element with specified key
    popitem() Removes the last inserted key-value pair
    update() Updates dictionary with specified key-value pairs
    values() Returns a list of all the values of dictionary
"""

#DICTIONARY
person = {
    1 : {"name" : "dika"},
    2 : {"name" : "dika2"},
    }

for i in person:
    print(person[i]["name"])
    


