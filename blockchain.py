import hashlib

def SHA256(text):
    return hashlib.sha256(text.encode("ascii")).hexdigest()

class Block:
    def __init__(self, previousHash, nonce=0):
        self.previousHash = previousHash
        self.nonce=nonce
        self.string_to_hash = str(previousHash)+str(nonce)
        self.block_hash = SHA256(self.string_to_hash)

    def computed_hash(self):
        block_string = str(self.previousHash)+str(self.nonce)
        self.string_to_hash = block_string
        self.block_hash = SHA256(block_string)
        return SHA256(block_string)
