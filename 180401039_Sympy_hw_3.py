#Musa Odabaşı, 180401039, https://github.com/Musa3719/Programlama_Lab/blob/master/180401039_Sympy_hw_3.py
#Exponential Distribution  delta = 1 / Ortalama olay süresi
#Şirketin bir ürünü satması ortalama 4 dakika sürüyor.
#Şirketin 12 dakika boyunca ürün satmama ihtimali
#Delta = 1/4 =0.25
from sympy import Symbol,pprint,exp
from sympy.plotting import plot
import matplotlib.pyplot as plt
x = Symbol('x')
delta = Symbol('delta')
ED = exp((-delta)*x)#1-(1-exp)=exp
plot(ED.subs({delta: 0.25}),(x,0,12),title='12 dakika ürün satılmama olasılığı')
x_values = []
y_values = []
for value in range(0, 13):
    y = ED.subs({delta: 0.25, x: value}).evalf()
    y_values.append(y)
    x_values.append(value)
plt.plot(x_values,y_values)
plt.show()
