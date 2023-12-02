# **HD WALLET ANALYSIS TOOL**
The HD Wallet Analysis Tool is a program that creates detailed information about Bitcoin wallets. It does this by shuffling a list of words, using a specific method for creating wallets, and checking the balances through a Block Explorer API. The tool uses advanced techniques like elliptic curve cryptography and SHA-256 hashing. It also relies on different libraries to manage phrases, create wallets, encode addresses, and make requests to external servers.Users start by entering a list of words. The tool then shuffles these words to create different patterns. For the first 12 patterns, it provides information like phrases, private keys, public keys, unique addresses, and balances.The tool is especially useful because it uses a strategy for creating wallets that involves organized steps. It also converts wallet addresses to a standard Bitcoin format.

To see the tool in action, check the image below:![Tool @ Work](https://github.com/Radiiplus/HD-WALLET-ANALYSER/blob/main/Screenshot_20231202-215635.jpg)

>**Note for Termux Users:**> If you're using Termux, you might face issues installing the pycryptodome library. It's recommended to use a PC, root your device, or use a VPS for a smooth installation.

### Installation Instructions
**Install the following libraries:**
- Pycryptodome- Mnemonic- bip32utils- base58- requests

```pip install pycryptodome mnemonic bip32utils base58 requests```

**Clone this repository:**

[https://github.com/Radiiplus/HD-WALLET-ANALYSER](https://github.com/Radiiplus/HD-WALLET-ANALYSER)

**Run the script using python3.**
> *Future Enhancements:*> The tool is planned to be updated to export wallet information to a file if it identifies a wallet with BTC. For questions or suggestions, contact radiiplus@gmail.com.

*If you find this tool useful, consider supporting its maintenance through a donation.*

**BTC Address:** bc1qdn8rdxjewlujq7c2h6h0cwf2ty4dpjqwaqmzul
