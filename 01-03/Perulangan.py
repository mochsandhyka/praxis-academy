#LIST
#dapat diakses melalui indeks
#slicing data misal ditampilkan dari data ke 2 - 3
#dapat menambah atau menghapus data melalui indeks atau tidak
#menambahkan dengan perintah list.append
listAngka = [1,2,3,16]
listAngka2 = listAngka[2:]
listAngka[0] = 0
listAngka.append(4)
listAngka.remove(16)
del listAngka[0]


#TUPLE
#dapat diakses melalui indeks
#slicing data misal ditampilkan dari data ke 2 - 3
#tidak dapat menambah atau menghapus data melalui indeks atau tidak
tupleAngka = (1,2,3)
tupleAngka2 = tuple(listAngka)


#SET
#tidak dapat diakses melalui indeks
#tidak ada fitur slicing data
#dapat menambah atau menghapus data bukan melalui indeks
#menambah dengan perintah set.add
setAngka = {1,2,3}
setAngka.add(4)


print("List angka :",listAngka)
print("Set angka :",setAngka)