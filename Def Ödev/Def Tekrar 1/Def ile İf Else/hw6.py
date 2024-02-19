def sayı():
    sayı=int(input("bir sayı girin:\n"))
    return sayı

def sayı2(sayı3):
   
    if sayı3 %3 == 0 and sayı3 %5 == 0 :
        print("girdiğiniz sayı 15'e tam bölünür")
    else :
        print("girdiğiniz sayı 15'e tam bölünmüyor")

sayı1 = sayı()
sayı2(sayı1)