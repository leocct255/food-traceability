import json
from pathlib import Path
from web3 import Web3

# Connect to Ganache
ganache_url = "http://127.0.0.1:8545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Deployed smart contract address
contract_address = Web3.to_checksum_address(
    "0x0067e5A03AfDdffd84FF518a941aa088492fc508"
)

# Load the contract ABI
abi_path = Path(__file__).parent / "contracts" / "FoodTraceability_abi.json"

with open(abi_path, "r", encoding="utf-8") as file:
    abi = json.load(file)

# Check the connection
if not web3.is_connected():
    print("Connection to Ganache failed!")
    raise SystemExit(1)

# Check that the contract exists at this address
if len(web3.eth.get_code(contract_address)) == 0:
    print("No contract found at this address!")
    raise SystemExit(1)

# Connect Python to the smart contract
contract = web3.eth.contract(
    address=contract_address,
    abi=abi
)

# Read data from the blockchain
next_id = contract.functions.nextBatchId().call()
batch_name = contract.functions.batchNames(1).call()

print("Connected to Ganache!")
print("Connected to FoodTraceability contract!")
print("Next batch ID:", next_id)
print("Name of batch 1:", batch_name)
