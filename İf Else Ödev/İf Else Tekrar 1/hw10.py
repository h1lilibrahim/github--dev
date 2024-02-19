saat = int(input("kaç saat kaldığınızı giriniz "))

saat1 = saat*4

saat2 = saat*3

if saat <= 1 :
    print("ücret : 5tl")
elif 1 < saat < 5 :
    print("ücret :",saat1)
else :
    print("ücret : ",saat2)