# FinTech_Mod-19_Challenge
Blockchain Integration

# Background

You work at a startup that’s building a new and disruptive application named KryptoJobs2Go (a fictitious application). Your customers can use KryptoJobs2Go to find fintech professionals from a list of candidates, hire them, and then pay them. As the lead developer, you’ve been tasked with integrating the Ethereum blockchain network into the application. The purpose is to enable the customers to instantly pay their hired fintech professionals with cryptocurrency.

## What You're Creating

The completed `fintech_finder.py` file, which contains the code that’s associated with the web interface of your application. (The included code is compatible with the Streamlit library.) You’ll write all your code for this Challenge in this file.

Note that by using import statements, you’ll integrate the `crypto_wallet.py` Python script into the code in this file. A `README.md` file that includes screenshots to confirm that by assuming the role of a KryptoJobs2Go customer, you successfully created an Ethereum transaction, including the gas estimate, that pays a KryptoJobs2Go candidate for their work.

## Files

Download the following files to help you get started:

- Module 19 Challenge files

## Instructions

The instructions for this Challenge are divided into the following high-level steps:

- Import Ethereum transaction functions into the KryptoJobs2Go application.
- Sign and run a payment transaction.
- Inspect the transaction in Ganache.

### Step 1: Import Ethereum Transaction Functions into the KryptoJobs2Go Application

In this section, you'll import several functions from the `crypto_wallet.py` file into the `fintech_finder.py` file. Note that the latter file contains the code for the customer interface of the KryptoJobs2Go application. And, you’ll import the functions to add wallet operations to this application. In this section, you’ll also assume the role of a KryptoJobs2Go customer (that is, you’ll provide your Ethereum wallet and account information to the application).

To do all this, complete the following steps:

1. Review the code in the `crypto_wallet.py` file. Note that the Ethereum transaction functions that you’ve built throughout this module have been incorporated into Python functions that allow you to automate the process of accessing them. The Ethereum transaction functions include `wallet`, `wallet.derive_acount`, `get_balance`, `fromWei`, `estimateGas`, `sendRawTransaction`, and others.

2. Add your mnemonic seed phrase (which Ganache provided) to the `SAMPLE.env` file. Then rename the file to `.env`.

3. Open the `fintech_finder.py` file. Near the beginning of the file, after the provided import statements, import the following functions from the `crypto_wallet.py` file:
   - `generate_account`
   - `get_balance`
   - `send_transaction`

4. In the Streamlit sidebar section of code, create a variable named `account`. Set this variable equal to a call to the `generate_account` function. Note that this function will create the hierarchical deterministic (HD) wallet and the Ethereum account of the KryptoJobs2Go customer (in this case, you).

5. In the same section of code, define a new `st.sidebar.write` function that displays the balance of the customer account. In this function, call the `get_balance` function, and pass it your Ethereum `account.address`.

### Step 2: Sign and Run a Payment Transaction

In this section, you'll write the code to calculate the wage, in ether, of a fintech professional. The code will base this wage on both the professional’s hourly rate and the number of hours that they worked for a customer. Note that `candidate_database` in `fintech_finder.py` contains the hourly rates.

You’ll then write the code that uses the calculated wage to send a transaction that pays the professional. This code should allow the KryptoJobs2Go customer to authorize the transaction with their digital signature. To test this application, you’ll use your own Ethereum account information as the customer account information.

To do all this, complete the following steps:

1. Note that a KryptoJobs2Go customer will first select a fintech professional candidate from the drop-down menu in the application interface. The customer will then enter the amount of time that they’ll hire the professional for. Code the application so that when a customer completes those steps, it calculates the wage, in ether, that the professional will get paid. To do so, complete the following steps:
   - Write the equation that calculates the candidate’s wage. This equation should get the candidate’s hourly rate from the candidate database (`candidate_database[person][3]`) and then multiply that by the value of the `hours` variable. Save the output of this calculation in a variable named `wage`.
   - Write the `wage` variable to the Streamlit sidebar by using `st.sidebar.write`.

