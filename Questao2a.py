# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 22:30:09 2019

@author: pablo gullith
"""
#Questão 2a:
#Aluno: Pablo Gullith de Melo Dantas
import numpy as np
from numpy import cos,sin,pi
import matplotlib.pyplot as plt

def J(m,x):	
	
	def f(teta):
	    return cos(m*teta - x*sin(teta))
	
	N = 1000
	a = 0
	b = pi
	h = (b-a)/N
	
	s = f(a) + f(b) + 4*f(b-h)
	for k in range(1,N//2):
	    s += 4*f(a + (2*k-1)*h) + 2*f(a+2*k*h)
	
	I = h/3*s/pi
	
	return I

x = np.linspace(0,20)
plt.title("Funções de Bessel")
plt.plot(x,J(0,x),label='J0')
plt.plot(x,J(1,x),label='J1')
plt.plot(x,J(2,x),label='J2')
plt.legend()
