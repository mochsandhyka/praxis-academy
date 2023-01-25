#LIST IN DICT TO LIST
listHewan = ["Ayam","Kelinci","Kuda"]
dictHewan = {"Karnivora" : ["Harimau","Singa"], "Herbivora" : ["Kambing"], "Omnivora" : ["Monyet"]}
dictHewanList = list(dictHewan.values())

for i in dictHewanList:
    listHewan.extend(i)
#print(listHewan)

#ADD KARNIVORA TO DICTHEWAN
listHewanKarnivora = ["Elang","Ular"]
dictHewan = {"Karnivora" : ["Harimau","Singa"], "Herbivora" : ["Kambing"], "Omnivora" : ["Monyet"]}
dictHewan.update({"Karnivora" : listHewanKarnivora})

#menambah listhewan karnifora ke dict hewan
if "Karnivora" in dictHewan:
    dictHewan["Karnivora"].extend(listHewanKarnivora)

#print(listHewanKarnivora)

dictBuku = {"Buku Pelajaran" : {"Judul":["Akutansi Pengantar 1","Akutansi Pengantar 2"],"Isi":["aaaaaaaaa","bbbbbbbb"]},
"Buku Cerita" : {"Judul":["Cindelaras","Mahabarata"],"Isi":["ccccccc","ddddddd"]}}
dictBukuPelajaran = list(dictBuku.values())
dictBukuPelajaran2 = dict(dictBukuPelajaran)
print(dictBukuPelajaran2)

print(type(dictBukuPelajaran2))
"""dictBukuPelajaran2 = dict(dictBukuPelajaran.values())
print(dictBukuPelajaran2)"""


listBukuPelajaran = []
for i in dictBukuPelajaran:
    listBukuPelajaran.extend(i)
print(listBukuPelajaran)

if "Buku Pelajaran" in dictBukuPelajaran:
    listBukuPelajaran.extend(dictBukuPelajaran)

"""listBuku =[]
for i in listBukuPelajaran:
    listBuku.extend(i)
print(listBuku)"""
