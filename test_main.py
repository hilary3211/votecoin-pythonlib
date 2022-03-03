from algosdk.v2client import algod
from test import (
    calculate_votes,
    create_option_account,
    mnemonic,
    validate_escrow_wallet,
    wait_for_x_secs,
    questions,
    winner,
)
from test import votee
vote = votee()



ALGOD_ADDRESS = "https://testnet.algoexplorerapi.io"
headers = {"User-Agent": "header"}
client = algod.AlgodClient("token", ALGOD_ADDRESS, headers)
def ques():
    #question to be asked
    address = str(input("Enter escrow address: "))
    mnemonics = str(
        input("Enter escrow mnemonic (Each word should be separate by whitespace): ")
    )
    title = str(input('enter title'))
    question = str(input('enter the question'))
    duration = str(input('enter the duration of the message'))
    category = str(input('enter category of te question'))


    is_valid = validate_escrow_wallet(address,mnemonics, client) 
    if not is_valid:
        print("Wallet does not meet the requirements.")
    else:
        questions(address,mnemonics, client,title,question,duration,category)
def main():
    """Entrypoint for the application."""
    escrow_address = str(input("Enter escrow address: "))
    escrow_mnemonic = str(
        input("Enter escrow mnemonic (Each word should be separate by whitespace): ")
    )

    is_valid = validate_escrow_wallet(escrow_address, escrow_mnemonic, client)
    if not is_valid:
        print("Wallet does not meet the requirements.")
    else:
        escrow_private_key = mnemonic.to_private_key(escrow_mnemonic)

        option_one_address = create_option_account(escrow_private_key, escrow_address, client)
        option_zero_address = create_option_account(escrow_private_key, escrow_address, client)

        vote.votes( escrow_address,escrow_mnemonic, option_zero_address, option_one_address, client)

        wait_for_x_secs(5)

        option_one_count, option_zero_count = calculate_votes(
            [option_one_address, option_zero_address], client
        )

        winner(option_zero_count, option_one_count)

def TL():
    address = str(input('enter address'))
    trusted = str(input('enter the trusted address'))
    untrusted = str(input('enter the untrusted address'))
    mnemonics = str(input("Enter  mnemonic (Each word should be separate by whitespace): "))
    is_valid = validate_escrow_wallet(address,mnemonics, client)

    if not is_valid:
        print("Wallet does not meet the requirements.")
    else:
       
        vote.Trustedlist(address,mnemonics, trusted, untrusted, client)
def vote_del():
    address = str(input('enter address')) 
    mnemonics = str(input("Enter  mnemonic (Each word should be separate by whitespace): "))
    category = str(input('enter category'))
    delegate_address = str(input('enter the address you want to delegate your account to'))
    delegated_vp = str(input('enter your ammount of vating power you want to delegate '))
    is_valid = validate_escrow_wallet(address,mnemonics, client)

    if not is_valid:
        print("Wallet does not meet the requirements.")
    else:
        vote.vote_del(address,mnemonics, delegate_address, category, delegated_vp)