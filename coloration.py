def coloration(matrice_adj):
  #premièrement on transforme la matrice d'adjacence a un dictionnaire de façons que les sommets sont les clés et ses voisins sont les valeurs
  graph={}
  ch="abcdefghijklmnopqrstuvwxyz"
  for i in range (len(matrice_adj)):
      liste=[]
      for j in range(len(matrice_adj[0])):
          if matrice_adj[i][j] == 1:
              liste.append(ch[j])
          graph[ch[i]] = liste
                    
  # Ordonner les sommets en degré décroissant
  sommets = sorted(list(graph.keys()), key=lambda x: len(graph[x]), reverse=True)
  s=[]
  for k in graph:
        if k not in s:
          s.append(k)
        for i in graph[k]:
            if i not in s:
              s.append(i)
  couleur_liste = {}
  couleur_actuelle = 1
  for sommet in sommets:
    if sommet not in couleur_liste:
      couleur_liste[sommet] = "C"+str(couleur_actuelle)
    for sommet2 in s:
      if sommet in graph and sommet2 not in graph[sommet] and sommet2 not in couleur_liste:
        couleur_liste[sommet2] = "C"+str(couleur_actuelle)
    if "C"+str(couleur_actuelle) in couleur_liste.values():
      couleur_actuelle +=1         
  return couleur_liste
