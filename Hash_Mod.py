def hash_mod_kume(hash_yapisi):
  maksimum_frekans=-1
  mod=-1
  for key in hash_yapisi.keys():
    print(key,hash_yapisi[key])
    if(hash_yapisi[key] > maksimum_frekans):
      maksimum_frekans=hash_yapisi[key]
      mod=key
  return mod,maksimum_frekans

def hash_mod_liste(hash_yapisi):
  maksimum_frekans=-1
  mod=-1
  for item,frekans in hash_yapisi:
    print(item,frekans)
    if(maksimum_frekans < frekans):
      maksimum_frekans=frekans
      mod=item
  return mod,maksimum_frekans
print(hash_mod_kume({5:2,1:6,2:2,3:1}))
print(hash_mod_liste([(1,2),(2,5),(5,1)]))
