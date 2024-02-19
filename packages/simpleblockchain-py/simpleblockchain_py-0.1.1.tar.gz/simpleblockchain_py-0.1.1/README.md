# simpleblockchain
A simple library to create and manage blockchains easily.

- 🔨 Quickly Customizable
- 💿 JSON Serialization
- 🔒 Proof-Of-Work
- 🔑 SHA-256 and MD5 Hashing


> *Note: MD5 Hashing is not considered secure*
## Functions

### `get_random_bytes(n)`

Generates a random byte string of length `n`.

#### Parameters:

- `n` (int): Length of the random byte string.

#### Returns:

- `bytes`: Random byte string.

### `calculate_hash(algorithm, *args)`

Calculates the hash based on the specified algorithm and input arguments.

#### Parameters:

- `algorithm` (str): Hashing algorithm ('sha256', 'md5').
- `*args`: Variable number of arguments for hashing.

#### Returns:

- `str`: Calculated hash.

### `encrypt_data(data, key)`

Encrypts data using AES encryption.

#### Parameters:

- `data` (str): Data to be encrypted.
- `key` (bytes): Encryption key.

#### Returns:

- `str`: Hexadecimal representation of the encrypted data.

### `proof_of_work(algorithm, *args, difficulty=4)`

Performs proof-of-work to find a valid nonce that satisfies the specified algorithm and difficulty level.

#### Parameters:

- `algorithm` (str): Hashing algorithm ('sha256', 'md5').
- `*args`: Variable number of arguments for hashing.
- `difficulty` (int): Difficulty level for proof-of-work.

#### Returns:

- `Tuple[int, str]`: Nonce and hash that meet the proof-of-work criteria.

## Classes

### `Block` Class

Represents an individual block in the blockchain.

#### Attributes:

- `block_id` (str): Unique identifier for the block.
- `previous_hash` (str): Hash of the previous block in the chain.
- `timestamp` (float): Time of block creation.
- `data` (str): Data to be stored in the block.
- `hash` (str): Hash of the block.
- `nonce` (int): Nonce value for proof-of-work.

#### Methods:

- `__init__(self, block_id, previous_hash, timestamp, data, hash, nonce)`: Initializes a new block.

### `Blockchain` Class

Represents the entire blockchain.

#### Attributes:

- `chain` (list): List of blocks in the blockchain.
- `hashing_algorithm` (str): Hashing algorithm ('sha256', 'md5').
- `encryption_key` (bytes): Encryption key for block data.
- `difficulty` (int): Difficulty level for proof-of-work.

#### Methods:

- `__init__(self, hashing_algorithm='sha256', encryption_key=None, difficulty=4)`: Initializes a new blockchain.
- `create_genesis_block()`: Creates the genesis block and adds it to the blockchain.
- `add_block(data, block_id=None)`: Adds a new block to the blockchain.
- `to_json()`: Serializes the blockchain to JSON format.
- `from_json(json_data)`: Deserializes JSON data and reconstructs the blockchain.

## Example Usage

```python
from simpleblockchain import Blockchain, calculate_hash, encrypt_data, proof_of_work, get_random_bytes
import json

# Create a custom class based on the Blockchain class 
class AcademicBlockchain(Blockchain):
    def __init__(self, institution_name, encryption_key=None, difficulty=4):
        super().__init__(hashing_algorithm='sha256', encryption_key=encryption_key, difficulty=difficulty)
        self.institution_name = institution_name

    def create_academic_record(self, student_name, degree, graduation_year):
        data = {
            'student_name': student_name,
            'degree': degree,
            'graduation_year': graduation_year,
            'institution': self.institution_name
        }

        # Convert data to JSON and encrypt it
        data_json = json.dumps(data)
        encrypted_data = encrypt_data(data_json, self.encryption_key)

        # Add the encrypted academic record to the blockchain
        self.add_block(encrypted_data)

encryption_key = get_random_bytes(16)  # 16 bytes for AES encryption key
university_blockchain = AcademicBlockchain(institution_name='University of Decentralization', encryption_key=encryption_key)

# Create academic records
university_blockchain.create_academic_record("Alice Doe", "Computer Science", 2022)
university_blockchain.create_academic_record("Bob Smith", "Electrical Engineering", 2023)

# Serialize the blockchain for storage or transmission
serialized_data = university_blockchain.to_json()

# ... Store or transmit the serialized_data

# Deserialize the blockchain from stored or transmitted data
new_university_blockchain = AcademicBlockchain(institution_name='University of Decentralization', encryption_key=encryption_key)
new_university_blockchain.from_json(serialized_data)

# Verify academic records
for block in new_university_blockchain.chain:
    decrypted_data = encrypt_data(block.data, new_university_blockchain.encryption_key, decrypt=True)
    print(f"Decrypted Academic Record: {decrypted_data}")
```


