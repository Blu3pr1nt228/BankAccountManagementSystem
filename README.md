# Bank Account Management System

## Description
This is a simple bank account management system implemented using Object-Oriented Programming (OOP) principles in Python. It allows users to create bank accounts, perform transactions, and view account details.

## BankAccount Class

### Attributes
- `accountNumber` (string): Unique identifier for the bank account.
- `accountHolder` (string): Name of the account holder.
- `balance` (float): Current balance of the account.

### Methods
- `__init__(self, accountNumber, accountHolder, initialBalance)`: Initializes the bank account with the given details.
- `deposit(self, amount)`: Deposits the specified amount into the account.
- `withdraw(self, amount)`: Withdraws the specified amount from the account. Prints an error if the amount exceeds the balance.
- `getBalance(self)`: Returns the current balance of the account.
- `displayAccountInfo(self)`: Displays the account number, account holder name, and current balance.

## Running the Program

1. Clone the repository or download the source code.
2. Run the main program by executing the `main()` function.
3. Observe the creation of bank accounts, transactions, and account details displayed in the console.

## Error Handling
- Deposit and withdrawal amounts must be positive numbers.
- Withdrawal amount cannot exceed the current balance.

## Testing
Tested for various scenarios including valid and invalid transactions to ensure functionality and robustness.
