from transaccion import Transaccion
from hashlib import sha256
from random import randrange
import json

class Block():
    '''
    Esta clase se encarga de los blockes del blockchain 
    '''

    number_block_static = 0

    def __init__(self, nonce:int = 0, transacciones:list = [], hash_preview = str('0'*64), hash = ''):

        Block.number_block_static += 1
        self.id = self.number_block_static 
        self.nonce = nonce
        self.transacciones:list = transacciones
        self.hash_preview = hash_preview
        self.hash = hash
    
    def __str__(self):
        
        lista_transacciones = []

        for transaccion in self.transacciones:
            lista_transacciones.append(transaccion.__str__())

        return {
                'block':self.id,
                'nonce':self.nonce,
                'transaccions': str(lista_transacciones),
                'hash_preview': self.hash_preview,
                'hash': self.hash
                }

    def agregar_transaccion(self, transaccion: Transaccion):
        self.transacciones.append(transaccion)

    def hash_is_valid(self):
        return self.hash.startswith('0000')
    
    def compute_hash(self):
        block_string = json.dumps(self.__str__(), sort_keys = True)
        return sha256(block_string.encode()).hexdigest()

    def mining_hash(self):
        self.nonce = randrange(0, 9999)
        self.hash = self.compute_hash()

    def firmar_block(self):
        while not self.hash_is_valid(): # Mientras el hash sea invalido se minara
            self.mining_hash()
    
    def get_transaction_list(self):
        return self.transacciones