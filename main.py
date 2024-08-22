class ExpenseTracker:
    def __init__(self):
        self.expenses = {}
        
    def create_category(self, category):
        if category not in self.expenses:
            self.expenses[category] = []
        else:
            print(f"Category {category} already exist.")

    def add_expense(self, category, amount, description):
        if category in self.expenses:
            self.expenses[category].append({'amount':amount, 'description':description})
        else:
            print("Category does not exist.")

    def remove_category(self, remove_category):
        if remove_category in self.expenses:
            result = self.expenses.pop(remove_category)
            print(f"{remove_category} has been removed.")
        else:
            print("Category does not exist.")
        return result

    def remove_expense(self, from_category, description):
        for expense in self.expenses[from_category]:
            if expense['description'] == description:
                result = self.expenses[from_category].remove(expense)
                print(f"{description} has been removed from {from_category}.")
        return result

    def create_report(self):
        print("\nTotal Expenses of Each Category:")
        report = []
        for category, expenses in self.expenses.items():
            total = sum(expense['amount'] for expense in expenses)
            report.append(f"{category}: ${total}")
        return "\n".join(report)

    def get_category(self, requested_category):
        if requested_category in self.expenses:
            print(f"{requested_category}:")
            result = []
            for expense in self.expenses[requested_category]:
                description = expense['description']
                amount = expense['amount']
                result.append(f"{description}: ${amount}")
            return "\n".join(result)
        else:
            print("Category does not exist")

    def save(self,filename):
        with open(filename, 'w') as file:
            for category, expenses in self.expenses.items():
                file.write(f"{category}\n")
                for expense in expenses:
                    file.write(f"{expense['amount']}, {expense['description']}\n")
        print(f"Your expenses as been saved in '{filename}'")

    def load(self, filename):
        with open(filename, 'r') as f:
            current_category = None
            for line in f:
                line = line.strip()
                if ',' not in line:
                    current_category = line
                    self.expenses[current_category] = []
                else:
                    amount, description = line.split(',',1)
                    self.expenses[current_category].append({'amount': int(amount),'description': description })

tracker = ExpenseTracker()

tracker.create_category("Clothes")
tracker.add_expense("Clothes", 10, "White shirt")
tracker.add_expense("Clothes", 10, "Purple shirt")

tracker.remove_category("Clothes")

tracker.create_category("Housing")
tracker.add_expense("Housing", 100, "Electric")
tracker.add_expense("Housing", 90, "Gas")

tracker.remove_expense("Housing", "Gas")

print(tracker.get_category("Housing"))

print(tracker.create_report())


tracker.save('text.txt')
tracker.load('text.txt')
print(tracker.create_report())



        

