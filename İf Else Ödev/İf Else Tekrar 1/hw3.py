kg = float(input("bagaj ağırlınızı girin\n"))

ekücret = (kg - 20) * 10
if kg <= 20 :
    print("Herhangi bir ücret ödemeniz gerekmiyor")
else:
    print("ek ücret",ekücret,"TL")