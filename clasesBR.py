class Patios:
    def __init__ (self, areaSocial, medidas, descripcion):
        self.__areaSocial=areaSocial
        self.__medidas=medidas
        self.__descripcion=descripcion

    def getAreaSocial(self):
        return self.__areaSocial
    def getMedidas(self):
        return self.__medidas
    def getDescripcion(self):
        return self.__descripcion
    def setAreaSocial(self, areaSocial):
        self.__areaSocial=areaSocial
    def setMedidas(self, medidas):
        self.__medidas=medidas
    def setDescripcion(self, descripcion):
        self.__descripcion=descripcion
        
class Lavatrastos:
    def __init__(self, depositos, aguaCaliente):
        self.__depositos=depositos
        self.__aguaCaliente=aguaCaliente
        
    def getDepositos(self):
        return self.__depositos
    def getAgiaCaliente(self):
        return self.__aguaCaliente
    def setDepositos(self,depositos):
        self.__depositos=depositos
    def setAgiaCaliente(self, aguaCaliente):
        self.__aguaCaliente=aguaCaliente

class Cocina:
    def __init__(self, electrodomesticos, medidas, materialDes, lavatrastos):
        self.__electrodomesticos=electrodomesticos
        self.__medidas=medidas
        self.__materialDes=materialDes
        self.__lavatrastos=lavatrastos
        
    def getElecrodomesticos(self):
        return self.__electrodomesticos
    def getmedidas(self):
        return self.__medidas
    def getMaterialesDes(self):
        return self.__materialDes
    def getLavatrastos(self):
        return self.__lavatrastos
    def setElecrodomesticos(self, electrodomesticos):
        self.__electrodomesticos=electrodomesticos
    def setmedidas(self,medidas):
        self.__medidas=medidas
    def setMaterialesDes(self, materialesDes):
        self.__materialDes=materialesDes
    def setLavatrastos(self, lavatrastos):
        self.__lavatrastos=lavatrastos
    
    class Cuarto:
        def Cuarto(self, medidas, ventanas):
            