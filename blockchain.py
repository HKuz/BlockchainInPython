#!/usr/local/bin/python3

import hashlib
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
        """
        prev_hash = self.hashes[-1] if len(self.hashes) >= 1 else "0" * 56
        txn = {"Sender": sender,
               "Receiver": receiver,
               "Amount": amount,
               "Prev_Hash": prev_hash}

        # TODO: generate hash for current transaction

        return txn

    def generate_hash(self, txn):
        """
        Generates appropriate hash (one starting with 3 0's) for given
            transaction
        :param txn: dict with keys for Sender, Receiver,
            Amount, and Previous_Hash
        :return: nonce (random number to meet hash requirements), hash
        """
        while True:
            nonce = random.randint(0, 10**10)
            txn["Nonce"] = nonce
            h = hashlib.sha224(bytes(txn))
            hashy = h.hexdigest()
            if hashy[:3] == "000":
                break
        return nonce, hashy


def main():
    pass


if __name__ == '__main__':
    main()
