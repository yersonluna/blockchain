from hashlib import sha256
import random as r
import json

class Block:
    """
    Esta clase se encarga de los blockes del blockchain 
    """
    def __init__(self, id, data, prevHash) -> None:
        self.id = id
        self.nonce = 0
        self.data = data
        self.prevHash = prevHash
        self.hash = ''
    
    def hash_is_valid(self):
        return self.hash.startswith('0000')
    
    def compute_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys = True)
        return sha256(block_string.encode()).hexdigest()

    def mining_hash(self):
        self.nonce = r.randrange(0, 9999)
        self.hash = self.compute_hash()


    def close_block(self):
        while not self.hash_is_valid(): # Mientras el hash sea invalido se minara
            self.mining_hash()
        
    def getHash(self):
        return self.hash
    
    def getId(self):
        return self.id
    
    def get_cantidad_transacciones(self):
        return len(self.data)

    def agregar_transaccion(self, transaccion):
        self.data.append(transaccion)

    def __str__(self) -> str:
        return 'Id: {} \nNonce: {} \nTransacciones: {} \nPrevHash: {} \nHash: {}'.format(
            self.id,
            self.nonce,
            self.data,
            self.prevHash,
            self.hash
        ) 

class Chain:
    """
    Esta clase se encarga de almacenar los bloques
    """
    def __init__(self) -> None:
        self.chain = []
        self.generar_bloque_genesis()
        
    def generar_bloque_genesis(self):
        EMITICION = '0-fabian->10000'
        transaccion_genesis = [EMITICION, ]
        block = Block(1, transaccion_genesis, "0"*64)
        block.close_block()
        self.chain.append(block)

    def agregar_bloque_nuevo(self):
        prevHash = self.chain[-1].getHash()
        prevId = self.chain[-1].getId()
        block = Block(prevId + 1,[] , prevHash)
        self.chain.append(block)


    def agregar_transaccion_en_bloque(self, transaccion):
        #si el bloque esta lleno se cierra y se registra la transaccion en uno nuevo
        
        
        
        if self.chain[-1].get_cantidad_transacciones() == 3: 
            self.chain[-1].close_block()
            self.agregar_bloque_nuevo()
        self.chain[-1].agregar_transaccion(transaccion)
        

    def print_blocks(self):
        for block in self.chain:
            print(block)
            
    def print_block(self, n):
        print(self.chain[n])

if __name__ == '__main__':
    blockchain = Chain()
    blockchain.print_blocks()
    blockchain.agregar_bloque_nuevo()
    blockchain.agregar_transaccion_en_bloque('fabian-camila->1000')
    blockchain.agregar_transaccion_en_bloque('fabian-camila->1000')
    blockchain.agregar_transaccion_en_bloque('fabian-camila->1000')
    blockchain.agregar_transaccion_en_bloque('fabian-camila->1000')
    blockchain.agregar_transaccion_en_bloque('fabian-camila->1000')
    blockchain.agregar_transaccion_en_bloque('fabian-camila->1000')
    blockchain.agregar_transaccion_en_bloque('fabian-camila->1000')
    blockchain.print_blocks()