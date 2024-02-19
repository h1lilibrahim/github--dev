ağırlık = float(input("Ağırlınızı Girin :\n"))
boy = float(input("Boyunuzu Girin ( metre cinsinden ) örn(*.**) :\n"))

vki = ağırlık / (boy * boy)

if vki <= 18 :
    print("Zayıf")

elif vki >18 and  vki<25 :
    print("Normal")
elif vki >25 and vki<30:
    print("Kilolu")
elif vki >30 and vki<=35:
    print("Obez")
else:
    print("Ciddi Obez")