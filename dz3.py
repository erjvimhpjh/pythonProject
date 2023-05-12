import random


class Player:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def play(self, machine, bet):
        result = machine.spin()
        if result == "BAR,BAR,BAR":
            self.balance += 10 * bet
        elif result == "777":
            self.balance += 5 * bet
        elif result == "Cherry,Cherry,Cherry":
            self.balance += 3 * bet
        elif result == "Cherry,Cherry":
            self.balance += 2 * bet
        else:
            self.balance -= bet

        return result


class SlotMachine:
    def __init__(self):
        self.symbols = ["BAR", "777", "Cherry"]

    def spin(self):
        return random.choice(self.symbols) + "," + random.choice(self.symbols) + "," + random.choice(self.symbols)
machine = SlotMachine()
player1 = Player("Alice", 100)
player2 = Player("Bob", 50)

for i in range(5):
    print("Round", i+1)
    print("Player 1's balance:", player1.balance)
    print("Player 2's balance:", player2.balance)
    player1.play(machine, 5)
    player2.play(machine, 3)

print("Final balances:")
print("Player 1's balance:", player1.balance)
print("Player 2's balance:", player2.balance)
