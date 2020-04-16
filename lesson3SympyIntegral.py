from sympy import Symbol, exp, sqrt, pi, Integral
x=Symbol('x')
p=exp(-(x-10)**2/2)/sqrt(2*pi)                  #integrali hesaplanacak fonksiyon
integral=Integral(p,(x,11,12)).doit().evalf()   #x'e göre integral al ve 11 ve 12 integralin alt ve üst sınırları olsun.
print(integral)                                 #evalf() --> sonucun float olarak döndür.