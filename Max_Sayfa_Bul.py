#belirli bir sayıdaki kişiler, sayfa sayısı verilmiş bir kitabı okuyor.
#hem Brute force yöntemini kullanarak hem de Brute Force yöntemini kullanmayarak;
#Bu kişilerin, okuduğu ortak sayfa bulunmayan alt kümelerindeki en fazla okunan sayfayı içeren alt kümeyi bulan kod.
import random
from itertools import chain, combinations
#alt küme oluşturma fonksiyonu
def powerset(iterable):
  s=list(iterable)
  return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
#kitap okuyan kişi sınıfı
class Item(object):
  def __init__(self,ilk_sayfa,son_sayfa):
    if(son_sayfa > ilk_sayfa): # if else bloğunda ilk sayfa küçük, son sayfa büyük yapılır
      self.son_sayfa = son_sayfa
      self.ilk_sayfa = ilk_sayfa
    else:
      self.ilk_sayfa = son_sayfa
      self.son_sayfa = ilk_sayfa
    self.okunan_sayfa = self.son_sayfa-self.ilk_sayfa+1
  def getIlkSayfa(self):
    return self.ilk_sayfa
  def getSonSayfa(self):
    return self.son_sayfa
  def getOkunanSayfa(self):
    return self.okunan_sayfa
  def __str__(self):
    result = "("+ str(self.ilk_sayfa)+","+str(self.son_sayfa)+")"
    return result
#Item özelliklerinin daha kolay çağrılması sağlanır
def ilksayfa(item):
  return item.getIlkSayfa()
def sonsayfa(item):
  return item.getSonSayfa()
def okunansayfa(item):
  return item.getOkunanSayfa()
#istenen sayıda kitap okuyan kişi yani Item nesnesi üretilir
#A)
def buildItems(uzunluk=5,sayfa_sayisi=250):
  Items=[]
  for i in range(uzunluk):
    Items.append(Item(random.randint(0,sayfa_sayisi),random.randint(0,sayfa_sayisi)))
  return Items
#En fazla okunan sayfa döndürülür
#B)
def max_okunan_sayfa_bul(items):
  sayfalar={}
  for item in items:
    for sayfa in range(ilksayfa(i),sonsayfa(i)+1): 
      if sayfa in sayfalar:
        sayfalar[sayfa] += 1
      else:
        sayfalar[sayfa] = 1
  en_fazla=0
  en_fazla_okunan_sayfa=0
  for key,value in sayfalar.items():
    if(sayfalar[key] > en_fazla):
      en_fazla = sayfalar[key]
      en_fazla_okunan_sayfa = key
  return en_fazla_okunan_sayfa
#Verilen nesneler için tüm alt kümeler içerisinde ortak sayfa bulundurmayan
#ve toplam okudukları sayfa sayıları en fazla olan alt küme ve max sayfa sayısı döndürülür
#D)
def brute_force(items):
  pset=set(powerset(items))
  MaxSayfa=0
  for items in pset:#alt kumeler tek tek gezilir
    kontrol=0  # kontrol 1 durumu, alt küme içerisinde aynı sayfa olması
    ItemsSayfa=0
    for item in items:#items kumesi icindeki nesneler gezilir
      ItemsSayfa += okunansayfa(item) #nesnenin okuduğu sayfalar, altkümenin toplam sayfasına eklenir
    kontrol=ortak_sayfa_kontrolu(items) #ortak sayfa var mı kontrolü yapılır
    if(kontrol==0 and ItemsSayfa > MaxSayfa): # Ortak sayfa bulunmuyorsa ve sayfa sayısı fazla ise
      MaxSayfa = ItemsSayfa
      MaxSayfaItems=items
  return MaxSayfa,MaxSayfaItems
#Verilen nesneler için, ortak sayfa barındırmayan gruplar arasındaki maximum sayfa sayısını
#ve maximum sayfa sayısına sahip grubu döndürür
#C)
def ortak_sayfasiz_max_sayfa(Kararsizlar, Secilenler=[]):
  ortak_sayfa_var_mi=ortak_sayfa_kontrolu(Secilenler)#varsa 1,yoksa 0 döndürür
  if(ortak_sayfa_var_mi==1): #ortak sayfa varsa hesaba katmamak için 0 döndürülür
    return 0,Secilenler
  elif(Kararsizlar==[]): 
    return topla(Secilenler),Secilenler
  else:
    YeniDizi=Secilenler.copy()
    YeniDizi.append(Kararsizlar[0]) #eleman eklenmiş dizi sol çağrıya gönderilir
    toplam_sol,Secilensol = ortak_sayfasiz_max_sayfa(Kararsizlar[1:],YeniDizi)#left branch
    toplam_sag,Secilensag = ortak_sayfasiz_max_sayfa(Kararsizlar[1:],Secilenler)#right branch
    if(toplam_sol > toplam_sag):
      toplam=toplam_sol
      Secilenler=Secilensol
    else:
      toplam=toplam_sag
      Secilenler=Secilensag
    return toplam,Secilenler
#Ortak sayfa var ise 1, yok ise 0 döndürür 
def ortak_sayfa_kontrolu(secilenler):
  if(secilenler==[]): #boş dizi geldiğinde ortak sayfa yok kabul edilir
    return 0
  for i in range(len(secilenler)):
    for j in range(i,len(secilenler)):
      if(i!=j):
        if(sonsayfa(secilenler[i]) > sonsayfa(secilenler[j])):
          buyuk_sayi_index=i
          kucuk_sayi_index=j
        else:
          buyuk_sayi_index=j
          kucuk_sayi_index=i
        if(ilksayfa(secilenler[buyuk_sayi_index]) <= sonsayfa(secilenler[kucuk_sayi_index])):
          return 1 #ortak sayfa bulundu. 1 döndürülür
  return 0 #hiç ortak sayfa bulunamadı. 0 döndürülür

#verilen nesnelerin okuduğu sayfaların toplamını döndürür
def topla(item_dizi):
  toplam=0
  for item in item_dizi:
    toplam += okunansayfa(item)
  return toplam
#main
items=buildItems() #    A)
print("Okunan sayfalar:")
for i in items: 
  print(i)
print()
print("En fazla okunan  sayfa: "+str(max_okunan_sayfa_bul(items)))    # B)
print()
Max,Taken=brute_force(items) #     D)
print("Brute Force ile cevap: ",Max)
print("Alınanlar:")
for i in Taken:
  print(i)
Max,Taken=ortak_sayfasiz_max_sayfa(items)
print("Ağaç yapısı ile cevap: ",Max) #    C)
print("Alınanlar")
for i in Taken:
  print(i)
