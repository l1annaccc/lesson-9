def add_transaction(transactions, transaction_type, amount, category, description):
    if transaction_type not in ["income" or "expence"] :
        print("Your transaction should be either income or expence")
        return



