def min_heapify(array, i):  #her eklenen elemanı yığın ağacının yapısını koruyarak uygun bir yere koyar.
    left = 2 * i + 1        #aldığı parametreler: array-> diziyi alır   i-> eklenecek sayıyı alır.
    right = 2 * i + 2
    length = len(array) - 1
    smallest = i
    if left <= length and array[i] > array[left]:
        smallest = left
    if right <= length and array[smallest] > array[right]:
        smallest = right
    if smallest != i:
        array[i], array[smallest] = array[smallest], array[i]
        min_heapify(array, smallest)

def build_min_heap(array):      #var olan bir listeyi min heap yapısına uygun olarak düzenler. Parametre olarak dizinin kendisini alır.
    for i in reversed(range(len(array)//2)):
        min_heapify(array, i)

my_array_1=[8,10,3,4,7,15,1,2,16]
build_min_heap(my_array_1)
print(my_array_1)

def heapsort(array):    #min heap ağacının liste halini alıp küçükten büyüğe sıralar.
    array = array.copy()
    build_min_heap(array)
    sorted_array = []
    for _ in range(len(array)):
        array[0], array[-1] = array[-1], array[0]
        sorted_array.append(array.pop())
        min_heapify(array, 0)
    return sorted_array

my_array_2=heapsort(my_array_1)
print("Dizi:",my_array_1)
print("Dizinin sıralanmıs hali:",my_array_2)

def insertItemToHeap(myheap_1,item):    #listeyi ve eklenecek elemanı alıp minheap yapısını koruyarak elemanı ekler.
    myheap_1.append(item)
    min_heapify(myheap_1, (len(myheap_1) - 1))
    myheap_2=heapsort(myheap_1)
    return myheap_2

my_array_3=insertItemToHeap(my_array_2,9)
print("Dizinin 9 eklenmiş hali:",my_array_3)


def removeItemFrom(myheap_1):     #minheap'deki en yüksek değerlikli elemanı siler. parametre olarak listeyi alır.
    myheap_1.pop(0)
    myheap_2=build_min_heap(myheap_1)
    return myheap_2

removeItemFrom(my_array_3)
print(my_array_3)