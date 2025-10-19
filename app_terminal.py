

import json
import sys

import time 

import data_functions
import data_util

from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

data = data_util.load_finance()
expenses = data["expenses"]
budget = data["budget"]


def main():
    global budget
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
            time.sleep(2)
            

        elif choice == 3:
            print("===Budget===")
            print("1) Set a Budget")
            print("2) Check Budget")
            choice_b1 = int(input())
            

            if choice_b1 == 1:
                choice_b2 = int(input("Choose budget: "))
                new_budget = choice_b2
                budget = new_budget

            elif choice_b1 == 2:
                x = data_functions.check_budget(0, budget, expenses)
                print(x)
                if x == 0:
                    choice = input("Would you like to remove an expense?")
                    if choice == "Y":
                        data_functions.remove_expense(0, expenses)
                        data_util.write_finance(data)


            

        elif choice == 4:
            break
                


    ##choice = input("Would you like to print the finances: (Y/N)")


main()