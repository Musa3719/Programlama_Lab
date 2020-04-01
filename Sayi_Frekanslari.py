import random

def n_rastgele_sayi(n=5,min=-5,max=5):
  sayilar=[]
  for i in range(n):
    sayilar.append(random.randint(min,max))
  return sayilar

def hash_sayilar_kume(sayilar):
  frekans_kumesi={}
  for i in sayilar:
    if i in frekans_kumesi:
      frekans_kumesi[i]=frekans_kumesi[i]+1
    else:
      frekans_kumesi[i]=1
  return frekans_kumesi

def hash_sayilar_liste(sayilar):
  frekans_listesi=[]
  for i in range(len(sayilar)):
    s=False
    for j in range(len(frekans_listesi)):
      if(sayilar[i]==frekans_listesi[j][0]):
        frekans_listesi[j][1]=frekans_listesi[j][1]+1
        s=True
    if(s==False):
      frekans_listesi.append([sayilar[i],1])
  return frekans_listesi
sayilar=n_rastgele_sayi()
sayilar=sorted(sayilar)
print(sayilar)
print(hash_sayilar_kume(sayilar))
print(hash_sayilar_liste(sayilar))