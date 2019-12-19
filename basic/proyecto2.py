import pandas as pd
import numpy as np
import matplotlib.pylab as plt

def leerCSV (archivo):
    CSV= pd.read_csv(archivo)
    #print(CSV)
    matriz=CSV.values
    #print(matriz)
    dias= matriz[:,0]                   # t
    TempMax= matriz[:,1]                # T1
    TempMin= matriz[:,2]                # T2
    PresMax= matriz[:,3]                # P1
    PresMin= matriz[:,4]                # P2
    VelViento= matriz[:,5]              # r
    Presipitaciones= matriz[:,6]        # s
    #print(PresMin)
    return dias,TempMax,TempMin,PresMax,PresMin,VelViento,Presipitaciones



def calculos (dato):
    #print('maximo:',max(dato),", minimo:",min(dato),', media:',dato.mean(), ', Desviacion STD:', dato.std(), ', desviacion relativa:', dato.var() )
    
    x = dias   
    y = dato
    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Grafico")
    plt.show()
    #print(dato)
    #print(dato.std())
    
    datoInf= dato.std()*-3
    lugar=0
    nuevo= []
    for i in dato:
        #print(i)
        datoSup=dato.mean()+(dato.std()*3)
        #print(datoSup)
        #lugar=lugar+1
        #print(lugar)
        if i >= datoSup:
            #print (i)
            nuevo.append(dato.mean)
            lugar=lugar+1
        else:
            nuevo.append(i) 
            lugar=lugar+1
    x = dias   
    y = nuevo
    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Grafico")
    plt.show()

    return i



############################### MAIN:

lectura= leerCSV('datos.csv')
dias=lectura[0]
calculos(lectura[3])