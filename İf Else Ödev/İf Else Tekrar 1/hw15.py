tercih = input("ne tercih edersiniz(sinema-tiyatro):")
öğrenci = input("öğrencimisiniz(e-h):")

if tercih == "sinema" and öğrenci =="h":
    print("ödemeniz gereken ücret 15tl")
elif tercih=="tiyatro" and öğrenci=="h":
    print("ödemeniz gereken ücret 10tl")

if tercih =="sinema" and öğrenci=="e":
    print("ödemeniz gereken ücret7.5tl")
elif tercih== "tiyatro" and öğrenci=="e":
    print("ödemeniz gereken ücret 5tl")
