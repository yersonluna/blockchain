
import hashlib

class Wallet():
    def __init__(self):
        self.counter = 0

    def generar_nueva_wallet(self):
        wallet = self.counter
        encrypt = hashlib.md5()
        encrypt.update(str(wallet).encode())
        wallet = encrypt.hexdigest()
        self.counter += 1
        print(wallet)
        return wallet 
