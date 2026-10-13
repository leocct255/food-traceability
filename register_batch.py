import json
from pathlib import Path
from web3 import Web3

# Connect to Ganache
web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

# Smart contract address
contract_address = Web3.to_checksum_address(
    "0x0067e5A03AfDdffd84FF518a941aa088492fc508"
)

# Load ABI
abi_path = Path(__file__).parent / "contracts" / "FoodTraceability_abi.json"

with open(abi_path, "r", encoding="utf-8") as file:
    abi = json.load(file)

if not web3.is_connected():
    raise SystemExit("Connection to Ganache failed!")

# Connect to the contract
contract = web3.eth.contract(
    address=contract_address,
    abi=abi
)

# Use the first Ganache account
account = web3.eth.accounts[0]

# Get information from the user
name = input("Food name: ").strip()
producer = input("Producer: ").strip()
origin = input("Origin: ").strip()

if not name or not producer or not origin:
    raise SystemExit("All fields are required!")

# Get the ID for the new batch
batch_id = contract.functions.nextBatchId().call()

# Send the transaction
tx_hash = contract.functions.registerBatch(
    name,
    producer,
    origin
).transact({"from": account})

# Wait for the transaction to be mined
receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

if receipt.status == 1:
    print("\nFood batch registered successfully!")
    print("Batch ID:", batch_id)
    print("Transaction hash:", tx_hash.hex())
    print("Food name:", contract.functions.batchNames(batch_id).call())
    print("Producer:", contract.functions.batchProducers(batch_id).call())
    print("Origin:", contract.functions.batchOrigins(batch_id).call())
else:
    print("Transaction failed!")
