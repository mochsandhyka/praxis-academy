a = ["nanas","nangka","nugget"]
for a in a:
    print(a,len(a))

#membuat list u
#                                                                                                                                                                                                  sers dan status
users = {"Hans" : "active", "Tiva":"inactive"}

#mengkopi item pada list users dan menghapus apabila status = inactive
for user, status in users.copy().items():
    if status == "inactive":
        del users[user]
#membuat list kosong
active_users = {}
#apabila status active insert ke list active_users
for user,status in users.items():
    if status == "active":
        active_users[user] = status

print(active_users)


#FUNGSI RANGE

#mulai dari 0 -4
for i in range(5):
    print(i)

#print lenght a dan isi a
a = ["nanas","nangka","nugget"]
for ab in range(len(a)):
    print(ab, a[ab])

#sum range a
a = sum(range(4))
print(a)

for a in range(2,10):
    for b in range(2,a):
        if a % b == 0:
            print(a,"equals",b ,"*",a//b)
            break
        else:
            print(a,"is prime number")

#for(i=0;i<lenA;i++)
a = ["1","2","3","4"]
for i in range(len(a)):
    print(i+1)

for num in range(2,10):
    if num % 2 == 0:
        print ("Found an even number", num)
        continue
    print("Found an odd number",num)

#MATCH

command = "hello"
match command:
    case "hello2":
        print("hello2")
    case "hello3":
        print("hello3")
    case "hello":
        print("hello")
    case other:
        print("nothing")

def http_error(status):
    match status:
        case 400:
            return "Bad Request"
        case 404:
            return "Not Found"
        case 418|419:
            return "Iam a teapot"
        case _:
            return "Something\'s wrong with the internet"

#point tuple
point = (0, 1)
match point:
    case(0, 0):
        print("Origin")
    case(0, y):
        print(f"Y={y}")
    case(x, 0):
        print(f"X={x}")
    case(x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("not a point")

