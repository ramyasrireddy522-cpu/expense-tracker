import json
import os
from datetime import datetime
from utils import load_expenses, save_expenses, display_menu
def add_expense(expenses):
    """Add a new expense"""
    try:
        amount = float(input("Enter amount: $"))
        description = input("Enter description: ")
        category = input("Enter category (Food/Transport/Entertainment/Shopping/Other): ")
        
        expense = {
            "id": len(expenses) + 1,
            "amount": amount,
            "description": description,
            "category": category,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        expenses.append(expense)
        save_expenses(expenses)
        print("\n✓ Expense added successfully!\n")
    except ValueError:
        print("\n✗ Invalid input. Please enter a valid amount.\n")

def view_all_expenses(expenses):
    """Display all expenses"""
    if not expenses:
        print("\n✗ No expenses recorded yet.\n")
        return
    
    print("\n" + "="*70)
    print(f"{'ID':<5} {'Date':<20} {'Category':<15} {'Description':<20} {'Amount':<10}")
    print("="*70)
    
    for expense in expenses:
        print(f"{expense['id']:<5} {expense['date']:<20} {expense['category']:<15} {expense['description']:<20} ${expense['amount']:<10.2f}")
    print("="*70 + "\n")

def view_by_category(expenses):
    """Filter and display expenses by category"""
    if not expenses:
        print("\n✗ No expenses recorded yet.\n")
        return
    
    category = input("Enter category (Food/Transport/Entertainment/Shopping/Other): ")
    filtered = [e for e in expenses if e['category'] == category]
    
    if not filtered:
        print(f"\n✗ No expenses found for category '{category}'.\n")
        return
    
    print(f"\n--- Expenses in '{category}' Category ---\n")
    total = 0
    for expense in filtered:
        print(f"{expense['date']} | {expense['description']:<20} | ${expense['amount']:.2f}")
        total += expense['amount']
    print(f"\nTotal: ${total:.2f}\n")

def view_statistics(expenses):
    """Show spending statistics"""
    if not expenses:
        print("\n✗ No expenses recorded yet.\n")
        return
    
    total = sum(e['amount'] for e in expenses)
    categories = {}
    
    for expense in expenses:
        cat = expense['category']
        categories[cat] = categories.get(cat, 0) + expense['amount']
    
    print("\n" + "="*50)
    print("📊 SPENDING STATISTICS")
    print("="*50)
    print(f"Total Spending: ${total:.2f}")
    print(f"Total Expenses: {len(expenses)}")
    print(f"Average Expense: ${total/len(expenses):.2f}")
    print("\nBreakdown by Category:")
    print("-"*50)
    
    for category, amount in sorted(categories.items(), key=lambda x: x[1], reverse=True):
        percentage = (amount/total)*100
        print(f"{category:<20} ${amount:<10.2f} ({percentage:.1f}%)")
    print("="*50 + "\n")

def delete_expense(expenses):
    """Delete an expense by ID"""
    if not expenses:
        print("\n✗ No expenses to delete.\n")
        return
    
    view_all_expenses(expenses)
    try:
        expense_id = int(input("Enter expense ID to delete: "))
        expenses = [e for e in expenses if e['id'] != expense_id]
        save_expenses(expenses)
        print("\n✓ Expense deleted successfully!\n")
    except ValueError:
        print("\n✗ Invalid ID.\n")

def main():
    """Main application loop"""
    print("\n🎯 Welcome to Expense Tracker!\n")
    
    expenses = load_expenses()
    
    while True:
        display_menu()
        choice = input("Choose an option (1-6): ")
        
        if choice == '1':
            add_expense(expenses)
            expenses = load_expenses()
        elif choice == '2':
            view_all_expenses(expenses)
        elif choice == '3':
            view_by_category(expenses)
        elif choice == '4':
            view_statistics(expenses)
        elif choice == '5':
            delete_expense(expenses)
            expenses = load_expenses()
        elif choice == '6':
            print("\n👋 Thank you for using Expense Tracker. Goodbye!\n")
            break
        else:
            print("\n✗ Invalid option. Please try again.\n")

if __name__ == "__main__":
    main()