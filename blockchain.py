#!/usr/local/bin/python3

import hashlib
import json
import random


class Blockchain():
    """
    Constructs and manipulates a simple blockchain object
    """

    def __init__(self):
        self.hashes = []
        self.transactions = []

    def add_transaction(self, sender, receiver, amount):
        """
        Creates a new transaction object

        :param sender: string, person sending funds
        :param receiver: string, person receiving funds
        :param amount: number, amount of funds transferred
        :return: None, updates internal transactions and hashes lists
        """
        prev_hash = self.hashes[-1] if len(self.hashes) >= 1 else "0" * 56
        txn = {"Sender": sender,
               "Receiver": receiver,
               "Amount": amount,
               "Prev_Hash": prev_hash}

        # TODO: generate hash for current transaction
        nonce, new_hash = self.generate_hash(txn)

        txn["Nonce"] = nonce
        txn["Hash"] = new_hash
        self.hashes.append(new_hash)
        self.transactions.append(txn)

    def generate_hash(self, txn):
        """
        Generates hash starting with 3 0's based on txn
            transaction
        :param txn: dict with keys for Sender, Receiver,
            Amount, and Previous_Hash
        :return: nonce (random number to meet hash requirements), hash
        """
        while True:
            nonce = random.randint(0, 10**10)
            txn["Nonce"] = nonce
            h = json.dumps(txn, sort_keys=True).encode()
            hashy = hashlib.sha224(h).hexdigest()
            if hashy[:3] == "000":
                break
        return nonce, hashy


def main():
    pass


if __name__ == '__main__':
    main()
