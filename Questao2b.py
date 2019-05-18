# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 22:37:35 2019

@author: pablo gullith
"""
#Questão 2b:
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

x,y = np.mgrid[-1:1:100j,-1:1:100j]
r = np.sqrt(x**2 + y**2)
wavelength = 0.5
k = 2*pi/wavelength

I = (J(1,r*k)/k/r)**2
plt.gray()
plt.imshow(I,vmax=0.1/10,extent=(-1,1,-1,1))
plt.title("Gráfico de Densidade")
