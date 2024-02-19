sayı1 = int (input("bir sayı girin\n"))
sayı2 = int (input("ikinci sayı girin\n"))
başlangıç = 0
s = sayı1

for s  in range(sayı1,sayı2) :
 başlangıç += s
s += 1
print (başlangıç)