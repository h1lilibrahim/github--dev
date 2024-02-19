açı1 = int(input("birinci açıy girin\n"))
açı2 = int(input("ikinci açıy girin\n"))
açı3 = int(input("üçüncü açıy girin\n"))

toplam = açı1 + açı2 + açı3

if toplam == 180 :
    if açı1 == açı2 and açı1 == açı3 and açı2 == açı3 :
        print("eşitkenar")
    elif açı1 == açı2 or açı1 == açı3 or açı2 == açı3 :
        print("ikiz kenar")
    elif açı1 != açı2 != açı3 :
        print(" çeşitkenar üçgendir")
else :
    print("böyle üçgen olamaz")