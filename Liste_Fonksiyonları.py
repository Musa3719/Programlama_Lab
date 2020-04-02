def liste_lineer_arama(item,liste):
  found=(-1,-1)
  n=len(liste)
  for i in range(n):
    if (item==liste[i]):
      found=(item,i)
      #break ilk indis icin
  return found

def liste_ortalama_deger(liste):
  s,t=0,0
  for item in liste:
    t=t+item
    s=s+1
  return t/s

def liste_sirala(liste):
  n=len(liste)
  for i in range(n-1,-1,-1):
    for j in range(0,i):
      if(liste[j]>liste[j+1]):
        temp=liste[j]
        liste[j]=liste[j+1]
        liste[j+1]=temp
  return liste

def liste_ikili_arama(item,liste):
  sol_index=0
  sag_index=len(liste)-1
  found=(-1,-1)
  while(sol_index <= sag_index):
    orta=(sol_index+sag_index)//2
    if(liste[orta]==item):
      found=(item,orta)
      return found
    elif(liste[orta]>item):
      sag_index=orta-1
    else:
      sol_index=orta+1
  return found

def liste_medyan(liste):
  liste=(liste_sirala(liste))
  n=len(liste)
  if(n%2==1):
    medyan=liste[n//2]
  else:
    medyan_1=liste[n//2-1]
    medyan_2=liste[n//2]
    medyan=(medyan_1+medyan_2)/2
  return medyan

liste=[10,6,3,2,1,15,14,45]
print(liste)
print(liste_lineer_arama(15,liste))
print(liste_ortalama_deger(liste))
liste=(liste_sirala(liste))
print(liste)
print(liste_ikili_arama(45,liste))
print(liste_medyan(liste))