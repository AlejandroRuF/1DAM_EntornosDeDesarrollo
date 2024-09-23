import matplotlib.pyplot as plt
import random
import time
import ordenacion as o
tamanyo = [100,500,1000,2000,5000,10000]
resultadosExange = []
for i in range(len(tamanyo)):
    desordenado=random.sample(range(0,tamanyo[i]),tamanyo[i])
    temp=desordenado.copy()
    inicio = time.process_time()
    o.exchange_sort(temp)
    fin = time.process_time()
    resultadosExange.append(fin - inicio)
    print(f"Exange ---> Tiempo proceso exchange: {resultadosExange[i]} en {tamanyo[i]}")

print("---------------------------------------------------------------------")

resultadosBubble = []
for i in range(len(tamanyo)):
    desordenado=random.sample(range(0,tamanyo[i]),tamanyo[i])
    temp=desordenado.copy()
    inicio = time.process_time()
    o.bubble_sort(temp)
    fin = time.process_time()
    resultadosBubble.append(fin - inicio)
    print(f"Bubble ---> Tiempo proceso exchange: {resultadosBubble[i]} en {tamanyo[i]}")

print("---------------------------------------------------------------------")

resultadosQuick = []
for i in range(len(tamanyo)):
    desordenado=random.sample(range(0,tamanyo[i]),tamanyo[i])
    temp=desordenado.copy()
    inicio = time.process_time()
    o.quick_sort(temp)
    fin = time.process_time()
    resultadosQuick.append(fin - inicio)
    print(f"Quick ---> Tiempo proceso exchange: {resultadosQuick[i]} en {tamanyo[i]}")

print("---------------------------------------------------------------------")

resultadosHeap = []
for i in range(len(tamanyo)):
    desordenado=random.sample(range(0,tamanyo[i]),tamanyo[i])
    temp=desordenado.copy()
    inicio = time.process_time()
    o.heap_sort(temp)
    fin = time.process_time()
    resultadosHeap.append(fin - inicio)
    print(f"Heap ---> Tiempo proceso exchange: {resultadosHeap[i]} en {tamanyo[i]}")

print("---------------------------------------------------------------------")

resultadosMerge = []
for i in range(len(tamanyo)):
    desordenado=random.sample(range(0,tamanyo[i]),tamanyo[i])
    temp=desordenado.copy()
    inicio = time.process_time()
    o.merge_sort(temp)
    fin = time.process_time()
    resultadosMerge.append(fin - inicio)
    print(f"Merge ---> Tiempo proceso exchange: {resultadosMerge[i]} en {tamanyo[i]}")



fig, ax = plt.subplots()
numeros = ['100', '500', '1000', '2000', '5000', '10000']
Segundos = {'Exchange':resultadosExange, 'Bubble':resultadosBubble,'Quick': resultadosQuick,'Heap': resultadosHeap,'Merge':resultadosMerge}
ax.plot(numeros, Segundos['Exchange'], label ='Exchange')
ax.plot(numeros, Segundos['Bubble'], label ='Bubble')
ax.plot(numeros, Segundos['Quick'], label ='Quick')
ax.plot(numeros, Segundos['Heap'], label ='Heap')
ax.plot(numeros, Segundos['Merge'], label ='Merge')
ax.legend(loc = 'upper right')
plt.show()