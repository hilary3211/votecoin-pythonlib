import time

from algosdk import account, mnemonic
from algosdk.encoding import is_valid_address
from algosdk.future.transaction import AssetTransferTxn, PaymentTxn
from database import* 
from trustedlistdb import *
conn()#importing the first database that stores the questions asked buy both the user and questioner 
connt()#importing the second database that stores the trusted list and untrusted list
VOTE_ASSET_ID = 452399768 #vote coin asset id


def validate_escrow_wallet(address: str, mnemonics: str, client) -> bool:
    """Validate an escrow wallet and check it has sufficient funds and is opted in to Vote Coin."""
    if not is_valid_address(address):
        return False

    # compare the address to the address gotten from the mnemonic
    if account.address_from_private_key(mnemonic.to_private_key(mnemonics)) != address:
        return False

    if not contains_vote_coin(address, client):
        return False

    if get_balance(address, client) < 1000:
        return False

    return True


def get_balance(address: str, client):
    """Get the balance of a wallet."""
    account = client.account_info(address)
    return account["amount"]


def contains_vote_coin(address: str, client) -> bool:
    """Checks if the address is opted into Vote Coin."""
    account = client.account_info(address)
    contains_vote = False

    for asset in account["assets"]:
        if asset["asset-id"] == VOTE_ASSET_ID:
            contains_vote = True
            break

    return contains_vote


def create_option_account(escrow_private_key: str, escrow_address: str, client) -> str:
    """Creates an account for option."""

    # This is the amount of Algo to fund the account with. The unit is microAlgos.
    AMOUNT = 1000000
    private_key, address = account.generate_account()

    is_successful = fund_address(AMOUNT, address, escrow_address, escrow_private_key, client)
    if not is_successful:
        raise Exception("Funding Failed!")

    is_optin_successful = opt_in_to_vote(private_key, address, client)
    if not is_optin_successful:
        raise Exception("Vote Coin Opt In Failed!")

    return address


def fund_address(
    amount: int, recipient_address: str, escrow_address: str, escrow_private_key: str, client
) -> bool:
    """Fund an account with Algo."""
    suggested_params = client.suggested_params()
    unsigned_transaction = PaymentTxn(
        escrow_address,
        suggested_params,
        recipient_address,
        amount,
        note="Initial Funding for Decision Creation"
    )
    signed_transaction = unsigned_transaction.sign(escrow_private_key)
    transaction_id = client.send_transaction(signed_transaction)

    return True


def opt_in_to_vote(private_key: str, address: str, client) -> bool:
    """Opt in a wallet to Vote Coin."""

    suggested_params = client.suggested_params()
    if not contains_vote_coin(address, client):
        unsigned_transaction = AssetTransferTxn(
            address, suggested_params, address, 0, VOTE_ASSET_ID
        )
        signed_transaction = unsigned_transaction.sign(private_key)
        transaction_id = client.send_transaction(signed_transaction)

    return True
def questions(escrow_address,mnemonics, client,title,question,duration,category):
    title_split = title.split()
    question = question.split()
    category = category.split()

    if len(title_split) < 1:
        print("The minimum title length is 1")

    elif len(title_split) > 50:
        print("You have exceeded the title limit of 50 characters")
    
    elif len(question) < 1:
        print("The minimum question number is 1")

    elif len(question) > 500:
        print('you have exceeded the maximum wordlength of 500 for questions')

    elif duration < 1:
        print('minimum duration for question')
    elif duration > 1000000:
        print('exceeded the maximum duration integer of 1000000')

    elif len(category) < 1:
        print('The minimum wordlength for category is 1')
    elif len(category) >50:
        print('maximum wordlength for category is 50')
    private_key = mnemonic.to_private_key(mnemonics)
    if not contains_vote_coin(escrow_address,client):
        suggested_params = client.suggested_params()
        unsigned_transaction = AssetTransferTxn(
                escrow_address,
                suggested_params,
                escrow_address,
                702,
                VOTE_ASSET_ID,
                note = question
            )
        signed_transaction = unsigned_transaction.sign(private_key)
        transaction_id = client.send_transaction(signed_transaction)

    insert(escrow_address,title,question,category)

    
def make_vote(sender, key, receiver, amount, comment, client):
    """Sends the transaction"""
    parameters = client.suggested_params()
    transaction = AssetTransferTxn(
        sender, parameters, receiver, amount, VOTE_ASSET_ID, note=comment
    )

    signature = transaction.sign(key)
    client.send_transaction(signature)

    txn_id = transaction.get_txid()
    return txn_id
