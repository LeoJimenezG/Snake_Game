from turtle import Turtle


class Score(Turtle):
    # Initializer
    def __init__(self):
        super().__init__()
        self.score = 0
        # Open the data file on read mode
        with open(file="data.txt", mode="r") as file:
            # Save the content and convert it to int
            self.highest_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(x=0, y=360)
        self.hideturtle()
        self.refresh_score()

    # Method to clear the previous draw and write the score
    def refresh_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}   Highest Score: {self.highest_score}", align="center", font=("arial", 20, "bold"))

    # Method to add one point to the score
    def add_score(self):
        self.score += 1
        self.refresh_score()

    # Method to show the game over message
    def game_over(self):
        # Check if the current score is higher than the highest score
        if self.score > self.highest_score:
            self.highest_score = self.score
            # Open the file on write mode
            with open(file="data.txt", mode="w") as file:
                # Convert the score to string and write it
                file.write(str(self.score))

        # Reset the score
        self.score = 0
        self.refresh_score()
