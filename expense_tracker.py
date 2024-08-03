# Expense Tracker Application

class Kharch:
    def __init__(self, date, rashi, category):
        self.date = date      # Description of the expense
        self.rashi = rashi    # Amount of the expense
        self.category = category  # Category of the expense
       

class ExpenseTracker:
    def __init__(self):
        self.kharch = []  # List to store expenses

    def kharch_add(self, date, rashi, category):
        naya_kharch = Kharch(date, rashi,category)
        self.kharch.append(naya_kharch)
        print(f"Kharch add: {date} - ₹{rashi:.2f} ({category})")

    def kharch_view(self):
        if not self.kharch:
            print("not kharch")
            return
        print("\nKharch:")
        for idx, kharch in enumerate(self.kharch, start=1):
            print(f"{idx}. {kharch.date} - ₹{kharch.rashi:.2f} ({kharch.category})")

    def kharch_delete(self, index):
        if 0 <= index < len(self.kharch):
            delete_kharch = self.kharch.pop(index)
            print(f"delete kharch: {delete_kharch.date} - ₹{delete_kharch.rashi:.2f} ({delete_kharch.category})")
        else:
            print("rong index.")

    def report_gen(self):
        if not self.kharch:
            print("not kharch")
            return
        
        category_total = {}
        for kharch in self.kharch:
            if kharch.category in category_total:
                category_total[kharch.category] += kharch.rashi
            else:
                category_total[kharch.category] = kharch.rashi
        
        print("\nKharch Report:")
        for category, total in category_total.items():
            print(f"{category}: ₹{total:.2f}")
        
        total_expense = sum(kharch.rashi for kharch in self.kharch)
        print(f"Total Kharch: ₹{total_expense:.2f}")

def main():
    tracker = ExpenseTracker()

    while True:
        print("\nKharch Tracker")
        print("1. Kharch add")
        print("2. Kharch view")
        print("3. Kharch delete")
        print("4. create new report")
        print("5. exit")

        choose = input("Enter your choice: ")

        if choose == '1':
            date= input("enter the date(dd/mm/yy): ")
            rashi = float(input("enter the rashi you spend: "))
            category = input("enter the category you spend the money (e.g., Khana, Safar, Avashyakta, etc.): ")
            tracker.kharch_add(date, rashi,category)
        elif choose == '2':
            # search_category = input("enter the category from which you want to see the expenses: ")
            # kharch_view(search_category)
            tracker.kharch_view()
        elif choose == '3':
            tracker.kharch_view()
            index = int(input("enter the index and delete: ")) - 1
            tracker.kharch_delete(index)
        elif choose == '4':
            tracker.report_gen()
        elif choose == '5':
            print("exit")
            break
        else:
            print("rong choice")

if __name__ == "__main__":
    main()
