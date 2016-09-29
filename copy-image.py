#!/usr/bin/python
# -*- coding: utf-8 -*-
#===================================#
# File name: copy-image.py			#
# Author: Vitor dos Santos Batista	#
# Date created:27/09/2016 			#
# Date last modified: 28/09/2016	#
# Python Version: 2.7				#
#===================================#

#===========================Importações============================#
import matplotlib.pyplot as plt
import numpy as np
from scipy import misc

#=============================Funções==============================#
#Avaliação
def avaliacao(pop):
    for i, ind in enumerate(pop):
        pop[i, -1] = sum(ind[:-1] == img)
        pop[i, -1] = pop[i, -1]/65
    return pop

#Seleção dos pais por Torneio
def selecaoTorneio(pop, tor):
    r = pop.shape[0]
    popOut = pop.copy()
    for i in range(r):
        #Torneio
        #Seleciona dois indivíduos aleatórios
        [a, b] = np.random.choice(r, 2, replace=False)
        ind1 = pop[a]
        ind2 = pop[b]
        #Realiza o torneio e coloca o selecionado na pop
        popOut[i] = torneio(ind1, ind2, tor)
    return popOut

#Seleção dos pais por Torneio
def selecaoTorneio(pop, tor):
    r = pop.shape[0]
    popOut = pop.copy()
    for i in range(r):
        #Torneio
        #Seleciona dois indivíduos aleatórios
        [a, b] = np.random.choice(r, 2, replace=False)
        ind1 = pop[a]
        ind2 = pop[b]
        #Realiza o torneio e coloca o selecionado na pop
        popOut[i] = torneio(ind1, ind2, tor)
    return popOut

#Torneio para a seleção
def torneio(ind1, ind2, tor):
    #Torneio
    rand = np.random.rand()
    #Minimizar
    if ind1[-1] > ind2[-1]:
        if tor > rand:
            return ind1
        else:
            return ind2
    else:
        if tor > rand:
            return ind2
        else:
            return ind1

#Mutação
def mutacao(pop, mut):
    popOut = pop.copy()
    for i, ind in enumerate(pop):
        for j, gen in enumerate(ind):
            r = np.random.rand()
            if mut > r:
                popOut[i, j] = 1-gen
    return popOut

#Cruzamento
def cruzamento(pop, cross):
    popTemp = pop.copy()
    popOut = pop.copy()
    popTemp = popTemp[:, :-1]
    for i in range(0, pop.shape[0], 2):
        if len(popTemp) < 2:
            break
        i1 = popTemp[0]
        i2 = popTemp[0]
        popTemp = popTemp[2:, :]
        rand = np.random.rand()
        if cross > rand:
            i1, i2 = crossBin(i1, i2)
        popOut[i, :-1] = i1
        popOut[i+1, :-1] = i2
    return popOut

#Crossover uniforme
def crossBin(p1, p2):
    f1 = f2 = p2
    mask = np.random.random(indTam-1) > 0.5
    for i, gen in enumerate(mask):
        if gen is True:
            f1[i] = p1[i]
        else:
            f2[i] = p1[i]
    return f1, f2

#==========================Funções-fim=============================#

#------------------------------------------------------------------#

#========================Leitura da imagem=========================#
img = misc.imread("space2.jpg", flatten=1)
img = img.ravel() > 100
img = img * 1 

#===========================Parâmetros=============================#
gen = 200
tor = 0.8
cross = 0.8
mut = 0.01
popTam = 700
indTam = 65

#Outros
fits = np.array(())


#=======================População inicial==========================#
pop = np.random.random(indTam) > 0.5
for i in range(popTam-1):
    a = np.random.random(indTam) > 0.5
    pop = np.vstack((pop, a))
pop = pop * 1.

#=====================Avaliação da População=======================#
pop = avaliacao(pop)

#==========================Gerações================================#
for i in range(gen):
	#Seleção
    pop = selecaoTorneio(pop, tor)
	#Cruzamento
    pop = cruzamento(pop, cross)
	#Mutação
    pop = mutacao(pop, mut)
	#Avaliação da população
    pop = avaliacao(pop)
    #Organização da população para a extração da
    #melhor fitness
    popSort = pop[pop[:,-1].argsort()]
    best = popSort[-1, -1]
    fits = np.append(fits, best)
	#Log
    print "Geração: ", i
    print "    Melhor: ", best
	#Salva na raiz as imagens dos melhores indivíduos de cada geração
    melhor = popSort[-1, :-1]
    melhor = np.reshape(melhor, (8, 8))
    #melhor = np.reshape(melhor, (16, 16))
    misc.imsave("%03d.png" %(i), melhor)

#===========================Plots==================================#
plt.plot(fits)
plt.show()
