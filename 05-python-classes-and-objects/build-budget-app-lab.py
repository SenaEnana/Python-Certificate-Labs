class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        """Appends a deposit object to the ledger."""
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        """Withdraws an amount if funds are available and records it as negative."""
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        """Returns the current balance based on the ledger."""
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category_instance):
        """Transfers an amount to another category if funds are available."""
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category_instance.name}")
            category_instance.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        """Returns False if amount exceeds balance, True otherwise."""
        return amount <= self.get_balance()

    def __str__(self):
        """Formats the ledger print output strictly to 30 characters wide."""
        # Title line: 30 characters total, centered with *
        title = f"{self.name:*^30}\n"
        
        items = ""
        for item in self.ledger:
            # Truncate description to 23 chars, left-aligned
            desc = f"{item['description'][:23]:<23}"
            # Format amount to 2 decimal places, right-aligned to 7 chars
            amt = f"{item['amount']:>7.2f}"
            items += f"{desc}{amt}\n"
            
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    """Generates a bar chart string representing percentages spent by category."""
    chart = "Percentage spent by category\n"
    
    # Calculate total withdrawals per category and overall total spent
    calc_withdrawals = []
    for cat in categories:
        spent = sum(-item["amount"] for item in cat.ledger if item["amount"] < 0)
        calc_withdrawals.append(spent)
        
    total_spent = sum(calc_withdrawals)
    
    # Calculate percentages rounded down to the nearest 10
    # Guard against division by zero if nothing was spent anywhere
    percentages = []
    for spent in calc_withdrawals:
        if total_spent > 0:
            pct = int((spent / total_spent) * 100 // 10) * 10
        else:
            pct = 0
        percentages.append(pct)

    # Build the bar chart rows (100 down to 0)
    for i in range(100, -1, -10):
        chart += f"{i:>3}| "
        for pct in percentages:
            if pct >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    # Build the horizontal line separator
    # 2 spaces padding before '|', 1 space after '|', plus 3 dashes per category
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Build the vertical category names
    max_len = max(len(cat.name) for cat in categories)
    for i in range(max_len):
        chart += "     "
        for cat in categories:
            if i < len(cat.name):
                chart += f"{cat.name[i]}  "
            else:
                chart += "   "
        if i < max_len - 1:
            chart += "\n"

    return chart