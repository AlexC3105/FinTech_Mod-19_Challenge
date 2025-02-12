# Cryptocurrency Wallet

################################################################################
# For this Challenge, you will assume the perspective of a KryptoJobs2Go
# customer in order to do the following:

# * Generate a new Ethereum account instance by using your mnemonic seed phrase
# (which you created earlier in the module).

# * Fetch and display the account balance associated with your Ethereum account
# address.

# * Calculate the total value of an Ethereum transaction, including the gas
# estimate, that pays a KryptoJobs2Go candidate for their work.

# * Digitally sign a transaction that pays a KryptoJobs2Go candidate, and send
# this transaction to the Ganache blockchain.

# * Review the transaction hash code associated with the validated blockchain transaction.

# Once you receive the transaction’s hash code, you will navigate to the Transactions
# section of Ganache to review the blockchain transaction details. To confirm that
# you have successfully created the transaction, you will save screenshots to the
# README.md file of your GitHub repository for this Challenge assignment.

################################################################################
# Imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from web3 import Web3
from crypto_wallet import generate_account, get_balance, send_transaction

# Connect to Ganache
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

################################################################################
# KryptoJobs2Go Candidate Information

# Database of KryptoJobs2Go candidates including their name, digital address, rating and hourly cost per Ether.
# A single Ether is currently valued at $1,500
candidate_database = {
    "Lane": [
        "Lane",
        "0x37667E906467542767e5A29c4009F66907c5ea81",
        "4.3",
        0.20,
        "Images/lane.jpeg",
    ],
    "Ash": [
        "Ash",
        "0xFDbFC0A0f012FaA5cc7f5ad2527104b6FDe56135",
        "5.0",
        0.33,
        "Images/ash.jpeg",
    ],
    "Jo": [
        "Jo",
        "0x0db023D88EdE2E22B426373A6044D7058d6960ef",
        "4.7",
        0.19,
        "Images/jo.jpeg",
    ],
    "Kendall": [
        "Kendall",
        "0x75546e8363a1F5b620CC7BD3bF451286254F9cec",
        "4.1",
        0.16,
        "Images/kendall.jpeg",
    ],
}

# A list of the KryptoJobs2Go candidates' first names
people = ["Lane", "Ash", "Jo", "Kendall"]

def get_people():
    """Display the database of KryptoJobs2Go candidate information in a grid format."""
    db_list = list(candidate_database.values())

    # Create two columns for layout
    col1, col2 = st.columns(2)

    # Iterate over candidates and place them in columns
    for index, candidate in enumerate(db_list):
        # Use modulus to alternate columns
        if index % 2 == 0:
            with col1:
                st.image(candidate[4], width=200)
                st.write("Name: ", candidate[0])
                st.write("Ethereum Account Address: ", candidate[1])
                st.write("KryptoJobs2Go Rating: ", candidate[2])
                st.write("Hourly Rate per Ether: ", candidate[3], "eth")
                st.text(" \n")
        else:
            with col2:
                st.image(candidate[4], width=200)
                st.write("Name: ", candidate[0])
                st.write("Ethereum Account Address: ", candidate[1])
                st.write("KryptoJobs2Go Rating: ", candidate[2])
                st.write("Hourly Rate per Ether: ", candidate[3], "eth")
                st.text(" \n")

################################################################################
# Streamlit Code

# Streamlit application headings with custom styling on one line
st.markdown("""
    <div style='text-align: center;'>
        <span style='font-size: 2.0em;'>KryptoJobs2Go!</span>
        <span style='font-size: 1.5em; margin-left: 30px;'>Hire A Fintech Professional!</span>
    </div>
    """, unsafe_allow_html=True)

################################################################################
# Streamlit Sidebar Code - Start

st.sidebar.markdown("## Client Account Address and Ethernet Balance in Ether")

# Step 1 - Part 4: Generate Account
account = generate_account()  # Call the generate_account function

# Write the client's Ethereum account address to the sidebar
st.sidebar.write(f"Address: {account.address}")

# Step 1 - Part 5: Display Account Balance
ether_balance = get_balance(w3, account.address)  # Call get_balance
st.sidebar.write(f"Balance: {ether_balance} Ether")

# Create a select box to choose a FinTech Hire candidate
person = st.sidebar.selectbox("Select a Person", people)

# Create an input field to record the number of hours the candidate worked
hours = st.sidebar.number_input("Number of Hours", min_value=0.0, step=0.25)

st.sidebar.markdown("## Candidate Name, Hourly Rate, and Ethereum Address")

# Identify the FinTech Hire candidate
candidate = candidate_database[person][0]

# Write the KryptoJobs2Go candidate's name to the sidebar
st.sidebar.write(candidate)

# Identify the KryptoJobs2Go candidate's hourly rate
hourly_rate = candidate_database[person][3]

# Write the KryptoJobs2Go candidate's hourly rate to the sidebar
st.sidebar.write(hourly_rate)

# Identify the KryptoJobs2Go candidate's Ethereum Address
candidate_address = candidate_database[person][1]

# Write the KryptoJobs2Go candidate's Ethereum Address to the sidebar
st.sidebar.write(candidate_address)

# Step 2 - Part 1: Calculate the Candidate's Wage
wage = hourly_rate * hours  # Calculate wage by multiplying hourly rate by hours worked

# Write the `wage` calculation to the Streamlit sidebar
st.sidebar.markdown("## Total Wage in Ether")
st.sidebar.write(f"Total Wage: {wage} Ether")

# Step 2 - Part 2: Send Transaction
if st.sidebar.button("Send Transaction"):
    transaction_hash = send_transaction(w3, account, candidate_address, wage)

    # Markdown for the transaction hash
    st.sidebar.markdown("#### Validated Transaction Hash")

    # Write the returned transaction hash to the screen
    st.sidebar.write(transaction_hash)

    # Celebrate your successful payment
    st.balloons()

# The function that starts the Streamlit application
# Writes KryptoJobs2Go candidates to the Streamlit page
get_people()

################################################################################
# Step 3: Inspect the Transaction

# Send a test transaction by using the application’s web interface, and then
# look up the resulting transaction hash in Ganache.

# Complete the following steps:

# 1. From your terminal, navigate to the project folder that contains
# your `.env` file and the `krypto_jobs.py` and `crypto_wallet.py` files.
# Be sure to activate your Conda `dev` environment if it is not already active.

# 2. To launch the Streamlit application,
# type `streamlit run krypto_jobs.py`.

# 3. On the resulting webpage, select a candidate that you would like to hire
# from the appropriate drop-down menu. Then, enter the number of hours that you
# would like to hire them for. (Remember, you do not have a lot of ether in
# your account, so you cannot hire them for long!)

# 4. Click the Send Transaction button to sign and send the transaction with
# your Ethereum account information. If the transaction is successfully
# communicated to Ganache, validated, and added to a block,
# a resulting transaction hash code will be written to the Streamlit
# application sidebar.

# 5. Navigate to the Ganache accounts tab and locate your account (index 0).
# * Take a screenshot of the address, balance, and transaction (TX) count.
# Save this screenshot to the README.md file of your GitHub repository for
# this Challenge assignment.

# 6. Navigate to the Ganache transactions tab and locate the transaction.
# * Click the transaction and take a screenshot of it.
# Save this screenshot to the README.md file of your GitHub repository for
# this Challenge assignment.