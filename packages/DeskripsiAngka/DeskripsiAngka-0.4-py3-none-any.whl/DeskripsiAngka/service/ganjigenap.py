class GanjilGenap:
    
    def isGanjil(self, angka) -> bool:
        if angka % 2 == 0:
            self.hasil = False
        else:
            self.hasil = True
        return self.hasil
    
    def isGenap(self, angka) -> bool:
        if angka % 2 == 0:
            self.hasil = True
        else:
            self.hasil = False
        return self.hasil