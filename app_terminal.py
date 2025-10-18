

import json
import sys

import data_functions
import data_util

from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

data = data_util.load_finance()
expenses = data["expenses"]
budget = data["budget"]
amt_spend = 0



def main():
    while True:
        print("===Welcome to Final Finance -- the world's leading app for finance!===")
        print("Please make a selection from the following options below:")
        
        print("1) Add Expense")
        print("2) Print Expense History")
        print("3) Budget")
        print("4) Quit")
        try:
            choice = int(input())
        except ValueError:
            print("Please enter a choice from 1-4.")
            continue

        if choice == 1:
            category = input("Cat: ")
            amount = float(input("Amt: "))
            data_functions.add_expense(category, amount, expenses)
            data_util.write_finance(data)

        elif choice == 2:
            print("1) Print Total Expenses")
            for i in range(len((expenses))):
                data_functions.print_expense(i, expenses)

        elif choice == 3:
            print("==Budget==")
            data_functions.check_budget(0, budget, expenses)
            print("$" + str(budget))

        elif choice == 4:
            break
                


    ##choice = input("Would you like to print the finances: (Y/N)")


main()