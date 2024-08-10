def main():
    # Create bank account objects
    account1 = BankAccount("123456789", "Alice Johnson", 1000.00)
    account2 = BankAccount("987654321", "Bob Smith", 500.00)

    # Display initial account information
    print("Initial Account Information:")
    account1.displayAccountInfo()
    account2.displayAccountInfo()

    # Perform transactions
    print("\nPerforming transactions:")
    account1.deposit(200)
    account1.withdraw(150)
    account2.deposit(100)
    account2.withdraw(600)

    # Display updated account information
    print("\nUpdated Account Information:")
    account1.displayAccountInfo()
    account2.displayAccountInfo()

if __name__ == "__main__":
    main()
