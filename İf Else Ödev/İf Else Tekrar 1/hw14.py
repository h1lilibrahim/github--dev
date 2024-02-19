sayı1 = int(input("1. Sayı: "))
sayı2 = int(input("2. Sayı: "))
sayı3 = int(input("3. Sayı: "))
 
if (sayı1 >= sayı2) and (sayı1 >= sayı3):
   buyuk = sayı1
elif (sayı2 >= sayı1) and (sayı2 >= sayı3):
   buyuk = sayı2
else:
   buyuk = sayı3
 
print(sayı1,",",sayı2,"ve",sayı3,"içinde en büyük olan sayı",buyuk)