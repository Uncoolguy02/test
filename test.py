import bip39
import os
import random
import string

def generate_mnemonic():
    # Generate 128 bits of randomness
    random_bytes = os.urandom(16)

    # Calculate checksum
    checksum = bip39.entropy_to_checksum(random_bytes)

    # Append the first 4 bits of the checksum to the original randomness
    random_bytes += checksum[0:4]

    # Convert the random bytes to a mnemonic phrase
    mnemonic = bip39.bytes_to_mnemonic(random_bytes)

    return mnemonic

# Generate a mnemonic phrase
mnemonic = generate_mnemonic()
print("Mnemonic phrase: ", mnemonic)
