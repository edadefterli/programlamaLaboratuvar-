#binomial distribution formula(binom dağılımı)

import sympy as sym
from sympy import Symbol
from sympy import pprint

p=Symbol('p')   #istenilen durumu başarma olasılığı
x=Symbol('x')   #istenilen durum sayısı
n=Symbol('n')   #deneme sayısı

my_f_3_part_0=sym.factorial(n)/(sym.factorial(x)*sym.factorial(n-x))
my_f_3_part_1=p**x
my_f_3_part_2=(1-p)**(n-x)
my_f_3=my_f_3_part_0*my_f_3_part_1*my_f_3_part_2

pprint(my_f_3)
sym.plot(my_f_3.subs({p:0.5,n:50}),(x,0,50),title='binomial distribution plot for n=50')