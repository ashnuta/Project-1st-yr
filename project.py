



import hashlib
from ntpath import join

class AshCoinsBlock:

    def __init__(self, previous_block_hash, transaction_list):
        pass
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

S1=input("Enter First Sender's name:")
print(S1)
R1=input("Enter First Receiver's name:")
print(R1)
t1=int(input("Enter Number of AshCoins sent:"))
print("Ashcoins sent in first transaction are:",t1)
str(t1)

S2=input("Enter Second Sender's name:")
print(S2)
R2=input("Enter Second Receiver's name:")
print(R2)
t2=int(input("Enter number Ashcoins sent:"))
print("Ashcoins sent in second transaction are:",t2)
str(t2)



initial_block = AshCoinsBlock("Initial String", [str(t1),str(t2)])

print(initial_block.block_data)
print(initial_block.block_hash)

S3=input("Enter Third Sender's name:")
print(S3)
R3=input("Enter Third Receiver's name:")
print(R3)
t3=int(input("Enter Number of AshCoins sent:"))
print("Ashcoins sent in third transaction are:",t3)
str(t3)

S4=input("Enter Fourth Sender's name:")
print(S4)
R4=input("Enter Fourth Receiver's name:")
print(R4)
t4=int(input("Enter number Ashcoins sent:"))
print("Ashcoins sent in fourth transaction are:",t4)
str(t4)

second_block = AshCoinsBlock(initial_block.block_hash, [str(t3),str(t4)])

print(second_block.block_data)
print(second_block.block_hash)

S5=input("Enter Fifth Sender's name:")
print(S5)
R5=input("Enter Fifth Receiver's name:")
print(R5)
t5=int(input("Enter Number of AshCoins sent:"))
print("Ashcoins sent in fifth transaction are:",t5)
str(t5)

S6=input("Enter Sixth Sender's name:")
print(S6)
R6=input("Enter Sixth Receiver's name:")
print(R6)
t6=int(input("Enter number Ashcoins sent:"))
print("Ashcoins sent in sixth transaction are:",t6)
str(t6)

third_block = AshCoinsBlock(second_block.block_hash, [str(t5),str(t6)])

print(third_block.block_data)
print(third_block.block_hash)
