def shellSort(arr):
    n=len(arr)
    gap=n//2
    while(gap>0):
        for i in range(gap,n):
            temp=arr[i]
            j=i
            while(j>=gap and arr[j-gap]>temp):
                arr[j]=arr[j-gap]
                j-=gap
            arr[j]=temp
        gap//=2

liste=[5,96,4,8,2,64,28,0]
shellSort(liste)
print(liste)