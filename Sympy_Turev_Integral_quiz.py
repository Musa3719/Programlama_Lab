from sympy import Symbol,Limit,pprint,exp,sqrt,pi,Integral
#Turev
t = Symbol('t')
St = 5*t**2 + 2*t + 8
t1 = Symbol('t1')
delta_t = Symbol('delta_t')
St1 = St.subs({t: t1})
St1_delta = St.subs({t: t1 + delta_t})
pprint(Limit((St1_delta-St1)/delta_t,delta_t, 0).doit())
#Integral
x = Symbol ('x')
p = exp(-(x-10)**2/2)/sqrt(2*pi)
pprint(Integral(p,(x, 11, 12)).doit().evalf())