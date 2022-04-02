#Yiska Astuti
#D0219401

class mahasiswa():
    jurusan = "Teknik"
 
    def __init__(self, input_nama):
        self.nama = input_nama # public
 
iska = mahasiswa("Yiska Astuti")

iska.jurusan = "Teknik Informatika"
 
print(mahasiswa.jurusan)
print(iska.jurusan)
