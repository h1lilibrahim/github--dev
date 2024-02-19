def sayıal1():
    sayı1 = int(input("bir sayı girin:\n"))
    return sayı1

def sayıal2():
    sayı2 = int(input("bir sayı daha girin:\n"))
    return sayı2

def konturol(sayı1,sayı2):
    
    s = sayı1
    başlangıç = 0
    
    while s <= sayı2 :
        başlangıç += s
        s += 1
    print(başlangıç)

sayı1 = sayıal1()
sayı2 = sayıal2()
konturol(sayı1,sayı2)