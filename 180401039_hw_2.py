import sys
def liste_sirala(liste):
  yeni_liste={}
  while(liste!={}):
    enkucuk=100
    for i in liste:
      if(liste[i] < enkucuk):
        enkucuk=liste[i]
        key=i
    yeni_liste[key]=liste[key]
    del liste[key]
  return yeni_liste

def liste_ortalama_deger(liste):
  s,t=0,0
  for item in liste:
    t+=liste[item]
    s=s+1
  return t/s

def liste_medyan(liste):
  liste=liste_sirala(liste)
  n=len(liste)
  if(n%2==1):
    medyan=n//2
  else:
    medyan1=n//2-1
    medyan2=n//2
    medyan=(medyan1+medyan2)/2
  c=0
  if(medyan==int(medyan)):
    for i in liste:
      if(c==medyan):
        return liste[i]
      else:
        c=c+1
  else:
    flag=0
    medyan=int(medyan)
    for i in liste:
      if(flag==1):
        return (key1+liste[i])/2
      if(c==medyan):
        key1=liste[i]
        flag=1
      else:
        c=c+1

dosya_oku=open(sys.argv[1]+"input_hw_2.csv","r")
satirlar=dosya_oku.readlines()
ayrilis_tarihi_frekans={}
for i in satirlar:
  ayrilis_tarihi=i.split(";")[3]
  ayrilis_ayi=ayrilis_tarihi.split("-")[1]
  ayrilis_ayi=int(ayrilis_ayi)
  if ayrilis_ayi in ayrilis_tarihi_frekans:
    ayrilis_tarihi_frekans[ayrilis_ayi]+=1
  else:
    ayrilis_tarihi_frekans[ayrilis_ayi]=1
ortalama=liste_ortalama_deger(ayrilis_tarihi_frekans)
medyan=liste_medyan(ayrilis_tarihi_frekans)
#print(ortalama,medyan)
dosya_oku.close()
dosya_yaz=open(sys.argv[2]+"180401039_hw_2_output.txt","w")
dosya_yaz.write("Medyan "+str(medyan)+"\nOrtalama "+str(ortalama))
dosya_yaz.close()
