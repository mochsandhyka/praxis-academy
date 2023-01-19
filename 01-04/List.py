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
listKendaraan = ["mobil","motor","truck"]  
listKendaraanTuples = ("pesawat","kapal")
listKendaraanSet = {"becak","delman"}
listKendaraanString = "kereta"
listKendaraanDictionary = {
    "darat" : ["kereta","delman"],
    "udara" : "helikopter"}

listKendaraanDic = list(listKendaraanDictionary.values())
for i in listKendaraanDic:
    listKendaraanDic.append(i)
print(listKendaraanDic)

listKendaraanDic[0].append(listKendaraanDic[1])
print(listKendaraanDic[0])
print(listKendaraanDic)

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
