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
print("[LIST ANGKA]")

for la in listAngka:
    print(la)


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

