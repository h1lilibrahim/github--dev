def bavul():
    bagaj = float(input("bagaj ağırlığını giriniz:\n"))
    return bagaj
def konturol(bagaj):
    ekücret=(bagaj - 20)*10
    if bagaj <= 20 :
        print("Herhangi bir ücret ödemeniz gerekmiyor")
    else :
        print("ödemeniz gereken ek ücret: ",ekücret,"TL")
bagaj = bavul()
konturol(bagaj)