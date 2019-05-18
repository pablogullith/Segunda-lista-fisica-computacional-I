# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 01:09:42 2019

@author: pablo gullith
"""
#Questão 3:
#Aluno: Pablo Gullith de Melo Dantas
from __future__ import division, print_function

def f(x):
    return x**4 - 2*x + 1


def integrate(f,a,b,N=20):
	
	h = (b-a)/N
	
	s = 0.5*f(a) + 0.5*f(b)
	for k in range(1,N):
	    s += f(a+k*h)
	
	return h*s

I1 = integrate(f,0,2,10)
I2 = integrate(f,0,2,20)

delta = 1/3*(I2-I1)
diferença = (4.4-I2)

print(
"""
N = 10 Fátias   Integral = {}
N = 20 Fátias 	Integral = {}
delta = {}
diferença = {}
""".format(I1,I2,delta,diferença)
)

#Os erros achados de ambas as formas são bem próximos.

#Não concordam perfeitamente porque em um dos métodos você usa
#o valor real 4.4 e no outro método você não usa. 
