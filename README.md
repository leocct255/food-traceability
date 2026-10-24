# Food Traceability Using Blockchain

A food traceability prototype developed for the Distributed Digital Transactions module.

The application uses a Solidity smart contract to register food batches on a local Ethereum blockchain. A Python command-line interface allows users to register and retrieve food information.

## Technologies

- Solidity 0.8.19 — Smart contract
- Ganache — Local Ethereum blockchain
- Python — Command-line application
- Web3.py — Communication between Python and blockchain
- Shell Script — Application startup automation
- Git and GitHub — Version control
## How to Run the Project

### 1. Install Dependencies

Requirements:
- Python 3
- Node.js and npm
- Git

Install Ganache:

```bash
npm install
```

Create and activate a Python virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
pip install web3
```

### 2. Start the Blockchain

Open a terminal in the project directory:

```bash
npx ganache
```

Keep this terminal running.

### 3. Deploy the Smart Contract

1. Open Remix IDE.
2. Load `contracts/FoodTraceability.sol`.
3. Compile using Solidity 0.8.19.
4. Connect Remix to Ganache at `http://127.0.0.1:8545`.
5. Deploy the `FoodTraceability` contract.
6. Copy the deployed contract address.
7. Update `CONTRACT_ADDRESS` in `app.py`.

### 4. Run the Application

Open another terminal in the project directory:

```bash
./run.sh
```

The application provides four options:

1. Register a food batch.
2. View a batch by ID.
3. List all registered batches.
0. Exit.

**Note:** Ganache must remain running while using the application. Without blockchain persistence, restarting Ganache requires deploying the contract again.
