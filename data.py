import data_util

def print_expense(n, expenses):
   e = expenses[n]
   print(f"{e['category']:<10} | ${e['amount']:>7.2f}")

def add_expense(cat, amt, expenses):
    expenses.append({"category": cat, "amount": amt})
    data_util.write_finance(expenses)