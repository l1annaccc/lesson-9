def calculate_income(transactions):
    return sum(i["amount"] for i in transactions if i["type"] == "income")


def calculate_expenses(transactions):
    return sum(i["amount"] for i in transactions if i["type"] == "expense")



