import random
from Crypto.PublicKey import ECC
from Crypto.Hash import SHA256
import mnemonic
import bip32utils
import base58
import requests
import time

RATE_LIMIT = 10  # Set the rate limit to 10 seconds

def generate_private_key(seed):
    hash_object = SHA256.new(seed)
    key = ECC.construct(curve='P-256', d=int.from_bytes(hash_object.digest(), byteorder='big'))
    return key

def generate_wallet_address(public_key):
    return SHA256.new(public_key.export_key(format='DER')).hexdigest()

def generate_hd_wallet(seed):
    return bip32utils.BIP32Key.fromEntropy(seed)

def get_balance_from_blockchain(wallet_address):
    api_url = f'https://blockchain.info/balance?active={wallet_address}'
    
    try:
        # Introduce rate limiting
        time.sleep(RATE_LIMIT)
        
        response = requests.get(api_url)
        data = response.json()
        # Get the balance directly from the API response
        balance = data.get(wallet_address, {}).get('final_balance', 0)
    except requests.exceptions.RequestException as e:
        # Print the full error message for better debugging
        print(f"Error checking balance for address {wallet_address}: {e}")
        balance = "Couldn't get balance"

    return balance

def shuffle_and_print_words(input_words, num_shuffles):
    generated_patterns = set()

    for _ in range(num_shuffles):
        while True:
            random.shuffle(input_words)
            selected_words = input_words[:12]
            pattern = " ".join(selected_words)

            if pattern not in generated_patterns:
                generated_patterns.add(pattern)
                break
            else:
                print("Duplicate pattern found. Reshuffling...")

        mnemonic_phrase = pattern
        m = mnemonic.Mnemonic("english")
        seed = m.to_seed(mnemonic_phrase, passphrase="")

        hd_wallet = generate_hd_wallet(seed)

        # Iterate only once
        i = 0
        child_key = hd_wallet.ChildKey(44 | 0x80000000).ChildKey(0 | 0x80000000).ChildKey(0 | 0x80000000).ChildKey(0).ChildKey(i)
        private_key = generate_private_key(seed)
        public_key = private_key.public_key()
        wallet_address = generate_wallet_address(public_key)

        # Conversion logic for P2PKH
        p2pkh_address = base58.b58encode_check(bytes.fromhex("00") + bytes.fromhex(wallet_address)).decode('utf-8')

        # Check balance
        balance = get_balance_from_blockchain(p2pkh_address)

        # Print with spacing for better readability
        print(f"\nMnemonic: {mnemonic_phrase}")
        print(f"Address {i+1} - Private Key: {private_key.d}")
        print(f"Public Key: {public_key.export_key(format='DER').hex()}")
        print(f"Wallet Address (P2PKH): {p2pkh_address}")
        print(f"Balance: {balance} Satoshis\n")

def main():
    # Taking input from the user
    input_words = input("\nEnter a list of words separated by spaces: ").split()
    num_shuffles = int(input("Enter the number of times to shuffle the word list: "))

    # Shuffle the entire word list and print private keys, public keys, P2PKH addresses, and balances for the first 12 words
    shuffle_and_print_words(input_words, num_shuffles)

if __name__ == "__main__":
    main()
