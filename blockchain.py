import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previoushash, difficulty):
        self.index = index
        self.previoushash = previoushash
        self.timestamp = timestamp
        self.data = data
        self.nonce = 0
        while True:
            hashobject = self.calculate_hash(f'{index}'
                                                  f'{previoushash}'
                                                  f'{timestamp}'
                                                  f'{data}'
                                                  f'{self.nonce}')

            print(hashobject.hexdigest(), "  ", self.nonce)
            if int.from_bytes(hashobject.digest()[0:difficulty], byteorder='big') != 0:
                self.nonce += 1
            else:
                self.hash = hashobject.hexdigest()
                break

    def calculate_hash(self, blockdata):
        message = hashlib.sha256()
        message.update(blockdata.encode())
        return message


class Blockchain:
    def __init__(self):
        # init chain
        self.chain = []
        self.chain_length = 0  # maybe just make this dynamic by returning len(self.chain)  ?

        self.difficulty = 2

        # init genesis block as first block in chain
        self.chain.append(Block(self.chain_length, time.time(), 'First block of the chain!',
                                'There is no previous hash', 2))
        print('initialized chain!')

    def add_block(self, data):
        self.chain.append(Block(len(self.chain), time.time(), data, self.chain[-1].hash,
                                self.difficulty))


# actual program
blockchain = Blockchain()

while True:
    blockchain.add_block(input('data to add to chain:'))
