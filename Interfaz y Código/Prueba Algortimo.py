#import graphviz as gv
import numpy as np
import pandas as pd
import heapq as hq
import math
import random
import csv

# Lee el archivo de texto

def loadData(fileName, time, dataset, rushHour = False):
  rushHour_Weigthed = []
  
  if rushHour == True: time = DeclarateTime()
  
  with open(fileName) as fname:
   datas = csv.reader(fname, delimiter = ",")
   
   for row in datas: 
    dataset.append(row)
    
    if rushHour == True:
      RushHours(rushHour_Weigthed)
      row.append(rushHour_Weigthed[int(time[:2])])

  #print(rushHour_Weigthed)

dataStreets = [] # osm_id, osm_name, #intersections 
dataIntersections = [] # all intersections data
intersectionList = []
intersectionID = []
adjList = []
time = ""



def intersectionsList(dataset, intersectionList, intersectionID, adjList):
  
  for row in dataset:
    targetIntersection = row[6]
    sourceIntersection = row[5]

    if sourceIntersection not in intersectionID:
      aux = []
      aux.append(row[11])
      aux.append(row[12])
      intersectionList.append(aux) 
      adjList.append([])
      intersectionID.append(sourceIntersection)
      

    if targetIntersection not in intersectionID:
      aux = []
      aux.append(row[13])
      aux.append(row[14])
      intersectionList.append(aux)
      adjList.append([])
      intersectionID.append(targetIntersection)
      


def adjl(dataset, adjList):
  

  for row in dataset:
    indexSource = row[5]
    indexTarget = row[6]
    weight = row[7]
    
    adjList[int(indexSource)].append([indexTarget, weight])
    adjList[int(indexTarget)].append([indexSource, weight])
   

 
  return None


def change():
  print(dataIntersections[3])
  for row in dataIntersections:
    row[5] = intersectionID.index(row[5])
    row[6] = intersectionID.index(row[6])

  intersectionID.clear()
  print(dataIntersections[3])
  return None

# Arroja una hora cualquiera al inicializar

def DeclarateTime():
  hour = random.randrange(24)
  minutes = random.randrange(60)

  time = ""

  if hour < 10:
    time += "0" + str(hour) + ":"
  else:
    time += str(hour) + ":"

  if minutes < 10:
    time += "0" + str(minutes)
  else:
    time += str(minutes)

  return time

# Se está aproximando a que: en las horas "puntas" (6 a 10, 12 a 15 y 17 a 21) se manejará con un
# aproximado de 0.75 de horas (45 en minutos) a 3 horas de demora por trafico en calles

def RushHours(rushHour_Weigthed):

  for i in range(24):
    if (i > 5 and i < 10) or (i > 11 and i < 15) or (i > 16 and i < 22): 
      capacity = round(random.uniform(0.75, 3), 2)
    else:
      capacity = round(random.uniform(0.10, 0.3), 2)

    rushHour_Weigthed.append(capacity)


def _dijkstra(G, n, sourceN, targetN):
  visited = [False]*n
  path = [None]*n
  cost = [math.inf]*n
  cost[sourceN] = 0
  queue = [(0, sourceN)]

  while queue:
    g_u, u = hq.heappop(queue)
    print("avanzando")
    if not visited[int(u)]:
      visited[int(u)] = True

      for v, w, in G[int(u)]:
        f = float(g_u) + float(w)

        if f < (cost[int(v)]):
          cost[int(v)] = f
          path[int(v)] = u
          hq.heappush(queue, (f, v))

        if v == targetN and visited[int(u)]:
          return path

  return path

def Dijkstra(G, sourceN, targetN):
  not_end = True
  path = _dijkstra(G, len(G), sourceN, targetN)
  _path = []
  path2 =[]
  while not_end:
    node = path[targetN]
    _path.append([node, targetN])

    if node == sourceN:
      break

  for i in range(len(path)):
    if path[i] != None:
      path2.append(path[i])

  return path2



loadData('/home/amy/Escritorio/Proyectos/Lima_streets.csv', time, dataIntersections, rushHour = True)
intersectionsList(dataIntersections, intersectionList, intersectionID, adjList)
change()
adjl(dataIntersections, adjList)

sourceIndex = intersectionList.index(['-12.0466783', '-77.0430483'])
targetIndex = intersectionList.index(['-12.0466949', '-77.042435'])
path = Dijkstra(adjList, sourceIndex, targetIndex)
print(path)
print("Listo we")
intersectionID.clear()
intersectionList.clear()
adjList.clear()
#print(intersectionList[100])