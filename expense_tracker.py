import matplotlib.pyplot as plt
import json
import logging

logging.basicConfig(level=logging.INFO)

try:
    with open("kharach.json", "r") as file:
        kharch_list = json.load(file)

except FileNotFoundError:
    kharch_list = []

while True:
    print("""
    Welcome to my spend expense tracker
    1. Add Expense
    2. View Expenses
    3. Delete Expense
    4. Total Expense Report
    5. Category-wise Report (Pie Chart)
    6. Daily Report (Bar Graph)
    7. Exit
    """)
    try:
        user_choice = int(input("Enter your choice: "))

    except ValueError:
        print("Invalid input! Please enter a number between 1 and 7.")
        continue

    if user_choice == 1:
        date = input("Enter the date (dd/mm/yy): ")
        try:
            rashi = float(input("Enter the amount of rashi: "))
        except ValueError:
            print("Invalid amount! Please enter a valid number.")
            continue
        category = input("Enter the category: ")
        kharch_list.append({"date": date, "rashi": rashi, "category": category})
        
        with open("kharach.json", "w") as file:
            json.dump(kharch_list, file)
        print("Expense added successfully!")

    elif user_choice == 2:
        if not kharch_list:
            print("No expense data available.")
        else:
            print("\nExpenses:")
            for expense in kharch_list:
                print(f"{expense['date']} - ₹{expense['rashi']} ({expense['category']})")

    elif user_choice == 3:
        if not kharch_list:
            print("No expenses to delete.")
        else:
            date_to_delete = input("Enter the date of the expense to delete (dd/mm/yy): ")
            deleted = False
            for i, expense in enumerate(kharch_list):
                if expense["date"] == date_to_delete:
                    del kharch_list[i]
                    with open("kharach.json", "w") as file:
                        json.dump(kharch_list, file)
                    print(f"Expense on {date_to_delete} deleted successfully!")
                    deleted = True
                    break
            if not deleted:
                print(f"No expense found on {date_to_delete}.")

    elif user_choice == 4:
        if not kharch_list:
            print("No expenses to report.")
        else:
            total_spent = sum(expense["rashi"] for expense in kharch_list)
            print(f"Total amount spent: ₹{total_spent:.2f}")

    elif user_choice == 5:
        if not kharch_list:
            print("No expenses to show in the report.")
        else:
            categories = {}
            for expense in kharch_list:
                category = expense["category"]
                categories[category] = categories.get(category, 0) + expense["rashi"]

            labels = list(categories.keys())
            sizes = list(categories.values())

            plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
            plt.title('Expense Distribution by Category')
            plt.show()

    elif user_choice == 6:
        if not kharch_list:
            print("No expenses to show in the report.")
        else:
            dates = {}
            for expense in kharch_list:
                date = expense["date"]
                dates[date] = dates.get(date, 0) + expense["rashi"]

            labels = list(dates.keys())
            values = list(dates.values())

            plt.bar(labels, values, color='skyblue')
            plt.xlabel('Dates')
            plt.ylabel('Amount (₹)')
            plt.title('Daily Expense Tracker')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()

    elif user_choice == 7:
        print("Thank you for using the expense tracker. Goodbye!")
        break

    else:
        print("Invalid choice! Please select a valid option.")

