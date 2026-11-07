# Food Traceability - Manual Test Results

| Test | Result |
|---|---|
| Register a food batch | PASS |
| View batch by ID | PASS |
| List registered batches | PASS |
| Check current batch owner | PASS |
| Transfer batch between accounts | PASS |
| Reject unauthorized transfer | PASS |
| View transfer history | PASS |

## Testing Environment

- Ganache: Local Ethereum blockchain
- Remix IDE: Smart contract deployment and testing
- Python CLI: Application interaction

## Observations

The application successfully registered and retrieved food batches.

Ownership changed after an authorized transfer.

Unauthorized transfers were rejected without crashing the application.

Transfer history displayed sender, receiver, and transaction timestamp.
