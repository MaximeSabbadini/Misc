#!/usr/bin/env python3
# -*- coding: utf-8 -*-



##############################################################################
#Programme de calcul d'incertitudes, utilisant l'écart-type expérimental,    #
#			l'incertitude type s et les coefficients de student 			 #
#						pour un nombre N de mesures.                         #
##############################################################################

""" @author: maximesabbadini """

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


nom_colonnes=['x','y']

data=pd.read_csv('mesures_bobine.csv', names=nom_colonnes, skiprows=1, dtype='float')   #Attention de bien mettre x dans la colonne 1 et y dans la colonne 2
																						#Si pas de titre de colonnes ==> skiprows=0
#print(data)      #Pour vérifier les données

N=10                      #Nbre de points par mesure
n=len(nom_colonnes)		  #Nbre de colonnes
coeff=2.26				  #Coeff de student

def incertitudes(data, N, n, coeff):   
    X=data.x
    Y=data.y
    
    Moyenne=np.zeros((n,int(len(data)/N)))              #Création du tableau vide pour stocker les valeurs de la moyenne
    
    for k in range(0, int(len(data)/N)):                #Calcul de la Moyenne
        Moyenne[0, k]=sum(X[k*N:(k+1)*N])/N
        Moyenne[1, k]=sum(Y[k*N:(k+1)*N])/N
        
    M=Moyenne[1,:]    									#Je prend les valeurs qui nécessitent un traitement d'incertitude
    Abscisse=Moyenne[0,:]       						#Ces valeurs sont stockées pour le plot plus tard
    
    sexp=np.zeros(int(len(data)/N))						#Création du tableau vide pour stocker les valeurs de l'écart type expérimental
    
    for i in range(0, int(len(data)/N)):				#Calcul de l'écart type expérimental
        somme=0
        for k in range(i*N, (i+1)*N):
            somme+=(Y[k]-M[i])**2
        sexp[i]=np.sqrt(somme/(N-1))
        
    s=np.zeros(int(len(data)/N))						
    for i in range(0, int(len(data)/N)):				#Calcul de l'incertitude type s
        s[i]=sexp[i]/np.sqrt(N)
    
    delta=np.zeros(int(len(data)/N))
    for i in range(0,int(len(data)/N)):					#Calcul de l'incertitude ±ks
            delta[i]=coeff*s[i]
            
            
    resultat=np.zeros((3,int(len(data)/N)),dtype='float')      #Tableau pour stocker le résultat du traitement avec :
    
    for i in range(0,int(len(data)/N)):
        resultat[0,i]=Abscisse[i]								#Ligne 0 : Abscisses stockées auparavant (Pas de traitement d'incertitudes)	
        resultat[1,i]=M[i]										#Ligne 1 : Valeurs moyennes des mesures
        resultat[2,i]=delta[i]									#Ligne 2 : Incertitude sur les mesures
    
    
    return resultat
    
    
L=incertitudes(data, N, n, coeff)           					#Appel de la fonction





