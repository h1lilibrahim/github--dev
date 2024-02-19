def işlemcial():
    islemci = input("işlemcinizi girin:\n")
    return islemci

def ramal(): 
    ram = float(input("reminizi girin:\n"))
    return ram


def pc (islemci,ram):
    if islemci >= "i7" and ram >= 8 :
        print("kuruluma uygun")
    else :
        print("kuruluma uygun değil")

işlemci = işlemcial() 
ram = ramal()
pc(işlemci,ram)