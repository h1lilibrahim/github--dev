def ısıal():
    sıcaklık = float(input("sıcaklık girin\n"))
    return sıcaklık
def konturol(sıcaklık):
    if sıcaklık <= 4 :
        print("soğuk")
    elif sıcaklık <= 14 :
        print ("ılık")
    elif sıcaklık <= 29:
        print("sıcak")
    else :
        print("hava çok sıcak dışarı çıkmanızı savsiye etmem")
sıcaklık = ısıal()
konturol(sıcaklık)