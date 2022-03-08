#votecoin pythonlib

requirement 
python 3.5 and above 


how to install
(yet to upload it on pypi.org)

ALGOD_ADDRESS = "https://testnet.algoexplorerapi.io"#to work on the mainnet you have to use the mainnet api
headers = {"User-Agent": "header"}
client = algod.AlgodClient("token", ALGOD_ADDRESS, headers)

The above code is used to interact with the algorad blockchain using the library functionalities mentioned below 
#FUNCTIONALITIES
i) validate_escrow_wallet(address: str, mnemonics: str, client) ----> this is used to validate the escrow wallet address before any transaction 

ii) get_balance(address: str, client)----> can be used to request for the wallet address balance

iii) contains_vote_coin(address: str, client) -----> this is used to check if a wallet address contains votecoin before any transaction is sign or approved

iv) create_option_account(escrow_private_key: str, escrow_address: str, client) ----> this can be used to create wallet addresses. for example it can be used to create wallet address for the options to be voted on

v) fund_address(amount: int, recipient_address: str, escrow_address: str,escrow_private_key: str, client)------> this is used to fund a wallet address with vote coin

vi) opt_in_to_vote(private_key: str, address: str, client) -----> opt-in wallet address to vote

vii) questions(escrow_address,mnemonics, client,title,question,duration,category) -----> used to ask questions and reply to this questions. this questions will be stored on the algorand blockchain.
Note it requires a sum of 702 microvotecoin to ask a question

viii) make_vote(sender, key, receiver, amount, comment, client)----> to make a user vote count so it can be calculated at the end of voting session

ix) vote = votee() -----> this is calling the votee class, this class contains all the voting functionalities

i) vote.Trustedlist(address,mnemonics, trusted, untrusted, client)----> adds and removes wallet address to the trustedlists 

ii)vote.vote_del(address,mnemonics, delegate_address, category, delegated_vp)----> voting power delegation
parameters:
address ----> the address of the user willing to delegate his/her voting power
mnemonics ----> account mnemonics
delegate_address ----> the address gaining the voting power
category ----> category were the delegate_address has the voting power
delegated_vp ----> the amount of voting power the address is willing to delegate to the delegate_address

iii) votes(escrow_address,mnemonics,client, votess, option_zero_address = None, option_one_address = None,option_two_address = None)-----> gives the users the ability to vote.
escrow_address ----> users address 
mnemonics ------> users mnemonics
client ------> client
votess ----> user vote ranging from (0 - 2)
option_zero_address -----> first options address
option_one_address ------> second option address
option_second_address -----> third option address

x) calculate_votes(self,addresses: list, client)-----> calculates the number of votes

xi) wait_for_x_secs(delay: float)----> Specify the number of seconds the program should delay for.
xii) winner(option_zero_count, option_one_count, option_two_count)----> Selects a winner based on the result.