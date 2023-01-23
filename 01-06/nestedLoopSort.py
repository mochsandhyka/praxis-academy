"""for x in range(3):
    for y in range(1,10):
        print(y, end = "")      #end = "" supaya cetak horizontal
    print()"""

"""for x in range(5):
    for y in range(1,5):
        print("#", end ="")
    print(" ")"""

"""peserta_0 = ["ucup",25,"laki-laki"]
peserta_1 = ["puio",2,"laki-laki"]
peserta_2 = ["ayu",14,"wanita"]
list_peserta = [peserta_0,peserta_1,peserta_2]

for x in list_peserta:
    print(f"nama : {x[0]}")
    print(f"umur : {x[1]}")
    print(f"gender : {x[2]}\n")"""

#bubble
data = [6,5,3,1,8,7,2,4]
n = len(data)
def bubble(data):
    for x in range(n-1):
        for y in range(0,n-x-1):
            if data[y] > data[y+1]:
                swapped = True
                data[y],data[y+1] = data[y+1],data[y]
                if not swapped:
                    return
bubble(data)
"""for x in range(n):
     print(data[x],end=" ")"""

#selection
data = [6,5,3,1,8,7,2,4]
n = len(data)

def selection_sort(data):  
    # perulangan list elemen
    for i in range(n):
        # cari nilai elemen terendah
        # yang masih tersedia
        min_idx = i
        for j in range(i+1, n):
            if data[min_idx] > data[j]:
                min_idx = j
        # tukar dengan nilai elemen ke-i
        data[i], data[min_idx] = data[min_idx], data[i]
    return data

selection_sort(data)
"""for x in range(n):
     print(data[x],end=" ")
"""

#insertion
data = [6,5,3,1,8,7,2,4]
n = len(data)

def insertion_sort(array):
    # perulangan pertama 
    for i in range(1, len(array)):
        # ini elemen yang akan kita posisikan
        key_item = array[i]
        # kunci index posisi 
        j = i - 1
        # lakukan perulangan kedua
        while j >= 0 and array[j] > key_item:
            # menggeser elemen yang lain
            array[j + 1] = array[j]
            j -= 1
        # memposisikan elemen
        array[j + 1] = key_item

    return array

"""print(insertion_sort(data))"""

#merge sort
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
# l is for left index and r is right index of the
# sub-array of arr to be sorted
 
 
def mergeSort(arr, l, r):
    if l < r:
 
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2
 
        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
 
 
# Driver code to test above
arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print("Given array is")
for i in range(n):
    print("%d" % arr[i],end=" ")
 
mergeSort(arr, 0, n-1)
print("\n\nSorted array is")
for i in range(n):
    print("%d" % arr[i],end=" ")
 
# This code is contributed by Mohit Kumra

#quick short
def partition(array, low, high):
 
    # choose the rightmost element as pivot
    pivot = array[high]
 
    # pointer for greater element
    i = low - 1
 
    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
 
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
 
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
 
    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    # Return the position from where partition is done
    return i + 1
 
# function to perform quicksort
 
 
def quickSort(array, low, high):
    if low < high:
 
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
 
        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)
 
        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)
 
 
data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array")
print(data)
 
size = len(data)
 
quickSort(data, 0, size - 1)
 
print('Sorted Array in Ascending Order:')
print(data)