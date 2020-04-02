#linear search on list

def my_linear_search(my_list,item_search):
    found=(-1,-1)  #default, eğer listede yoksa
    n=len(my_list)
    for indis in range(n):
        if my_list[indis]==item_search:
            found=(my_list[indis],indis)  #aranan elemandan 1'den fazla varsa son bulduğunun indisini yazar
            #break  #ilk bulduğu anda döngüden çıkar
    return found

my_list=[5,7,2,6,2,8,9,3,4,8,5,3,0,6,4]
print(my_linear_search(my_list,8))


#mean on list

def my_mean(my_list):
    s,t=0,0
    for item in my_list:
        s+=1
        t+=item
    mean=t/s
    return mean

my_list=[5,7,2,6,2,8,9,3,4,8,5,3,0,6,4]
print(my_mean(my_list))


#sort the list(bubble sort)

def bubble_sort(my_list):
    n=len(my_list)
    #print(my_list)
    for i in range(n-1,-1,-1):
        for j in range(0,i):
            if not (my_list[j]<my_list[j+1]):
                #print("swap işlemi")
                temp=my_list[j]
                my_list[j]=my_list[j+1]
                my_list[j+1]=temp
    return my_list

my_list=[5,7,12,-6,8,91,3,4,-84]
print(bubble_sort(my_list))


#binary search on a sorted list

def my_binary_search(my_list,item_search):
    found=(-1,-1)
    low=0
    high=len(my_list)-1
    while low<=high:
        mid=(low+high)//2
        if my_list[mid]==item_search:
            return my_list[mid],mid
        elif my_list[mid] > item_search:
            high=mid-1
        else:
            low=mid+1
    return found

my_list=[-84, -6, 3, 4, 5, 7, 8, 12, 91]
print(my_binary_search(my_list,8))


#median of a list

def my_median(my_list):
    my_list_2=bubble_sort(my_list)
    n=len(my_list_2)
    if n%2==1:    #liste tek elemanlı ise
        median=my_list_2[n//2]

    else:
        middle_1=my_list_2[int(n//2)]
        middle_2=my_list_2[int(n//2)-1]
        median=(middle_1+middle_2)/2

    return median

my_list=[5,7,12,-6,8,91,3,4,-84,4]
print(my_median(my_list))