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
        Adds current transactions into the blockchain

        :return: <None> adds bock to internal blockchain
        """
        # TODO: fix logic to use get_hash and current_txns list
        nonce, new_hash = self.generate_hash(txn)

        txn["Nonce"] = nonce
        txn["Hash"] = new_hash

    # def generate_hash(self, txn):
    #     """
    #     Generates hash starting with 3 0's based on txn
    #         transaction
    #     :param txn: dict with keys for Sender, Receiver,
    #         Amount, and Previous_Hash
    #     :return: nonce (random number to meet hash requirements), hash
    #     """
    #     nonce = 0
    #     while True:
    #         txn["Nonce"] = nonce
    #         h = json.dumps(txn, sort_keys=True).encode()
    #         hashy = hashlib.sha224(h).hexdigest()
    #         if hashy[:3] == "000":
    #             break
    #         nonce += 1
    #     return nonce, hashy

    def find_valid_hash(self, prev_hash, data_hash):
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
    pass


if __name__ == '__main__':
    main()