2. Write the code that allows a customer (in this case, you) to send an Ethereum blockchain transaction that pays the hired candidate. To do so, first find the following code: `if st.sidebar.button("Send Transaction")`. Next, add logic to that if statement to send the appropriate information to the `send_transaction` function. To do so, complete the following steps:
   - Call the `send_transaction` function, and pass it the following three parameters:
     - Your Ethereum account information. Recall that this account instance got created when the `generate_account` function was called. And from the account instance, the application will be able to access the `account.address` information that it needs to populate the `from` data attribute in the raw transaction.
     - The `candidate_address` value. Note that this will get created and identified in the sidebar when a customer selects a candidate. It will populate the `to` data attribute in the raw transaction.
     - The `wage` value. This will get passed to the `toWei` function to determine the value, in wei, of the payment in the raw transaction.

3. Save the transaction hash, which the `send_transaction` function returns, as a variable named `transaction_hash`, and then display it in the web interface of the application.

### Step 3: Inspect the Transaction in Ganache

In this section, you’ll test the KryptoJobs2Go application with your newly integrated Ethereum wallet. Specifically, you’ll send a test transaction by using the web interface of the application, and then look up the resulting transaction in Ganache.

To do so, complete the following steps:

1. In the terminal, navigate to the project folder that contains your `.env`, `fintech_finder.py`, and `crypto_wallet.py` files. If your Conda dev environment isn’t already active, activate it.

2. To launch the Streamlit application, type `streamlit run fintech_finder.py`, and then press Enter.

3. On the resulting webpage, on the appropriate drop-down menu, select a candidate that you want to hire. Then enter the number of hours that you want to hire them for. (Remember that you don’t have lots of ether in your account, so you can’t hire them for too long.)

4. Click the `Send Transaction` button to sign and send the transaction with your Ethereum account information. Then navigate to the Transactions section in Ganache and complete the following steps:
   - Take a screenshot of your address balance and history in Ganache. Save this screenshot in the `README.md` file of your GitHub repository for this Challenge assignment.
   - Take a screenshot of the transaction details in Ganache. Save this screenshot in the same `README.md` file.
   - Return to the original transaction, click the `To` address of the transaction, and then complete the following step:
     - Take a screenshot of the recipient’s address balance and history in Ganache. Save this screenshot to the `README.md` file.

## Requirements

### Import Ethereum Transaction Functions into the KryptoJobs2Go Application (30 points)

To receive all points, you must:

- Import the `generate_account`, `get_balance`, and `send_transaction` functions from the `crypto_wallet.py` file into the `fintech_finder.py` file. (10 points)

- Call the `generate_account` function, and store the account object. (10 points)

- Call the `get_balance` function and pass it the Ethereum `account.address`. (10 points)

### Sign and Run a Payment Transaction (20 points)

To receive all points, you must:

- Calculate the transaction’s total wage. (10 points)

- Call the `send_transaction` function, and pass it the `account`, `candidate_address`, and `wage` parameters. (5 points)

- Return the transaction hash from `send_transaction`, and display it in the web interface of the application. (5 points)

### Inspect the Transaction in Ganache (20 points)

To receive all points, you must:

- Send a transaction by using the KryptoJobs2Go application, and then use the returned transaction hash to verify the transaction in Ganache. In the `README.md` file of your GitHub repository for this Challenge assignment, include a screenshot from Ganache of the transaction details. (10 points)

- In your `README.md` file, include two screenshots from Ganache: one of the sender’s address balance and history and another of the recipient's address balance and history. (10 points)

### Coding Conventions and Formatting (10 points)

To receive all points, you must:

- Place imports at the top of the file, just after any module comments and docstrings, and before module globals and constants. (3 points)

- Name functions and variables with lowercase characters, with words separated by underscores. (2 points)

- Follow DRY (Don't Repeat Yourself) principles, creating maintainable and reusable code. (3 points)

- Use concise logic and creative engineering where possible. (2 points)

### Deployment and Submission (10 points)

To receive all points, you must:

- Submit a link to a GitHub repository that’s cloned to your local machine and that contains your files. (4 points)
- Use the command line to add your files to the repository. (3 points)
- Include appropriate commit messages for your files. (3 points)

### Comments (10 points)

To receive all points, your code must:

- Be well commented with concise, relevant notes that other developers can understand. (10 points)