import random

x=random.randint(0,20)
while True:
    tahmin=int(input("0-20 arası bir sayı tahmin ediniz\n"))

    if tahmin < x:
        print("daha yüksek bir sayı giriniz")
    elif tahmin > x:
        print("daha düşük bir sayı giriniz")
    else:
        break
print("tebrikler bildiniz")