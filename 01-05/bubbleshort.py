data = [6,5,3,1,8,7,2,4]
n = len(data)
def bubble(data):
    for i in range(n-1):
        for j in range(0,n-i-1):
            if data[j] > data[j+1]:
                swapped = True
                data[j],data[j+1] = data[j+1],data[j]
                if not swapped:
                    return
bubble(data) 
for i in range(len(data)):
    print("%d" % data[i],end=" ")