# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 14:02:08 2018

@author: Samuel
"""
import matplotlib.pyplot as plt
fin=0
n=0
ListeNoeuds=[]
while fin==0 :
    print("ajouter noeud ? (oui/non)")
    res=input()
    if res=="non":
        fin=1
    elif res=="oui":
        print("coordonnée en x")
        x=int(input())
        print("coordonnée en y")
        y=int(input())
        ListeNoeuds.append([x,y])
    else :
        print("erreur, veuiller entrer oui ou non")
fin=0
n=0
ListeBarres=[]
while fin==0 :
    print("ajouter barre ? (oui/non)")
    res=input()
    if res=="non":
        fin=1
    elif res=="oui":
        print("noeud 1 ou -1 si appui sol")
        n1=int(input())
        print("type liaison ? (encastrement e, articulation a, appui simple ap)")
        l1=input()
        print("noeud 2 ou -1 si appui sol")
        n2=int(input())
        print("type liaison ? (encastrement e, articulation a, appui simple ap)")
        l2=input()
        ListeBarres.append([n1,l1,n2,l2])
        n+=1
    else :
        print("erreur, veuiller entrer oui ou non")   
        
b=len(ListeBarres)
pN=0
ql=0

for i in range(len(ListeBarres)):
    for j in range(len(ListeBarres[i])):
        if ListeBarres[i][j]=="e":
            ql+=3
        elif ListeBarres[i][j]=="a":
            ql+=2
        elif ListeBarres[i][j]=="ap":
            ql+=1
            
            
for i in range(len(ListeNoeuds)):
    Li=[]
    for j in range(len(ListeBarres)):
        if ListeBarres[j][0]==i and ListeBarres[j][1]=="e" or ListeBarres[j][2]==i and ListeBarres[j][3]=="e" :
            Li.append(3)
        elif ListeBarres[j][0]==i and ListeBarres[j][1]=="a" or ListeBarres[j][2]==i and ListeBarres[j][3]=="a" :
            Li.append(2)
        elif ListeBarres[j][0]==i and ListeBarres[j][1]=="ap" or ListeBarres[j][2]==i and ListeBarres[j][3]=="ap" :
            Li.append(1)
    mx=0
    for k in range(len(Li)):
        if Li[k]>mx:
            mx=Li[k]
    pN+=mx
        
print("degré d'hyperstatisme:")  
print(3*b+pN-ql)

XN=[ListeNoeuds[i][0] for i in range(len(ListeNoeuds))]
YN=[ListeNoeuds[i][1] for i in range(len(ListeNoeuds))]
plt.scatter(XN,YN)
for i in range(len(ListeBarres)):
    k=int(ListeBarres[i][0])
    l=int(ListeBarres[i][2]) 
    plt.plot([ListeNoeuds[k][0],ListeNoeuds[l][0]],[ListeNoeuds[k][1],ListeNoeuds[l][1]])
