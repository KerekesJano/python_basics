class Game:
    def __init__(self, message):
        # Players score
        self.score1 = 0
        self.score2 = 0
        # Round count
        self.round = 0
        # Print out welcome message
        print(f"{message}")

    def score(self, player):
        match player:
            case "player1":
                self.ruond += 1
                self.score1 = self.score1 + 1
                print(self.score1)
            case "player2":
                self.ruond += 1
                self.score2 = self.score2 + 1
                print(self.score2)
            case _:
                print("Invalid player")

    def is_game_over(self) -> bool:
        if self.round == 2 and abs(self.score1 - self.score2):
            return True
        elif self.round >= 3:
            return True
        else:
            return False


welcome_message = "Hello, let's play!"
game = Game(welcome_message)

game.score1 = 100
game.score("player1")

# Init


def init():
    pass
