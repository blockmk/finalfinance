import data_util

def check_budget(n, budget, expenses):
   b = budget
   e = expenses[n]
   total = 0
   for expense in expenses:
        total += expense["amount"]
   print("Expenses total:" + str(total))
   if total > budget:
       print("You have exceeded your budget by " + str((((total - budget)/budget)*100)) + "%")
       return 0


def add_expense(cat, amt, expenses):
    expenses.append({"category": cat, "amount": amt})
     
def remove_expense(n, expenses):
    del expenses[n]

def print_expense(n, expenses):
   e = expenses[n]
   print(f"{e['category']:<10} | ${e['amount']:>7.2f}")

