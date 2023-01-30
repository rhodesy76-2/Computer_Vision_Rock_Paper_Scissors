#%%

import cv2
import numpy as np
from keras.models import load_model
import random
import time

class RockPaperScissors():
    def __init__(self):
        self.model = load_model('keras_model.h5')
        self.label_names = ["Rock", "Paper", "Scissor"]

    def get_winner(self, computer_choice, user_choice):
        """Determines the winner of the game based on the user's and computer's choices.

        Returns 1 if the user wins, 2 if the user loses, and 0 if it's a draw.
        """
        results = {
            ("Rock", "Scissor"): 1,
            ("Rock", "Paper"): 2,
            ("Paper", "Rock"): 1,
            ("Paper", "Scissor"): 2,
            ("Scissor", "Paper"): 1,
            ("Scissor", "Rock"): 2,
        }
        if user_choice == computer_choice:
            print("It's a draw, you both chose {}".format(computer_choice))
            return 0
        else:
            result = results.get((user_choice, computer_choice))
            if result == 1:
                print("You won!")
            else:
                print("You lost!")
            return result

    def interpret_prediction(self, prediction):
        """Interprets the prediction from the model and returns the label name.

        Returns None if the prediction is invalid.
        """
        label_id = np.argmax(prediction)
        if 0 <= label_id < len(self.label_names):
            return self.label_names[label_id]
        else:
            return None

    def get_prediction(self):
        """Captures webcam input and returns the prediction from the model."""
        with cv2.VideoCapture(0) as cap:
            while True:
                # Capture webcam input
                ret, frame = cap.read()
                if not ret:
                    print("Error capturing webcam input.")
                    return None
                # Pre-process the frame
                data = np.expand_dims(frame, axis=0)
                # Get the prediction from the model
                prediction = self.model.predict(data)
                return prediction

    def play_game(self):
        """Plays a game of rock-paper-scissors using webcam input."""
        computer_choice = random.choice(self.label_names)
        print("Make your choice.")
        user_choice = self.interpret_prediction(self.get_prediction())
        if user_choice is None:
            print("Unable to detect your choice, please try again.")
            return
        print("You chose {}.".format(user_choice))
        time.sleep(1)
        print("The computer chose {}.".format(computer_choice))
        time.sleep(1)
        return self.get_winner(computer_choice, user_choice)

    def play_again(self):
        """ask the user if they want to play again"""
        choice = input("Do you want to play again? Y/N ")
        if choice.upper() == "Y":
            return True
        else:
            return False

    def main(self):
        """Main function to run the game."""
        score = {'win': 0, 'lost': 0, 'draw': 0}
        while True:
            result = self.play_game()
            if result == 1:
                score['win'] += 1
                # TODO if win = 3, game over, you won, play again?
            elif result == 2:
                score['lost'] += 1
                # TODO break if loss = 3, game over, you lost, play again?
            else:
                score['draw'] += 1
            print("Wins: {} | Losses: {} | Draws: {}".format(score['win'], score['lost'], score['draw']))
            if not self.play_again():
                print("Thanks for playing!")
                break

if __name__ == "__main__":
    game = RockPaperScissors()
    game.main()

# %%
