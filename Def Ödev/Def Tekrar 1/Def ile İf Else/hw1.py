def notal1():
    not1 = int(input("1. sınav notunuzu girin :\n"))
    return not1

def notal2():
    not2 = int(input("2. sınav notunu girin :\n"))
    return not2

def notal3():
    
    
    return not3

def konturol(not1,not2,not3):
    ort = (not1 + not2+ not3)/3
    print(ort,"\n")
    if ort >= 50:
     print("başarılı")
    else :
       print("başarasız")

not1= notal1()
not2 = notal2()
not3 = notal3()
konturol(not1,not2,not3)