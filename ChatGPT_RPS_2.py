import cv2
import numpy as np
from keras.models import load_model
import random
import logging
from Label import Label
import time

class RockPaperScissors():
    def __init__(self):
        self.model = self.load_model()
        self.score = {'win': 0, 'lost': 0, 'draw': 0}
        self.cap = self.check_webcam()
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.ERROR)

    def load_model(self):
        try:
            model = load_model('keras_model.h5')
            self.logger.info("Model loaded successfully")
            return model
        except Exception as e:
            self.logger.error(f"An error occurred while loading the model. {e}")
            return None

    def check_webcam(self):
        try:
            cap = cv2.VideoCapture(0)
            if not cap.isOpened():
                raise Exception("Webcam is not available")
            else:
                self.logger.info("Webcam is available")
                return cap
        except Exception as e:
            self.logger.error(f"An error occurred while accessing the webcam. {e}")
            return None

    def get_winner(self, computer_choice, user_choice):
        """Determines the winner of the game based on the user's and computer's choices.

        Returns 1 if the user wins, 2 if the user loses, and 0 if it's a draw.
        """
        results = {
            (Label.Rock, Label.Scissor): 1,
            (Label.Rock, Label.Paper): 2,
            (Label.Paper, Label.Rock): 1,
            (Label.Paper, Label.Scissor): 2,
            (Label.Scissor, Label.Paper): 1,
            (Label.Scissor, Label.Rock): 2,
        }
        if user_choice == computer_choice:
            print("It's a draw, you both chose {}".format(computer_choice.name))
            return 0
        else:
            result = results.get((user_choice, computer_choice))
            if result == 1:
                print("You won!")
                self.score['win'] += 1
            else:
                print("You lost!")
                self.score['lost'] += 1
            return result

    def interpret_prediction(self, prediction):
        """Interprets the prediction from the model and returns the label name.

        Returns None if the prediction is invalid.
        """
        label_id = np.argmax(prediction)
        if 0 <= label_id < len(Label):
            return Label(label_id)
        else:
            return None

    def get_prediction(self):
        """Captures webcam input and returns the prediction from the model."""
        try:
            ret, frame = self.cap.read()
            if not ret:
                self.logger.error("Error capturing webcam input.")
                return None
            data = np.expand_dims(frame, axis=0)
            prediction = self.model.predict(data)
            return prediction
        except Exception as e:
            self.logger.error(f"An error occurred while getting the prediction. {e}")
            return None

    def play_game(self):
        """Plays a game of rock-paper-scissors using webcam input."""
        computer_choice = random.choice(list(Label))
        print("Make your choice.")
        user_choice = self.interpret_prediction(self.get_prediction())
        if user_choice is None:
            print("Unable to detect your choice, please try again.")
            return
        print("You chose {}.".format(user_choice.name))
        time.sleep(1)
        print("The computer chose {}.".format(computer_choice.name))
        time.sleep(1)
        result = self.get_winner(computer_choice, user_choice)
        if result == 0:
            self.score['draw'] += 1
        return result

    def play_again(self):
        """Prompts the user if they want to play again and returns True or False."""
        while True:
            choice = input("Do you want to play again? Y/N ")
            if choice.upper() == "Y":
                return True
            elif choice.upper() == "N":
                return False
            else:
                print("Invalid input. Please enter Y or N.")

    def display_result(self):
        """Displays the final result of the game."""
        print("Wins: {} | Losses: {} | Draws: {}".format(self.score['win'], self.score['lost'], self.score['draw']))

    def main(self):
        """Main function to run the game."""
        if self.model is None or self.cap is None:
            return
        while True:
            self.play_game()
            if not self.play_again():
                print("Thanks for playing!")
                break
            
if __name__ == "__main__":
    game = RockPaperScissors()
    game.main()