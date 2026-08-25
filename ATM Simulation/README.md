# ATM Simulation

A simple Python-based ATM simulation that allows users to securely log in using a username and PIN and perform basic banking operations.

## Features

* User login with PIN authentication
* Maximum 3 incorrect PIN attempts
* Check account balance
* Withdraw money
* Deposit money
* Change PIN
* Quit the ATM system

## Requirements

Python 3.x

No external libraries are required.

## Run

```bash
python atm_simulation.py
```

### Default Login

| Username | PIN  | Balance |
| -------- | ---- | ------: |
| user1    | 1111 |   €1000 |
| user2    | 2222 |   €2000 |
| user3    | 3333 |   €3000 |

## Technologies

* Python
* `getpass` for hidden PIN input
* Basic loops, conditions, lists, and user input
