class Laptop:
    def __init__(self, inputNama, inputHarga, inputWarna):
        self.nama = inputNama
        self.harga = inputHarga
        self.warna = inputWarna

Laptop1 = Laptop("Hp",5000000,"Hitam")
Laptop2 = Laptop("asus",8000000,"Silver")

print(Laptop2.harga)