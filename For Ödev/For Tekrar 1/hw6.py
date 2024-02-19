sayi1=int(input("1.sayıyı Girin : "))
sayi2=int(input("2.sayıyı Girin : "))
 
toplam=0
for s in range(sayi1,sayi2+1):
  toplam+=s
 
sayı = toplam / (sayi2-sayi1 + 1)
print("Sayıların Ortalaması: ",(sayı))
