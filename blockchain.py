#!/usr/local/bin/python3

import hashlib
import json
import time


class Blockchain():
    """
    Constructs and manipulates a simple blockchain object
    """

    def __init__(self):
        self.hashes = []
        self.current_txns = []
        self.blockchain = []

        # TODO: create 1st block

    def new_transaction(self, sender, receiver, amount):
        """
        Creates a new transaction that goes into the block queue

        :param sender: <str> account sending funds
        :param receiver: <str> account receiving funds
        :param amount: <int> or <float> amount of funds transferred
        :return: None, appends the transaction to current_txns list
        """
        prev_hash = self.hashes[-1] if len(self.hashes) >= 1 else "0" * 56
        txn = {"Sender": sender,
               "Receiver": receiver,
               "Amount": amount,
               "Timestamp": time.time(),
               "Prev_Hash": prev_hash}

        self.current_txns.append(txn)

    def create_block(self):
        """
        Initiates the verification process

        :param sender: <str>, person sending funds
        :param receiver: <str>, person receiving funds
        :param amount: <int> or <float>, amount of funds transferred
        :return: block
        """
        # TODO: fix logic to use get_hash and current_txns list
        nonce, new_hash = self.generate_hash(txn)

        txn["Nonce"] = nonce
        txn["Hash"] = new_hash
        pass

    def generate_hash(self, txn):
        """
        Generates hash starting with 3 0's based on txn
            transaction
        :param txn: dict with keys for Sender, Receiver,
            Amount, and Previous_Hash
        :return: nonce (random number to meet hash requirements), hash
        """
        nonce = 0
        while True:
            txn["Nonce"] = nonce
            h = json.dumps(txn, sort_keys=True).encode()
            hashy = hashlib.sha224(h).hexdigest()
            if hashy[:3] == "000":
                break
            nonce += 1
        return nonce, hashy

    def get_hash(self, data, algo='sha224'):
        # TODO: Write function to return hashlib hexdigest for given data
        pass


def main():
    pass


if __name__ == '__main__':
    main()
