def açıal1():
    üçgen1 = int(input("birinci açıyı girin:\n"))
    return üçgen1

def açıal2():
    üçgen2 = int(input("ikinci açıy girin:\n"))
    return üçgen2

def açıal3():
    üçgen3 = int(input("üçüncü açıyı girin:\n"))
    return üçgen3

def konturol(üçgen1,üçgen2,üçgen3):
    toplam = (üçgen1+üçgen2+üçgen3)==180
    print(toplam)
    
    if toplam :
        print("bu bir üçgendir")
    else :
        print("bu bir üçgen değildir")

üçgen1 = açıal1()
üçgen2 = açıal2()
üçgen3 = açıal3()
konturol(üçgen1,üçgen2,üçgen3)