sayı= int(input("sayıyı girin \n"))
faktoriyel=1
i=1

if sayı >= 0:
        while i <= sayı:
           faktoriyel*=i
           i+=1
        print(sayı,"nın faktoriyeli",faktoriyel)
else:
        print("negatif sayıların faktoriyelı olmaz")