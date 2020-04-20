#Musa Odabaşı, 180401039, https://github.com/Musa3719/Programlama_Lab/blob/master/180401039_Sympy_hw_3.py
#Exponential Distribution  delta = 1 alındı
from sympy import Symbol,pprint,exp
from sympy.plotting import plot
import matplotlib.pyplot as plt
x = Symbol('x')
delta = Symbol('delta')
ED = delta*exp((-delta)*x)
plot(ED.subs({delta:1}),(x,0,25),title='Exponential Distribution')
x_values = []
y_values = []
for value in range(0, 26):
    y = ED.subs({delta: 1, x: value}).evalf()
    y_values.append(y)
    x_values.append(value)
plt.plot(x_values,y_values)
plt.show()
