import random

# Define the symbols and their corresponding payouts
symbols = ['🍒', '🍉', '🥭', '🔔', '✨']
payouts = {
    '🍒': 15,
    '🍉': 30,
    '🥭': 25,
    '🔔': 50,
    '✨': 10,
}

def spin_row():
    """Simulate spinning the slot machine and returning a row of symbols."""
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    """Print the row of symbols."""
    print(" | ".join(row))

def get_payout(row):
    """Calculate the payout based on the row of symbols."""
    # Check if all symbols are the same
    if len(set(row)) == 1:
        return payouts[row[0]]
    return 0

def main():
    balance = 1000

    print("**************************")
    print("Welcome to Python Slots")
    print("Symbols: 🍒 🍉 🥭 🔔 ✨")
    print("**************************")

    while balance > 0:
        print(f"Current balance: ${balance}")
        bet = input("Please enter your bet amount: ")

        if not bet.isdigit() or int(bet) <= 0 or int(bet) > balance:
            print("Please enter a valid bet amount.")
            continue
        
        bet = int(bet)
        balance -= bet

        # Spin the slot machine
        row = spin_row()
        print_row(row)

        # Get the payout
        payout_multiplier = get_payout(row)
        if payout_multiplier > 0:
            payout = payout_multiplier * bet  # Multiply the payout by the bet
            balance += payout
            print(f"You won: ${payout}!")
        else:
            print("No win this time.")

    print("Game over! You ran out of balance.")

if __name__ == '__main__':
    main()
