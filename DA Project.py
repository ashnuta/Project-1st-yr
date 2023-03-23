



import hashlib
from ntpath import join

class AshCoinsBlock:

    def __init__(self, previous_block_hash, transaction_list):
        pass
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

t1 = "Aranya sends 2 AC to Anvisha"
t2 = "Raman sends 4.1 AC to Anshul"
t3 = "Aditya sends 3.2 AC to Aditi"
t4 = "Daniel sends 0.3 AC to Franco"
t5 = "Advika sends 1 AC to David"
t6 = "David sends 5.4 AC to Carol"

initial_block = AshCoinsBlock(" ", [t1,t2])

print(initial_block.block_data)
print(initial_block.block_hash)

second_block = AshCoinsBlock(initial_block.block_hash, [t3,t4])

print(second_block.block_data)
print(second_block.block_hash)

third_block = AshCoinsBlock(second_block.block_hash, [t5,t6])

print(third_block.block_data)
print(third_block.block_hash)
