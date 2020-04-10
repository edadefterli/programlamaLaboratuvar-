import csv
import re

def my_frequency_with_of_tuples(list_1):  #liste yardımıyla histogram hesaplama
    frequency_list=[]
    for i in range(len(list_1)):
        s=False
        for j in range(len(frequency_list)):
            if(list_1[i]==frequency_list[j][0]):
                frequency_list[j][1]=frequency_list[j][1]+1
                s=True
        if(s==False):                              #eğer bir değerle ilk defa karşılaşıyorsa bu bloğa girer
            frequency_list.append([list_1[i],1])
    return frequency_list

def my_median(my_list):  #medyan değerinin hesaplanması
    n=len(my_list)
    if n%2==1:    #liste tek elemanlı ise
        median=my_list[n//2]
    else:
        middle_1=my_list[int(n//2)]
        middle_2=my_list[int(n//2)-1]
        median=(middle_1+middle_2)/2
    return median


dosya=open("input_hw_2.csv","r")
satirlar=dosya.readlines()
liste=[]
sozluk={}
for satir in satirlar:
    x=re.split(";",satir)  #dosyada her satırda bulunan ; ile ayrılan öğeleri x değişkenine listeler,yani her satırı liste şekline getirir.
    x=x[-1]                 #listedeki son elemanı alır,yani her satırdaki ayrılış_tarihini tutar.
    a=re.split("-",x)       #ayrılış tarihindeki yıl-ay-gün-saat şeklinde ayrılmış değerleri a değişkenine listeler.
    liste.append(int(a[1])) #bu listenin 1.indisindeki değeri yani ayı integer'a çevirerek listeye ekler.

liste.sort()
#print(liste)    #dosyadaki bütün ay değerlerini sıralı bir şekilde yazdırır.

histogram_listesi=my_frequency_with_of_tuples(liste)
for i in range(len(histogram_listesi)):
    for j in range(1):
        print(histogram_listesi[i][j],".ay",histogram_listesi[i][j+1],"kişi ilişiğini kesmiş.")

#print(histogram_listesi) #histogram listesini çıkarır.

frequency=[]
for i in range(len(histogram_listesi)):     #histogram listesindeki aylardaki ilişiği kesilmiş kişi sayılarını listeye atar.
    frequency.append(histogram_listesi[i][1])
frequency.sort()
#print(frequency)

toplam=0
for i in frequency: #liste toplamı
    toplam+=i

ortalama=toplam/len(frequency)
medyan=my_median(frequency)

f=open("170401025_hw_2_output.txt","w",encoding="utf-8")
f.write("Medyan degeri:")
f.write(str(medyan))
f.write("\nortalama degeri:")
f.write(str(ortalama))
f.close()
