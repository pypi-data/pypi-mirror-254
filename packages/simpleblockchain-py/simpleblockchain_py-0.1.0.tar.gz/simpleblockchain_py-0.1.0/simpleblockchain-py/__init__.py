import hashlib
import time
import json
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes as grb

def get_random_bytes(n):
    return grb(n)

class Block:
    def __init__(self, block_id, previous_hash, timestamp, data, hash, nonce):
        """
        Initialize a new block in the blockchain.

        Parameters:
        - block_id (str): Unique identifier for the block.
        - previous_hash (str): Hash of the previous block in the chain.
        - timestamp (float): Time of block creation.
        - data (str): Data to be stored in the block.
        - hash (str): Hash of the block.
        - nonce (int): Nonce value for proof-of-work.
        """
        self.block_id = block_id
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash
        self.nonce = nonce

def calculate_hash(algorithm, *args):
    """
    Calculate the hash based on the specified algorithm and input arguments.

    Parameters:
    - algorithm (str): Hashing algorithm ('sha256', 'md5').
    - *args: Variable number of arguments for hashing.

    Returns:
    str: Calculated hash.
    """
    block_data = ''.join(map(str, args))
    
    if algorithm not in ['sha256', 'md5']:
        raise ValueError("Invalid hashing algorithm. Supported algorithms: 'sha256', 'md5'.")

    return hashlib.new(algorithm, block_data.encode()).hexdigest()

def encrypt_data(data, key):
    """
    Encrypt data using AES encryption.

    Parameters:
    - data (str): Data to be encrypted.
    - key (bytes): Encryption key.

    Returns:
    str: Hexadecimal representation of the encrypted data.
    """
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data.encode())
    return ciphertext.hex()

def proof_of_work(algorithm, *args, difficulty=4):
    """
    Perform proof-of-work to find a valid nonce that satisfies the specified algorithm and difficulty level.

    Parameters:
    - algorithm (str): Hashing algorithm ('sha256', 'md5').
    - *args: Variable number of arguments for hashing.
    - difficulty (int): Difficulty level for proof-of-work.

    Returns:
    Tuple[int, str]: Nonce and hash that meet the proof-of-work criteria.
    """
    nonce = 0
    while True:
        hash_attempt = calculate_hash(algorithm, *args, nonce)
        if hash_attempt.startswith('0' * difficulty):
            return nonce, hash_attempt
        nonce += 1

class Blockchain:
    def __init__(self, hashing_algorithm='sha256', encryption_key=None):
        """
        Initialize a new blockchain.

        Parameters:
        - hashing_algorithm (str): Hashing algorithm ('sha256', 'md5').
        - encryption_key (bytes): Encryption key for block data.
        """
        if hashing_algorithm not in ['sha256', 'md5']:
            raise ValueError("Invalid hashing algorithm. Supported algorithms: 'sha256', 'md5'.")

        self.chain = []
        self.hashing_algorithm = hashing_algorithm
        self.encryption_key = encryption_key
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        Create the genesis block and add it to the blockchain.
        """
        genesis_block = Block('0', '0', time.time(), 'Genesis Block', '', 0)
        nonce, hash_attempt = proof_of_work(self.hashing_algorithm, genesis_block.block_id, 
                                            genesis_block.previous_hash, genesis_block.timestamp,
                                            genesis_block.data)
        genesis_block.hash = hash_attempt
        genesis_block.nonce = nonce
        self.chain.append(genesis_block)

    def add_block(self, data, block_id=None):
        """
        Add a new block to the blockchain.

        Parameters:
        - data (str): Data to be stored in the block.
        - block_id (str, optional): Unique identifier for the block. If not provided, a default one will be generated.
        """
        if block_id is None:
            block_id = str(len(self.chain))

        if not isinstance(data, str):
            raise TypeError("Block data must be a string.")

        previous_block = self.chain[-1]
        timestamp = time.time()
        nonce, hash_attempt = proof_of_work(self.hashing_algorithm, block_id,
                                            previous_block.hash, timestamp, data)
        new_block = Block(block_id, previous_block.hash, timestamp, data, hash_attempt, nonce)
        
        if self.encryption_key:
            new_block.data = encrypt_data(data, self.encryption_key)

        self.chain.append(new_block)

    def to_json(self):
        """
        Serialize the blockchain to JSON format.

        Returns:
        str: JSON representation of the blockchain.
        """
        return json.dumps([vars(block) for block in self.chain])

    def from_json(self, json_data):
        """
        Deserialize JSON data and reconstruct the blockchain.

        Parameters:
        - json_data (str): JSON representation of the blockchain.
        """
        try:
            blocks = json.loads(json_data)
            self.chain = [Block(block['block_id'], block['previous_hash'], block['timestamp'],
                                block['data'], block['hash'], block['nonce']) for block in blocks]
        except (json.JSONDecodeError, KeyError) as e:
            raise ValueError(f"Error during deserialization: {e}")
