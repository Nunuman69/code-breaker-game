import random

class CodeBreakerGame:
    def __init__(self, code_length=4, digit_min=1, digit_max=8, max_attempts=10):
        self.code_length = code_length
        self.digit_min = digit_min
        self.digit_max = digit_max
        self.max_attempts = max_attempts
        self.secret_code = self.generate_secret_code()
        self.history = {}

    def generate_secret_code(self):
        return ''.join(str(random.randint(self.digit_min, self.digit_max)) for _ in range(self.code_length))

    def get_player_guess(self):
        while True:
            guess = input(f"Enter your {self.code_length}-digit guess (digits between {self.digit_min} and {self.digit_max}): ")
            if len(guess) != self.code_length or not guess.isdigit():
                print(f"Error: Please enter exactly {self.code_length} digits.")
                continue
            if any(int(d) < self.digit_min or int(d) > self.digit_max for d in guess):
                print(f"Error: All digits must be between {self.digit_min} and {self.digit_max}.")
                continue
            return guess

    def generate_feedback(self, guess):
        feedback = []
        secret_temp = list(self.secret_code)
        guess_temp = list(guess)

        # Step 1: Check for exact matches (X)
        for i in range(self.code_length):
            if guess_temp[i] == secret_temp[i]:
                feedback.append("X")
                secret_temp[i] = None
                guess_temp[i] = None

        # Step 2: Check for partial matches (O)
        for i in range(self.code_length):
            if guess_temp[i] is not None and guess_temp[i] in secret_temp:
                feedback.append("O")
                secret_temp[secret_temp.index(guess_temp[i])] = None

        return ''.join(feedback)

    def play(self):
        print("-- Welcome to Code Breaker --")
        print(f"I have generated a secret {self.code_length}-digit code. Each digit is between {self.digit_min} and {self.digit_max}. You have {self.max_attempts} attempts to guess it.")
        print("Feedback: 'X' for correct digit in the correct position, 'O' for correct digit in the wrong position.\n")

        for attempt in range(1, self.max_attempts + 1):
            print(f"Attempt {attempt}/{self.max_attempts}")
            guess = self.get_player_guess()
            feedback = self.generate_feedback(guess)
            self.history[attempt] = (guess, feedback)
            print(f"Feedback for {guess}: {feedback}\n")

            if feedback == "X" * self.code_length:
                print(f"Congratulations! You guessed the code correctly in {attempt} attempts!")
                return

        print(f"Game Over! You’ve used all {self.max_attempts} attempts.")
        print(f"The secret code was: {self.secret_code}")

# Start the game:
if __name__ == "__main__":
    game = CodeBreakerGame()
    game.play()
