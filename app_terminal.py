

import json
import sys

import data
import data_util

from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

expenses = data_util.load_finance()
budget = 3000
amt_spend = 

def main():
    for i in range(1):
        print("===Welcome to Final Finance -- the world's leading app for finance!===")
        print("Please make a selection from the following options below:")
        
        print("1) Add Expense")
        print("2) Print Expense History")
        print("3) Budget")
        print("4) Quit")
        choice = int(input())
        if choice == 1:
            category = input("Cat: ")
            amount = float(input("Amt: "))
            data.add_expense(category, amount, expenses)
        elif choice == 2:
            print("1) Print Total Expenses")
            for i in range(len((expenses))):
                data.print_expense(i, expenses)
        elif choice == 3:
            print("==Budget==")

        elif choice == 4:
            n = int(input("How much do you want to print of the array: "))
            for j in range(n):
                data.print_expense(j-1, expenses)


    ##choice = input("Would you like to print the finances: (Y/N)")


main()