kullanıcı = input("bir ifade girin :\n")
harf = input("hangi ifdeyi aratacaksnız :\n")
adet = kullanıcı.count(harf)

for kul in harf:
 print(kullanıcı,"kelimesinde toplam",harf,"harfinden",adet,"adet","vardır")