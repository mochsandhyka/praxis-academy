#FUNGSI STRING

#capitalize
txt = "hello, and welcome to my world."
x = txt.capitalize()                    #Awal string menjadi huruf besar
#print(x)

#casefold
txt = "Hello, and wElcome to my woRld."
x = txt.casefold()                      #semua huruf menjadi kecil
#print(x)

#center
txt = "Kuda" 
x = txt.center(20)                        #20 car baru stringnya
x = txt.center(20, "o")                   #diantara txt disisipkan o
#print(x)

#count
txt = "I love apple, apple are my favorite fruit"
x = txt.count("apple", 1, 24)              #Search from position 1 -24
#print(x)

#encode
txt = "My name is Ståle" 
x = txt.encode()

#endswith
txt = "Hello, welcome to my world."
x = txt.endswith("my world.", 5, 11)

#expandtab
#txt = "H\te\tl\tl\to"

#print(txt)
#print(txt.expandtabs(1))
#print(txt.expandtabs(2))
#print(txt.expandtabs(4))
#print(txt.expandtabs(10)) 

#find
txt = "Hello, welcome to my world."
x = txt.find("e", 5, 10)            #find index e dari 5 -10
print(x)
#format
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36) 

