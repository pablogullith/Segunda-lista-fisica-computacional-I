# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 22:00:00 2019

@author: pablo gullith
"""
#Questão 1:
#Aluno: Pablo Gullith de Melo Dantas
from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return np.exp(-x**2)

#Funções para dar o valor da integral
def integrate(f,a,b,N):
	
	h = (b-a)/N
	
	s = 0.5*f(a) + 0.5*f(b)
	for k in range(1,N):
	    s += f(a+k*h)
	
	return h*s

I1 = integrate(f,0,3,30)
print('Integral:',I1)

#Funções para dar o gráfico
def integrate(f,a,b):
	
	h = 0.1
	
	N = int((b-a)/h)
	
	
	delta = b-a - N*h

	I = 0
	
	if N>0:	
		s = (f(a) + f(b-delta))/2
		
		for k in range(1,N):
			s+= f(a+k*h)
	
		I = s*h

	I += delta*(f(b) + f(b-delta))/2
	
	return I

x = np.linspace(0,3)
E = [integrate(f,0,xi) for xi in x]
plt.title("Gráfico E(x)")
plt.plot(x,E)
