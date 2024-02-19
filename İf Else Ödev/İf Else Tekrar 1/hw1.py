sınav1 = int(input("1.sınav notunu girin:\n "))
sınav2 = int(input("2.sınav notunu  girin: \n"))
performans_notu = int (input("performans notunu girin:\n"))

x = (sınav1+sınav2+performans_notu)/3
if x >=50 :
    print("başarılı")
else :
    print("başarısız")