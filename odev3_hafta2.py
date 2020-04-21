#Binom dağılımı: n sayıda, sadece 2 farklı sonuc(evet veya hayır,1 veya 0 vb.) verebilen denemelere uygulanır.
#p değerine evet dersek 1-p hayır sonucuna karşılık gelir.
#Bu türlü bağımsız n sayıda denemeler serisi içinde elde edilen başarı sayısının ayrık olasılık dağılımı binom dağılım olarak tanımlanır.
#Bir binom dağılım sadece iki parametre ile, yani n ve p, ile tam olarak tanımlanır.
#X binom dağılım gösterirse şöyle ifade edilir: X ~ B(n,p)

import sympy as sym
from sympy import Symbol
from sympy import pprint
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

p=Symbol('p')   #istenilen durumu başarma olasılığı
x=Symbol('x')   #istenilen durum sayısı
n=Symbol('n')   #deneme sayısı

my_f_3_part_0=sym.factorial(n)/(sym.factorial(x)*sym.factorial(n-x))
my_f_3_part_1=p**x
my_f_3_part_2=(1-p)**(n-x)
my_f_3=my_f_3_part_0*my_f_3_part_1*my_f_3_part_2

print("Binomial Distribution")
pprint(my_f_3)
sym.plot(my_f_3.subs({p:0.5,n:50}),(x,0,50),title='binomial distribution plot for n=50') #sympy kütüphanesi ile gösterim


#matpoltlib kütüphanesi ile gösterim
x1=[]
y1=[]
for i in range(50):
    y = my_f_3.subs({p: 0.5, n: 50, x: i}).evalf()
    y1.append(y)
    x1.append(i)

plt.plot(x1,y1)
plt.show()