
from fun import *
from classes import *

while True:
    
    a = Makanan.getDaftarBuah()

    ambil = int(input("Ambil buah : "))
    
    b = Makanan.getBuah(ambil)
    print(b)
    info = input("Cek info? (y/n) : ")
    
    if info == "y":
        Makanan.getDetail(b)
            