# Blockchain-Based Food Supply Chain

A beginner-friendly college project using Python, Flask, SQLite, and a SHA-256 blockchain simulation.

## Features
- Add farmer/distributor/retailer/customer supply-chain records
- Each record becomes a blockchain block
- SHA-256 hash and previous-hash linking
- Blockchain integrity verification
- SQLite database for records
- Simple web interface

## Requirements
Python 3.10+ recommended.

## Installation

Open a terminal in this project folder:

```bash
python -m venv venv
```

Windows:
```bash
venv\Scripts\activate
```

Linux/macOS:
```bash
source venv/bin/activate
```

Install Flask:
```bash
pip install -r requirements.txt
```

## Run

```bash
python app.py
```

Open:
http://127.0.0.1:5000

## Demo
Add records such as:

1. Tomato / TOM-001 / 1000 kg / Chennai Farm / Farmer / Harvested
2. Tomato / TOM-001 / 1000 kg / Chennai Warehouse / Distributor / Received
3. Tomato / TOM-001 / 950 kg / Chennai Retail Store / Retailer / Received
4. Tomato / TOM-001 / 1 kg / Chennai / Customer / Sold

The blockchain is recreated when the Flask server starts, while SQLite stores the records.

## Important note
This is an educational blockchain simulation, not a production Ethereum network. For a larger project, the next step would be adding a real smart contract with Solidity and a local Ethereum development network.
