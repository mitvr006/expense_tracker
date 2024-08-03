# Expense Tracker program
expense_data = {}

while True:
    expense_choose = int(input("\nKharch tracker\n1. Kharch add\n2. Kharch view\n3. Kharch delete\n4. Create new report\n5. Exit\nEnter your choice: "))
    
    if expense_choose == 1:
        while True:
            date = str(input("Enter the kharch date (dd/mm/yy): "))
            rashi = float(input("Enter the kharch rashi: "))
            category = str(input("Enter the category you kharch the rashi (e.g., Khana, Safar, Avashyakta, etc.): "))
            if date in expense_data:
                expense_data[date].append((rashi, category))
            else:
                expense_data[date] = [(rashi, category)]
            print(f"Kharch added: {date} - ₹{rashi:.2f} ({category})")
            break

    elif expense_choose == 2:
        date = str(input("Enter the kharch date to view (dd/mm/yy): "))
        if date in expense_data:
            print(f"Expenses for {date}:")
            for i, (rashi, category) in enumerate(expense_data[date], start=1):
                print(f"{i}. ₹{rashi:.2f} ({category})")
        else:
            print("Kharch not found")
            
    elif expense_choose == 3:
        date = str(input("Enter the kharch date to delete (dd/mm/yy): "))
        if date in expense_data:
            del expense_data[date]
            print(f"Kharch on {date} deleted.")
        else:
            print("Kharch not found")
            
    elif expense_choose == 4:
        category_expenses = {}
        for date, expenses in expense_data.items():
            for rashi, category in expenses:
                if category in category_expenses:
                    category_expenses[category] += rashi
                else:
                    category_expenses[category] = rashi
        
        print("\nKharch Report:")
        for category, total in category_expenses.items():
            print(f"{category}: ₹{total:.2f}")
        
        total_expense = sum(rashi for expenses in expense_data.values() for rashi, category in expenses)
        print(f"Total Kharch: ₹{total_expense:.2f}")
        
    elif expense_choose == 5:
        break

    else:
        print("Invalid choice, please try again.")
