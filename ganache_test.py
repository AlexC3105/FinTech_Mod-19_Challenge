from web3 import Web3, Account
import os
from dotenv import load_dotenv
from crypto_wallet import generate_account, get_balance

# Load environment variables from the .env file
load_dotenv()

# Enable mnemonic-based account generation
Account.enable_unaudited_hdwallet_features()

def generate_account():
    # Get mnemonic from the .env file
    mnemonic = os.getenv("MNEMONIC")

    # Generate account from mnemonic
    account = Account.from_mnemonic(mnemonic)
    return account

# Set up a connection to the Ganache local blockchain
ganache_url = "http://127.0.0.1:7545"
w3 = Web3(Web3.HTTPProvider(ganache_url))

# Check if connected to Ganache
if w3.is_connected():
    print("Successfully connected to Ganache!")
else:
    print("Failed to connect to Ganache. Please check your setup.")

# Generate an account using the mnemonic from the .env file
account = generate_account()

# Display the account address
print(f"Account Address: {account.address}")

# Check and display the account balance
balance = get_balance(w3, account.address)  # Pass both w3 and account.address
print(f"Account Balance: {balance} Ether")