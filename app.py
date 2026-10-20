import json
from pathlib import Path
from datetime import datetime, timezone
from web3 import Web3


GANACHE_URL = "http://127.0.0.1:8545"


CONTRACT_ADDRESS = Web3.to_checksum_address(
   "0x933b4Cab0b38C7367e6Ea8Bdc081B9eb813E319C"
)


ABI_PATH = Path(__file__).parent / "contracts" / "FoodTraceability_abi.json"


def connect_contract():
    web3 = Web3(Web3.HTTPProvider(GANACHE_URL))

    if not web3.is_connected():
        raise ConnectionError("Could not connect to Ganache.")

    with open(ABI_PATH, "r", encoding="utf-8") as file:
        abi = json.load(file)

    if not web3.eth.get_code(CONTRACT_ADDRESS):
        raise RuntimeError("Smart contract not found at this address.")

    contract = web3.eth.contract(
        address=CONTRACT_ADDRESS,
        abi=abi
    )

    account = web3.eth.accounts[0]

    return web3, contract, account


def register_batch(contract, account):
    name = input("Food name: ").strip()
    producer = input("Producer: ").strip()
    origin = input("Origin: ").strip()

    if not name or not producer or not origin:
        print("All fields are required.")
        return

    batch_id = contract.functions.nextBatchId().call()

    transaction_hash = contract.functions.registerBatch(
        name,
        producer,
        origin
    ).transact({"from": account})

    receipt = Web3  # Temporary reference removed below
    receipt = contract.w3.eth.wait_for_transaction_receipt(
        transaction_hash
    )

    if receipt.status == 1:
        print("\nBatch registered successfully!")
        print("Batch ID:", batch_id)
        print("Transaction hash:", transaction_hash.hex())
    else:
        print("Registration failed.")


def display_batch(contract, batch_id):
    next_id = contract.functions.nextBatchId().call()

    if batch_id < 1 or batch_id >= next_id:
        print("Batch not found.")
        return

    name = contract.functions.batchNames(batch_id).call()
    producer = contract.functions.batchProducers(batch_id).call()
    origin = contract.functions.batchOrigins(batch_id).call()
    timestamp = contract.functions.batchTimestamps(batch_id).call()

    date = datetime.fromtimestamp(
        timestamp, timezone.utc
    ).strftime("%d-%m-%Y %H:%M:%S UTC")

    print(f"\nBatch ID: {batch_id}")
    print(f"Food: {name}")
    print(f"Producer: {producer}")
    print(f"Origin: {origin}")
    print(f"Registered at: {date}")


def list_batches(contract):
    next_id = contract.functions.nextBatchId().call()

    if next_id == 1:
        print("No food batches registered.")
        return

    for batch_id in range(1, next_id):
        display_batch(contract, batch_id)
        print("-" * 30)


def main():
    try:
        web3, contract, account = connect_contract()
        print("Connected to Ganache and FoodTraceability!")
    except Exception as error:
        print("Connection error:", error)
        return

    while True:
        print("\n=== FOOD TRACEABILITY ===")
        print("1 - Register food batch")
        print("2 - View batch by ID")
        print("3 - List all batches")
        print("0 - Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            try:
                register_batch(contract, account)
            except Exception as error:
                print("Registration error:", error)

        elif choice == "2":
            try:
                batch_id = int(input("Enter batch ID: "))
                display_batch(contract, batch_id)
            except ValueError:
                print("Please enter a valid number.")
            except Exception as error:
                print("Could not retrieve batch:", error)

        elif choice == "3":
            try:
                list_batches(contract)
            except Exception as error:
                print("Could not list batches:", error)

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
