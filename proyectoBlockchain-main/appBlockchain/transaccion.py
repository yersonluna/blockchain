class Transaccion():
    '''
    Son las transacciones que se van a guardar
    en los bloques
    '''

    def __init__(self, de_quien, para_quien, monto):
        self.de_quien = de_quien
        self.para_quien = para_quien
        self.monto = monto

    def __str__(self):
        # return "de {}, para {}, monto {}".format(self.de_quien, self.para_quien, self.monto)

        return {
                'de':self.de_quien,
                'para':self.para_quien,
                'monto':self.monto
                }
    
    def get_monto(self):
        return self.monto

    def get_de_quien(self):
        return self.de_quien
    
    def get_para_quien(self):
        return self.para_quien