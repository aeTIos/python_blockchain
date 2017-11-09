#!/usr/bin/env python3
import hashlib
import time


class Block:
    def __init__(self, index, timestamp, data, previoushash, target):
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

            if int.from_bytes(hashobject.digest()[0:target], byteorder='big') != 0:
                self.nonce += 1
            else:
                self.hash = hashobject.hexdigest()
                break

    def calculate_hash(self, blockdata):
        message = hashlib.sha256()
        message.update(blockdata.encode())
        return message


class Blockchain:
    def __init__(self, target):
        self.chain = []

        self.target = target

        self.chain.append(Block(0, time.time(), 'First block of the chain!',
                                'There is no previous hash', self.target))
        print('Initialized chain!')

    def add_block(self, data):
        self.chain.append(Block(len(self.chain), time.time(), data,
                                self.chain[-1].hash, self.target))



blockchain = Blockchain(1)

while True:
    blockchain.add_block(input('Data to add to chain:'))
    blockchain.target += 1
