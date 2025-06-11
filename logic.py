# savers_logic.py

def deposit(money, amount):
    """Add amount to savings and return updated total."""
    return money + amount

def deduct(money, amount):
    """Deduct amount from savings and return updated total."""
    if amount > money:
        raise ValueError("You can't deduct more than what you have!")
    return money - amount