class votee():
    def Trustedlist(self,address,mnemonics, trusted, untrusted, client):
        self.address = address
        self.trusted = trusted
        self.untrusted = untrusted
        self.client = client
        self.mnemonics = mnemonics
        trusted = self.trusted.split()
        untrusted = self.untrusted.split()

        if len(trusted) < 1:
            print('wordlength less than 1')
        elif len(untrusted) > 60:
            print('wordlength is greater 60')
        private_key = mnemonic.to_private_key(self.mnemonics)
        if not contains_vote_coin(self.address,client):
            suggested_params = client.suggested_params()
            unsigned_transaction = AssetTransferTxn(
                    self.address,
                    suggested_params,
                    self.address,
                    705,
                    VOTE_ASSET_ID,
                    note = str([trusted,untrusted])
                )
            signed_transaction = unsigned_transaction.sign(private_key)
            transaction_id = client.send_transaction(signed_transaction)
        insert(self.trusted, self.untrusted)
        self.all_list = [trusted,untrusted]
    def vote_del(self,address,mnemonics, delegate_address, category, delegated_vp):
        self.address = address
        self.delegate_address = delegate_address
        self.category = category
        self.delegated_vp = delegated_vp
        self.mnemonics = mnemonics
        ad1_vp = 100
        ad2_vp = 100
        if self.all_list[1] == self.address:
            print('This address is untrusted and has been added to the untrusted list')
        else:
            for i in range(100):
                if i == self.delegated_vp:
                    self.ad1_vp = ad1_vp - i
                    self.ad2_vp = ad2_vp + i
            private_key = mnemonic.to_private_key(self.mnemonics)
            del_list = str([delegate_address,self.ad2_vp])
            if not contains_vote_coin(self.address,self.client):
                    suggested_params = self.client.suggested_params()
                    unsigned_transaction = AssetTransferTxn(
                            self.address,
                            suggested_params,
                            self.address,
                            701,
                            VOTE_ASSET_ID,
                            note = del_list
                        )
                    signed_transaction = unsigned_transaction.sign(private_key)
                    transaction_id = self.client.send_transaction(signed_transaction)
        
    def votes(self, escrow_address,mnemonics, option_zero_address, option_one_address,option_two_address, client, votess):#"Vote 0 for zero and vote 1 for one: "
        """Places a vote based on the input of the user."""
        self.escrow_address = escrow_address
        self.option_zero_address = option_zero_address
        self.option_one_address = option_one_address
        self.option_two_address = option_two_address
        self.mnemonics = mnemonics
        self.votess = votess
        self.client = client
        private_key = mnemonic.to_private_key(self.mnemonics)
        if self.all_list[1] == self.address:
            print('This address is untrusted and has bee added to the untrusted list')
        else:
            if self.votes == 0:
                make_vote(
                    self.escrow_address,
                    private_key,
                    self.option_zero_address,
                    703,
                    "Voting Powered by Vote Coin.",
                    self.client
                )
                print("Thanks for voting for zero.")
            elif self.votes == 1:
                make_vote(
                    self.escrow_address,
                    private_key,
                    self.option_one_address,
                    703,
                    "Voting Powered by Vote Coin.",
                    self.client
                )
                print("Thanks for voting for one.")
            elif self.votes == 2:
                make_vote(
                    self.escrow_address,
                    private_key,
                    self.option_two_address,
                    703,
                    "Voting Powered by Vote Coin.",
                    self.client
                )
                print("Thanks for voting for two.")
    def calculate_votes(self,addresses: list, client):
        """Calculate the result of a voting process."""
        results = []
        for addr in self.addresses:
            account_info = self.client.account_info(addr)
            assets = account_info.get("assets")

            for _asset in self.assets:
                if _asset["asset-id"] == VOTE_ASSET_ID:
                    amount = _asset.get("amount")
                    results.append(amount)

        return results

def wait_for_x_secs(delay: float) -> None:
    """Specify the number of seconds the program should delay for."""

    # A block takes approximately four(4) seconds to be added to the blockchain on Algorand
    print(f"Waiting for {delay} second(s) for blockchain to sync...")

    time.sleep(delay)
def winner(option_zero_count, option_one_count):
    """Selects a winner based on the result."""
    if option_zero_count > option_one_count:
        print("Option zero wins.")
    else:
        print("Option one wins.")


