import math
class Prima:
    def isPrima(self, angka) -> bool:
        if angka < 2:
            self.hasil = False
        elif angka == 2:
            self.hasil = True
        elif angka % 2 == 0:
            self.hasil = False
        else:
            # Check divisibility starting from 3 up to the square root of n, with steps of 2
            for i in range(3, int(math.sqrt(angka)) + 1, 2):
                if angka % i == 0:
                    self.hasil = False
            self.hasil = True
        return self.hasil
