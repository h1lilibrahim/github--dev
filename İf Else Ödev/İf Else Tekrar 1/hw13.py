kullanıcı=input("adınızı giriniz\n")
maaş=int(input("maaşınızı giriniz\n"))
yıl=int(input("çalışma yılınızı giriniz\n"))
zam=0

if yıl  <= 5:
   yıl=maaş*10/100
elif yıl > 6 < 10:
   yıl=maaş*15/100
else:
   yıl=maaş*25/100

print(kullanıcı," zamlı maaşınız  ",(maaş+yıl),"TL")
    