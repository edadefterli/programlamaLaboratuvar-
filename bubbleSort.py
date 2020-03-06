def bubble_sort(list1):
    for i in range(len(list1)):
        for j in range(0,len(liste)-i-1):
            if(list1[j]>list1[j+1]):
                t=list1[j+1]
                list1[j+1]=list1[j]
                list1[j]=t
    return list1

liste=[3,5,9,12,54,7,23,0]
bubble_sort(liste)
for i in range(len(liste)):
    print ("%d" %liste[i])