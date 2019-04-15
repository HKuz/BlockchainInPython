#!/usr/local/bin/python3

import hashlib
import json
import time


class Blockchain():
    """
    Constructs a simple blockchain object
    """

    def __init__(self):
        self.current_txns = []
        self.blockchain = []

        # Create first block in the chain
        self.create_block()

    def new_transaction(self, sender, receiver, amount):
        """
        Creates a new transaction that goes into the block queue

        :param sender: <str> account sending funds
        :param receiver: <str> account receiving funds
        :param amount: <int> or <float> amount of funds transferred
        :return: <None> appends the transaction to current_txns list
        """
        txn = {
            "Sender": sender,
            "Receiver": receiver,
            "Amount": amount,
            "Timestamp": time.time()
        }

        self.current_txns.append(txn)

    def create_block(self):
        """
        Creates a block for current transactions and adds into the blockchain

        :return: <None> adds bock to internal blockchain
        """
        prev_hash = ('0' * 64 if len(self.blockchain) < 1
                     else self.blockchain[-1]["Current_Hash"])
        data = self.current_txns
        data_hash = self.get_hash(data)

        nonce, current_hash = self.mine_block(prev_hash, data_hash)

        block = {
            "Timestamp": time.time(),
            "Prev_Hash": prev_hash,
            "Transactions": data,
            "Data_Hash": data_hash,
            "Nonce": nonce,
            "Current_Hash": current_hash
        }

        self.current_txns = []
        self.blockchain.append(block)

    def mine_block(self, prev_hash, data_hash):
        """
        Finds the nonce and a hash starting with 3 0's when the previous hash,
            the data hash, and the nonce are hashed together

        :param prev_hash: <str> hash for previous block
        :param data_hash: <str> hash for transaction data going into current
            block
        :return: <tuple> nonce, current hash
        """
        nonce = 0
        while True:
            guess = f'{prev_hash}{data_hash}{nonce}'.encode()
            h = hashlib.sha256(guess).hexdigest()
            if h[:3] == "000":
                break
            nonce += 1

        return nonce, h

    def get_hash(self, data):
        """
        Generates a SHA-256 hash for the given data

        :param data: a block or transaction
        :return: hash for given data
        """
        data_string = json.dumps(data, sort_keys=True).encode()
        return hashlib.sha256(data_string).hexdigest()


def main():
    # Test blockchain
    blockchain = Blockchain()
    print('Gene sends Heather 10')
    blockchain.new_transaction("Gene", "Heather", 10)
    print(f'Current transactions: {blockchain.current_txns}')
    print(f'Blockchain: {blockchain.blockchain}')
    print('Heather sends Jeff 5')
    blockchain.new_transaction("Heather", "Jeff", 5)
    print(f'Current transactions: {blockchain.current_txns}')
    print(f'Blockchain: {blockchain.blockchain}')
    print('Creating a block...')
    blockchain.create_block()
    print(f'Current transactions: {blockchain.current_txns}')
    print(f'Blockchain: {blockchain.blockchain}')


if __name__ == '__main__':
    main()
