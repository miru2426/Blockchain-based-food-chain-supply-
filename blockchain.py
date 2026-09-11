import hashlib
import json
from datetime import datetime

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        payload = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash
        }, sort_keys=True)
        return hashlib.sha256(payload.encode()).hexdigest()

class FoodBlockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        self.chain.append(Block(0, {"product": "Genesis", "batch_id": "GENESIS"}, "0"))

    def add_food_record(self, product, batch_id, quantity, location, owner, status):
        previous = self.chain[-1]
        data = {
            "product": product,
            "batch_id": batch_id,
            "quantity": quantity,
            "location": location,
            "owner": owner,
            "status": status
        }
        block = Block(len(self.chain), data, previous.hash)
        self.chain.append(block)
        return block

    def verify_chain(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            if current.hash != current.calculate_hash():
                return False
            if current.previous_hash != previous.hash:
                return False
        return True
