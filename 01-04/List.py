#METHOD PADA DATA LIST

#APPEND
listKendaraan = ["mobil","motor","truck"]   #buat list kendaraan
listKendaraan.append("bus")                 #menambah list kendaraan dengan append(menambah 1 data di akhir
#print(listKendaraan)

listKendaraanTambahan =["perahu","pesawat"] #list kendaraan tambahan
for listK in listKendaraanTambahan:         #looping untuk menambah data di tambahan ke list kendaraan
    listKendaraan.append(listK)
#print(listKendaraan)

#tuples,set -> langsung ditambahkan
#string     -> ditambahkan perkarakter
#dictionary -> ditambahkan key saja

#EXTEND
listKendaraan = ["mobil","motor","truck","motor"]  
listKendaraanTuples = ("pesawat","kapal")
listKendaraanSet = {"becak","delman"}
listKendaraanString = "kereta"
listKendaraanDictionary = {
    "darat" : ["kereta","delman"],
    "udara" : "helikopter"}


listKendaraanDic = list(listKendaraanDictionary.values())   #convert value dictionary ke list 
#for i in listKendaraanDic[0]:                               #looping isi listkendaraandic[0]
 #   listKendaraanDic.append(i)                              #menambah listkendaraandic dengan isi dari listkendaraandic[0]
#listKendaraanDic.pop(0)                                     #menghapus isi listkendaraandic index ke 0


listKendaraan2Dictionary = {
    "darat" : ["kereta","delman"],
    "air" : ["kapal selam"],
    "udara" : ["kelelawar","helikopter"]}
listKendaraan2Dictionary = list(listKendaraan2Dictionary.values())
ask = []
for i in listKendaraan2Dictionary:
    ask.extend(i)

print(ask)

 
 

#listKendaraanDic.extend(listKendaraanDic[0])
#listKendaraanDic.pop(0)


#print(listKendaraanDic)


#listKendaraan.extend(listKendaraanDictionary.values())
#print(listKendaraan)


#INSERT
#insert data ke index tertentu
#Tipe data tetap 
listKendaraan.insert(1,listKendaraanString)
#print(listKendaraan)

#REMOVE
#listKendaraan.remove("motor")   #remove element in list
#print(listKendaraan)
#listKendaraan.pop(0)            #remove element by index
#print(listKendaraan)
#listKendaraan.clear()           #remove all item 
#print(listKendaraan)

#INDEX
index = listKendaraan.index("mobil")
#print(index)

#COUNT
count = listKendaraan.count("motor")
#print(count)

#SORT
listKendaraan.sort()            #sort a - z
listKendaraan.sort(reverse=True)#sort z- a

def fungsiSort(a):              #def fungsi sort berdasar banyak karakter
    return len(a)

listKendaraan.sort(key=fungsiSort)  #sort dengan fungsi

kendaraan = [
    {"merk" : "yamaha", "tahun" : 2005},
    {"merk" : "bmw", "tahun" : 2020},
    {"merk" : "honda",  "tahun" : 2002}
]

def fungsiSortTahun(a):
    return a["tahun"]

kendaraan.sort(reverse=False, key=fungsiSortTahun)

