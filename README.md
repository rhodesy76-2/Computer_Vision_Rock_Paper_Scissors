# Computer Vision Rock Paper Scissors

Rock-Paper-Scissors is a game in which each player simultaneously shows one of three hand signals representing rock, paper, or scissors. Rock beats scissors. Scissors beats paper. Paper beats rock. The player who shows the first option that beats the other player's option wins. This is an implementation of an interactive Rock-Paper-Scissors game, in which the user can play with the computer using the camera.

## Milestone 2
The first task consisted of creating a computer vision system, also know as a model, that detects whether the user is showing Rock, Paper or scissors to the camera.

To do this I iused the  to Teachable-Machine website (https://teachablemachine.withgoogle.com) to create a model. 

Each class was trained with images of myslef showing each option to the camera. 

The "Nothing" class represents the lack of option in the image. 

I used roughly 500 images to train the model, thgough bviously teh mopre images you use the ore accurate the model is but also it becomes cumbersome with too many

I found that to make it accurate it was beast to move the appropiate hand configuration starting in each cardner and moving around the sceen corner to corner, going up down, side to side, and then onto diagonally. It also was important that each hand representation and background was constant and that the the computer/ cam,era and mytself were in the same position.

The model is the foundation of the Rock Paper Scissor project, as it will be used to see interpret what we are showing to the camera when playing the game.

### Milestone 3
Setup a new vitual environment  and isntalled the necessary dependencies. Then took the example code and annotated it to understand and explain whatit does. Added a function to translate the what the prediction actually is in relation to the labels. Used argmax to find what the highest value of the prediction numpy array is. Added a line to the while true loop to flip the video fame from the camera so what you see makes sense when playing (mirror image rather than what the camera sees)
### Usage
```python
# Import opencv-python. Opencv is an open source library which is very useful for computer vision applications 
# such as video analysis, CCTV footage analysis and image analysis.
import cv2
# Import load_model from keras.model. From ilpies it has been installed already and l it is installed as part of cv2
from keras.models import load_model
# Import numpy and call it np. 
'''
NumPy is the fundamental package for scientific computing in Python. It is a Python 
library that provides a multidimensional array object, various derived objects (such as masked arrays and matrices), 
and an assortment of routines for fast operations on arrays, including mathematical, logical, shape manipulation, 
sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random 
simulation and much more.
'''
import numpy as np
# From the above imported load_model import we load in our keras_model.h5 model we crerated from Teachable-Machine website
model = load_model('keras_model.h5')
# cv2.VideoCapture(0) returns video from the webcam on my computer and sets it to a variable called cap. The number indicates which
# camera (in case you have more than one)
cap = cv2.VideoCapture(0)
# Creates the vairable data and sets in to an array object represents a multidimensional, homogeneous array of fixed-size items. 
'''
An associated data-type object describes the format of each element in the array (its byte-order, how many bytes it occupies in memory,
whether it is an integer, a floating point number, or something else, etc.)
Arrays should be constructed using array, zeros or empty. 
The parameters given here refer to a low-level method (ndarray(...)) for instantiating an array.
Parameters (for the __new__ method; see Notes below)
    shape : tuple of ints - Shape of created array.
    dtype : data-type, optional - Any object that can be interpreted as a numpy data type.
    np.float32 - means that each value in the numpy array would be a float of size 32 bits
'''
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)



# Added a fucntion to interpret the numpty array output
def interpret_prediction(prediction):
    # used argmax non the numpty array to see what the highest value is
    idetifier_for_label = np.argmax(prediction)
    # Simple if/ elif/ else to convert the the argmax value to what is associated uner the label
    # TODO could refernce the labvel file to get the label?
    if idetifier_for_label == 0:
        print("Rock")
    elif idetifier_for_label == 1:
        print ("Paper")
    elif idetifier_for_label == 2:
        print ("Scissor")
    elif idetifier_for_label == 3:
        print ("Nothing is seen")   
    else:
        print("You shouldnt see this warning")

# This code initiates an infinite loop (to be broken later by a break statement), where we have ret and frame being defined
# as the cap.read(). Basically, ret is a boolean regarding whether or not there was a return at all, at the frame is each 
# frame that is returned. If there is no frame, you wont get an error, you will get None.
while True: 
    ret, frame = cap.read()
    # This resizes an the video camera image (from the cap variable) and saves as resized_fame variable. Sets to 224 by 224, 
    # which is the size of the images from the Teachable-Machine website model
    '''
    The function resize resizes the image src (cap in our case) down to or up to the specified size. Note that the initial dst type or 
    size are not taken into account. Instead, the size and type are derived from the src,dsize,fx, and fy. 
    Uses the Inter_Area method for interpolation
    When the output image is not larger than the input image both in width and height:
        — The input/output scales in both width and height are integers:
             1. If width and height are shrinked by half, and the number of channels is not 2, then INTER_LINEAR_EXACT is INTER_AREA;
             2. If width and height are shrinked by half, then INTER_LINEAR is INTER_AREA;
         INTER_AREA is the boxed/window resampling.
             When the output image is larger than the input image in either width or/and height:
         — The output/input scales in both width and height are integers:
              INTER_AREA is a bilinear interpolation with coefficients (1, 0).
         — Otherwise:
             INTER_AREA is a bilinear interpolation with slightly more complicated coefficient values.
    '''
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    # This creates a numpy array from the resized_fame variabl, saving it as a variable called image_np
    image_np = np.array(resized_frame)
    # Normalizes the image
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    #?????
    data[0] = normalized_image
    # pediction comes from model variable (from keras_model.h5), and making a prediction of what the camera is seeing (as a numpy array)
    prediction = model.predict(data)
    # Added code to flip the frame so a mirror image is displayed inthe python screen output
    flip_frame = cv2.flip(frame,1)
    # The function imshow displays an image in the specified window. Shows the fliped frame  
    cv2.imshow('frame', flip_frame)
    # Prints what the prediction is. A number 0-3, where 0 = Rock, 1 = Paper, 2 =Scissor and 3 = Nothing 
    print(prediction)
    # Prints the numpy array prediction of what the camera is seeing. argmax returns the indices of the maximum values along an axis.
    print(np.argmax(prediction))
    # Calling the interpret_prediction function I added to print out what the prediction avctiually corresponds to (Rock, Paper, Scissor or Nothing)
    interpret_prediction(prediction)
    # Press q to close the window using an if statement to break the True loop 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
        
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
```
### Milestone 4
Created initial steps a manual RPS game. Initially just created two functions, one using the imported randomm function to get a compute choice (computer_choice), and then another function to take a user choice (user_choice) via input whith a simple loop incase an invlaid choice/input given.
Then added a function, get_winner, to determine who won based on the classic rules of Rock-Paper-Scissors and prints the result. The fucntion takes computer_choice, user_choice as arguments.
I then created a simple play function which calls the other three functions I created (get_computer_choice, get_user_choice, and get_winner)
I wrapped up by just calling the play function to run a game.

### Usage
```python
# Importing random module to allow us to pick a random option between rock, paper, and scissors
import random
choice_list = ("Rock", "Paper", "Scissor")

# Function to randomly pick an option between "Rock", "Paper", and "Scissors" and return the choice
def get_computer_choice():
    computer_choice =  random.choice(choice_list)
    print(f"The computer chose {computer_choice}") 
    return computer_choice


# Function to ask the user for an input and return it.
def get_user_choice():
    while True:
        user_choice = input("Please chose one of Rock, Paper or Scissor") 
        if user_choice == "Rock":
            print("You chose Rock")
            return user_choice 
        elif user_choice == "Paper":
            print("You chose Paper") 
            return user_choice 
        elif user_choice == "Scissor":
            print("You chose Scissor")
            return user_choice 
        else:
            print("Please input a valid input; Rock, Paper or Scissor")


#  Function to chose winner
def get_winner(computer_choice, user_choice):
    if user_choice == computer_choice:
       print(f"It's a draw, you both chose {computer_choice}")
    elif user_choice == "Rock":
       if computer_choice == "Scissor":
           print("Rock breaks Scissor, you won!")
       else:
           print("Paper covers Rock, you lost!")
    elif user_choice == "Paper":
       if computer_choice == "Rock":
           print("Paper covers Rock , you won!")
       else:
           print("Scissor cuts Paper, you lost!")
    elif user_choice == "Scissor":
       if computer_choice == "Paper":
           print("Scissor cuts Paper , you won!")
       else:
           print("Rock breaks Scissor, you lost!")
           
# get_winner("Rock", "Scissor")    
def play():    
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    get_winner(computer_choice, user_choice)
    
play()

```

### Milestone 5
Incorporated the computer vision recognition into the RPS game for the playres choice. 

Added lines that display a 'press p to play prompt' and a countdown timer in the python window itself. 

Added a simple play again function. 

Changed the get_winner function so it uses a dictionary rather than just else if statements. Reordered when the computer choice is shown, so it comes after user choice.

Tidied up code and comments.

Finished off by wrapping up the code in a class.

TODO Could add more text prompts in the python window, in fact my initioal vision was everything to run in the python window but demonstrated this in principle. Another rabbit hole but at this stage want to move onto the next project.

Also played around with ChatGPT integration into VSCode, found it actually can critique and suggest code imporovements quite well. 
### Usage
```python


# Import opencv-python. Opencv is an open source library which is very useful for computer vision applications 
# such as video analysis, CCTV footage analysis and image analysis.
import cv2
# Import load_model from keras.model. From ilpies it has been installed already and l it is installed as part of cv2
from keras.models import load_model
# Import numpy and call it np. 
'''
NumPy is the fundamental package for scientific computing in Python. It is a Python 
library that provides a multidimensional array object, various derived objects (such as masked arrays and matrices), 
and an assortment of routines for fast operations on arrays, including mathematical, logical, shape manipulation, 
sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random 
simulation and much more.
'''
import numpy as np
# From the above imported load_model import we load in our keras_model.h5 model we crerated from Teachable-Machine website
import random
import time



# Created a class
class RockPaperScissors():
    def __init__(self):
        self.model = load_model('keras_model.h5')
        self.label_names = ["Rock", "Paper", "Scissor"]
        
#  Function to chose winner
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
                print(f"You won! {user_choice} beats {computer_choice}")
            else:
                print(f"You lost! {computer_choice} beats {user_choice} ")
            return result



    # A fucntion to get and interpret the numpty array output
    def interpret_prediction(self, prediction):
        # used argmax non the numpty array to see what the highest value is
        idetifier_for_label = np.argmax(prediction)
        # Simple if/ elif/ else to convert the the argmax value to what is associated uner the label
        
        while True:
            if idetifier_for_label == 0:
            #print("You chose Rock")
                return "Rock"
            elif idetifier_for_label == 1:
            #print("You chose Paper")
                return "Paper"
            elif idetifier_for_label == 2:
                #print("You chose Scissor")
                return "Scissor"
            elif idetifier_for_label == 3:
                print ("Nothing is seen")   
                return "Nothing is seen"
            else:
                print("You shouldnt see this warning")
        
        

        
    

    # Function to get the prediction from what the camera is seeing    
    def get_prediction(self):
        model = load_model('keras_model.h5')
        # cv2.VideoCapture(0) returns video from the webcam on the computer and sets it to a variable called cap. The number indicates which
        # camera (in case you have more than one)
        cap = cv2.VideoCapture(0)
        # Creates the vairable data and sets in to an array object represents a multidimensional, homogeneous array of fixed-size items. 
        '''
        An associated data-type object describes the format of each element in the array (its byte-order, how many bytes it occupies in memory,
        whether it is an integer, a floating point number, or something else, etc.)
        Arrays should be constructed using array, zeros or empty. 
        The parameters given here refer to a low-level method (ndarray(...)) for instantiating an array.
        Parameters (for the __new__ method; see Notes below)
        shape : tuple of ints - Shape of created array.
        dtype : data-type, optional - Any object that can be interpreted as a numpy data type.
        np.float32 - means that each value in the numpy array would be a float of size 32 bits
        '''
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        # set countdown timer variable, set to 3 seconds
        TIMER = int(3) 
        #print(data)
        # To initiate the 3 second coundown time you must press the p button
        print("Press p to play")
        # This code initiates an infinite loop (to be broken later by a break statement), where we have ret and frame being defined
        # as the cap.read(). Basically, ret is a boolean regarding whether or not there was a return at all, at the frame is each 
        # frame that is returned. If there is no frame, you wont get an error, you will get None.
        while True: 
            ret, frame = cap.read()
            # Added code to flip the frame so a mirror image is displayed inthe python screen output
            flip_frame = cv2.flip(frame,1)
            # Adding text to screen to say press p to play
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(flip_frame, str('Press p to play'), 
                        (200, 250), font,
                        3, (0, 255, 255),
                        4, cv2.LINE_AA)
            # The function imshow displays an image in the specified window. Shows the fliped frame  
            cv2.imshow('Computer Vision: Rock, Paper, Scissor', flip_frame)    
            # check for the key pressed
            k = cv2.waitKey(125)
            # set the key for the countdown
            # to begin. Here we set p
            if k == ord('p'):
                prev = time.time()
                # define what to do whilst Timer is greater or equal to zero
                while TIMER >= 0:
                    ret, frame = cap.read()
                    # Added code to flip the frame so a mirror image is displayed inthe python screen output
                    flip_frame = cv2.flip(frame,1)
                    # Display countdown on each frame
                    # specify the font and draw the
                    # countdown using puttext
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    cv2.putText(flip_frame, str(TIMER), 
                        (200, 250), font,
                        7, (0, 255, 255),
                        4, cv2.LINE_AA)
                    cv2.imshow('Computer Vision: Rock, Paper, Scissor', flip_frame)
                    cv2.waitKey(125)
  
                    # current time
                    cur = time.time()
  
                    # Update and keep track of Countdown
                    # if time elapsed is one second 
                    # then decrease the counter
                    if cur-prev >= 1:
                        prev = cur
                        TIMER = TIMER-1
  
                else:
                    ret, frame = cap.read()
                    # Added code to flip the frame so a mirror image is displayed inthe python screen output
                    flip_frame = cv2.flip(frame,1)
                    cv2.imshow('Computer Vision: Rock, Paper, Scissor', flip_frame)

                    # This next part resizes an the video camera image (from the cap variable) and saves as resized_fame variable. Sets to 224 by 224, 
                    # which is the size of the images from the Teachable-Machine website model
                    '''
                    The function resize resizes the image src (cap in our case) down to or up to the specified size. Note that the initial dst type or 
                    size are not taken into account. Instead, the size and type are derived from the src,dsize,fx, and fy. 
                    Uses the Inter_Area method for interpolation
                    When the output image is not larger than the input image both in width and height:
                    — The input/output scales in both width and height are integers:
                    1. If width and height are shrinked by half, and the number of channels is not 2, then INTER_LINEAR_EXACT is INTER_AREA;
                    2. If width and height are shrinked by half, then INTER_LINEAR is INTER_AREA;
                    INTER_AREA is the boxed/window resampling.
                    When the output image is larger than the input image in either width or/and height:
                        — The output/input scales in both width and height are integers:
                    INTER_AREA is a bilinear interpolation with coefficients (1, 0).
                    — Otherwise:
                    INTER_AREA is a bilinear interpolation with slightly more complicated coefficient values.
                    '''
                    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
                    # This creates a numpy array from the resized_fame variable, saving it as a variable called image_np
                    image_np = np.array(resized_frame)
                    # Normalizes the image
                    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 
                    #?????
                    data[0] = normalized_image
                    # pediction comes from model variable (from keras_model.h5), and making a prediction of what the camera is seeing (as a numpy array)
                    prediction = self.model.predict(data)
                    # Prints what the prediction is. A number 0-3, where 0 = Rock, 1 = Paper, 2 =Scissor and 3 = Nothing 
                    print(prediction)
                    # Prints the numpy array prediction of what the camera is seeing. argmax returns the indices of the maximum values along an axis.
                    print(np.argmax(prediction))
                    # Calling the interpret_prediction function I added to print out what the prediction avctiually corresponds to (Rock, Paper, Scissor or Nothing)
                    # user_choice = interpret_prediction(prediction)
                    user_choice = np.argmax(prediction)
                    # Press q to close the window using an if statement to break the True loop 
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                    # Call get prediction again if nothing is seen, will loop until a valid input is seen
                    else:
                        #user_choice = interpret_prediction(prediction)
                        # print(f"You chose 1 {user_choice}")
                        return user_choice
    
        # After the loop release the cap object
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()




    def play_game(self):
            """Plays a game of rock-paper-scissors using webcam input."""
            computer_choice = random.choice(self.label_names)
            print("Make your choice.")
            user_choice = self.interpret_prediction(self.get_prediction())
            if user_choice == 3:
                print("Unable to detect your choice, please try again.")
                self.get_prediction()
            print("You chose {}.".format(user_choice))
            time.sleep(1)
            print("The computer chose {}.".format(computer_choice))
            time.sleep(1)
            return self.get_winner(computer_choice, user_choice)
    
    # Following function is not called, is just a where I got trying to achieve the following
    # TODO amend the play again so displays play again in puython window and takes input. At moment this seems to not wait
    def play_again2(self):
        print("Play again? (y/n): ")
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        # Added code to flip the frame so a mirror image is displayed inthe python screen output
        flip_frame = cv2.flip(frame,1)
        # The following code displays "Play again y/n" in the pytghon frame
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(flip_frame, str("Play again? (y/n):"), 
                            (200, 250), font,
                            3, (0, 255, 255),
                            4, cv2.LINE_AA)
            # The function imshow displays an image in the specified window. Shows the fliped frame  
        cv2.imshow('Computer Vision: Rock, Paper, Scissor', flip_frame)   
        play_again_input = cv2.waitKey(125)
        time.sleep(1)
        time.sleep(1)
        time.sleep(1)
        if play_again_input == ord('y'):
            print("You chose to play again")
            return True
        else:
            print("You chose not to play again")
            return False
        
    def play_again(self):
        play_again_input = input("Play again? (y/n): ")
        if play_again_input.lower() == "n":
            return False
        elif play_again_input.lower() == "y":
            return True
    
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
                if score['win'] == 3:
                    print("Game Over! You won the match/ 3 games")
                    if not self.play_again():
                        print("Thanks for playing!")
                        break
                    else:
                        score = {'win': 0, 'lost': 0, 'draw': 0}
                        self.main()
                elif score['lost'] == 3:
                    print("Game Over! You lost the match/ 3 games")
                    if not self.play_again():
                        print("Thanks for playing!")
                        break
                    else:
                        score = {'win': 0, 'lost': 0, 'draw': 0}
                        self.main()
        
            
      
if __name__ == "__main__":
    game = RockPaperScissors()
    game.main()
```