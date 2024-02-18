from .service.ganjigenap import GanjilGenap
from .service.prima import Prima

class DeskripsiAngka:

    def isGanjil(self, angka):
        return GanjilGenap.isGanjil(self, angka)
    
    def isGenap(self, angka):
        return GanjilGenap.isGenap(self, angka)
    
    def isPrima(self, angka):
        return Prima.isPrima(self, angka)