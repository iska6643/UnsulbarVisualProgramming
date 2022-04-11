class Hobby:
  def __init__(self, myhobby, keahlian):
    self.myhobby = myhobby
    self.keahlian = keahlian 

  def printhasil(self):
    print(self.myhobby, self.keahlian)
    
class Hobby_sampingan(Hobby):
  pass

hobbyku = Hobby("Mendengar Musik", "Memasak")
hobbyku.printhasil()
hobbylain = Hobby_sampingan("Menyanyi", "Bemain Gitar")
hobbylain.printhasil()
