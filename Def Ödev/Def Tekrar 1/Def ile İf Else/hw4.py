def ürünal1():
    ürün1 = int(input("birinci ürünün fiyatını girin:\n"))
    return ürün1

def ürünal2():
    ürün2 = int(input("ikinci ürünün fiyatını girin\n"))
    return ürün2

def konturol (ürün1,ürün2):
    toplam = ürün1 + ürün2
    indirim = toplam * 0.75
    if toplam <= 200 :
        print("ödemeniz gereken fiyat:",toplam)
    else :
        print("ödemeniz gereken fiyat indirimden önce:",toplam,"indirimden sonra",indirim,"TL")
ürün1 = ürünal1()
ürün2 = ürünal2()
konturol(ürün1,ürün2)