from block import Block
from wallet import Wallet
from transaccion import Transaccion
from threading import Thread
import time

       

class Blockchain():
    def __init__(self):
        self.blockchain = []
        self.hash_blockchain = ''
        self.amount = 0
        self.block_instanted = Block()
        self.libro_publico = []
        self.generator_wallets = Wallet()

    def __str__(self):
        blocks_list = []
        for block in self.blockchain:
            blocks_list.append(str(block.__str__()))

        return {
                'blockchain':blocks_list,
                'cantidad':len(self.blockchain)
                }

    def verificar_cantidad_transacciones(self):
        return (len(self.block_instanted.transacciones) == 3)


    def agregar_transaccion_bloque(self, transaccion: Transaccion):
        #si el bloque esta lleno se cierra y se registra la transaccion en uno nuevo
        if not self.verificar_cantidad_transacciones():
            self.block_instanted.agregar_transaccion(transaccion)
            if self.verificar_cantidad_transacciones():
                self.close_block()
                self.agregar_bloque_nuevo()
        

    def close_block(self):
        if len(self.blockchain) == 0:
            self.block_instanted.firmar_block()
        else:
            last_block = self.blockchain[-1]
            self.block_instanted.hash_preview = last_block.hash
            self.block_instanted.firmar_block()
            
    def agregar_bloque_nuevo(self):
        self.blockchain.append(self.block_instanted)
        self.block_instanted = Block()
        self.block_instanted.transacciones = []

    def calculate_founds_blockchain(self, wallet):
        amount_wallet = int(0)
        for block in self.blockchain:
            transaction_list = block.get_transaction_list()
            for transaction in transaction_list:
                if wallet == transaction.de_quien:
                    amount_wallet -= int(transaction.monto)
                if wallet == transaction.para_quien:
                    amount_wallet += int(transaction.monto)

            
        return amount_wallet

    def consult_founds_wallet(self, address:str) -> dict:
    
        response = {
                    'exists': False, 
                    'amount': 0
                    }
                   
        if self.account_exists(address):
            response['exists'] = True
            amount = self.calculate_founds_blockchain(address)
            response['amount'] = amount
        
        return response
        

    def generate_wallet(self, name_user):
        
        if not self.user_exists(name_user):
            new_account = self.generator_wallets.generar_nueva_wallet()
            new_user = {'user':name_user,'account':new_account}

            self.libro_publico.append(new_user)

    def user_exists(self, user):
        exists = False
        for user_account in self.libro_publico:
            if user_account['user'] == user:
                exists = True 
        return exists
            
    def account_exists(self, account):
        exists = False

        for user_account in self.libro_publico:
            if user_account['account'] == account:
                exists = True
        return exists
    
    def users(self):
        return self.libro_publico



if __name__ == '__main__':
    blockchain = Blockchain()
    n_threads = 3
    t1 = Transaccion('cfcd208495d565ef66e7dff9f98764da','c4ca4238a0b923820dcc509a6f75849b',12)
    blockchain.agregar_transaccion_bloque(t1)
    # camila andres
    t1 = Transaccion('c4ca4238a0b923820dcc509a6f75849b','c81e728d9d4c2f636f067f89cc14862c',6)
    blockchain.agregar_transaccion_bloque(t1)
    
     # andres fafa
    t1 = Transaccion('c81e728d9d4c2f636f067f89cc14862c','cfcd208495d565ef66e7dff9f98764da',1)
    blockchain.agregar_transaccion_bloque(t1)
    
    # andres fafa
    t1 = Transaccion('c81e728d9d4c2f636f067f89cc14862c','cfcd208495d565ef66e7dff9f98764da',1)
    blockchain.agregar_transaccion_bloque(t1)
    # andres fafa
    t1 = Transaccion('c81e728d9d4c2f636f067f89cc14862c','cfcd208495d565ef66e7dff9f98764da',1)
    blockchain.agregar_transaccion_bloque(t1)
    
    # andres fafa
    t1 = Transaccion('c81e728d9d4c2f636f067f89cc14862c','cfcd208495d565ef66e7dff9f98764da',1)
    blockchain.agregar_transaccion_bloque(t1)
    # andres fafa
    t1 = Transaccion('c81e728d9d4c2f636f067f89cc14862c','cfcd208495d565ef66e7dff9f98764da',1)
    blockchain.agregar_transaccion_bloque(t1)
    while True:
        print("Bienvenidos a Crypto Coca")
        print("Menu de opciones")
        print("1. Crear Bloque")
        print("2. Registrar Data")
        print("3. Consultar fondos")
        print("4. Registrar Transaccion")
        print("5. Consultar Dir")
        print("6. Cerrar Bloque")
        opcion = input("Su respuesta es: ")
        if opcion=="1":
            print("")
        elif opcion=="2":
            print("Registro datos")
        elif opcion=="3":     
                # fafa camila
         
            print("generamos wallet")
            blockchain.generate_wallet('fafa') # cfcd208495d565ef66e7dff9f98764da
            blockchain.generate_wallet('camila') # c4ca4238a0b923820dcc509a6f75849b
            blockchain.generate_wallet('andres') # c81e728d9d4c2f636f067f89cc14862c
            blockchain.generate_wallet('petro') # eccbc87e4b5ce2fe28308fd9f2a7baf3

            camila = blockchain.consult_founds_wallet("c4ca4238a0b923820dcc509a6f75849b")
            print("camilaaaa fondos", camila["amount"])

            andres = blockchain.consult_founds_wallet("c81e728d9d4c2f636f067f89cc14862c")
            print("andres fondos", andres["amount"])
            
        elif opcion=="4":
            print()
        elif opcion=="5":
            
            #print(blockchain.libro_publico)
            list = blockchain.__str__()
         

            print(list)
        elif opcion=="6":
            print("Consultar directorio")
        else:
            print("Elige una respuesta")


   