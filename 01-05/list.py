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
#dictHewan.update({"Karnivora" : listHewanKarnivora})

#menambah listhewan karnifora ke dict hewan
if "Karnivora" in dictHewan:
    dictHewan["Karnivora"].extend(listHewanKarnivora)

print(dictHewan)
