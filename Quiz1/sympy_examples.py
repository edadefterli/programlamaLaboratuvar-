from sympy import Symbol
x=1
print(x+x+1) #Buradaki x değeri değişkendir bu değişken sembolik olarak x ile gösterilmiştir.

x=Symbol('x') #sembolik bir değişkendir.İşlemler sembol üzerinden yapılır.
print(x+x+1)

x=Symbol('x')
y=Symbol('y')
p=x*(x+x)
print(p)

p=(x+2)*(x+3)
print(p)

from sympy import factor,expand          #factor: verilen ifadeyi çarpanlarına ayırır.
expr=x**2 - y**2                         #expand: factorun tam tersi çalışır.
print(factor(expr))
factors=factor(expr)
print(expand(factors))

expr=x**3 + 3*x**2*y + 3*x*y**2 + y**3
factors1=factor(expr)
print(factors1)

from sympy import pprint        #pprint: verilen ifadeyi günlük hayatta kullandığımız formatta yazar.
expr=x**2 + 2*x*y + y**2
pprint(expr)

x=Symbol('x')
series=x
n=5
for i in range(2,n+1):                #kuralı verilen bir diziyi 5 değerine kadar kurallı yazdırır.
    series=series+(x**i)/i
pprint(series)

expr1=x*x + x*y + x*y + y*y
res=expr1.subs({x:1,y:2})           #subs fonksiyonu Symbollerin yerine başka değerler koymamızı sağlar.Bu değerler sayi veya Symbol olabilir.
print(res)
print(expr1.subs({x:1-y}))    #x yerine 1-y koyar.



x=Symbol('x')
series1=x
n=50
x_value=5
for i in range(2,n+1):
    series1=series1+(x**i)/i
pprint(series1)
series1_value=series1.subs({x:x_value})
print(series1_value)
