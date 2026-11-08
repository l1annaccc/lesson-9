from transactions import (
    add_transaction,
    show_transactions,
    delete_transaction,
)
from statistics import (
    calculate_income ,
    calculate_expenses ,
    calculate_balance,
    filter_by_category
)


def main():
    transactions = []

    while True:
        print("========== FINANCE MANAGER ==========\n ")
        print(" 1. Додати дохід\n")
        print(" 2. Додати витрату\n")
        print(" 3. Переглянути всі транзакції\n")
        print(" 4. Показати загальний дохід\n")
        print(" 5. Показати загальні витрати\n")
        print(" 6. Показати поточний баланс\n")
        print(" 7. Фільтрація за категорією\n")
        print(" 8. Видалити транзакцію\n")
        print(" 0. Вихід\n")
        
        choice = input("\nОберіть дію: ")
        
        match choice :
            case "0":
                print("Використання завершено")
                break
            case "1":
                amount = float(input("Введіть суму доходу: "))
                category = input("Введіть категорію: ") 
                description = input("Введіть опис : ")
                add_transaction(transactions, "income", amount, category, description)
            case "2" :
                amount = float(input("Введіть суму витрати: "))
                category = input("Введіть категорію: ")
                description = input("Введіть опис : ")
                add_transaction(transactions, "expense", amount, category, description)
            case "3":
                show_transactions(transactions)
            case "4":
                income = calculate_income(transactions)
                print(f"Загальний дохід: {income}")
            case "5":
                expense = calculate_expenses(transactions)
                print(f"Загальні витрати: {expense}")
            case "6":
                balance = calculate_balance(transactions)
                print(f"Ваш поточний баланс: {balance}")
            case "7":
                category = input("Введіть категорію для фільтрації: ")
                filtered = filter_by_category(transactions, category)
                show_transactions(filtered)
            case "8":
                transaction_id = int(input("Введіть ID транзакції для видалення: "))
                delete_transaction(transactions, transaction_id)


if __name__ == "__main__" :
    main()

# test stash
