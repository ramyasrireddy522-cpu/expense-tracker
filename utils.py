import json
import os

EXPENSES_FILE = "expenses.json"

def load_expenses():
    """Load expenses from JSON file"""
    if os.path.exists(EXPENSES_FILE):
        try:
            with open(EXPENSES_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def save_expenses(expenses):
    """Save expenses to JSON file"""
    with open(EXPENSES_FILE, 'w') as f:
        json.dump(expenses, f, indent=4)

def display_menu():
    """Display main menu"""
    print("="*40)
    print("📋 EXPENSE TRACKER MENU")
    print("="*40)
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View by Category")
    print("4. View Statistics")
    print("5. Delete Expense")
    print("6. Exit")
    print("="*40)