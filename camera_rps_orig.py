 # %%


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


#  Function to chose winner
def get_winner(computer_choice, user_choice):
    if user_choice == computer_choice:
       print(f"It's a draw, you both chose {computer_choice}")
    elif user_choice == "Rock":
       if computer_choice == "Scissor":
           print("Rock breaks Scissor, you won!")
           return 1
       else:
           print("Paper covers Rock, you lost!")
           return 2
    elif user_choice == "Paper":
       if computer_choice == "Rock":
           print("Paper covers Rock , you won!")
           return 1
       else:
           print("Scissor cuts Paper, you lost!")
           return 2
    elif user_choice == "Scissor":
       if computer_choice == "Paper":
           print("Scissor cuts Paper , you won!")
           return 1
       else:
           print("Rock breaks Scissor, you lost!")
           return 2



# A fucntion to get and interpret the numpty array output
def interpret_prediction(prediction):
    # used argmax non the numpty array to see what the highest value is
    idetifier_for_label = np.argmax(prediction)
    # Simple if/ elif/ else to convert the the argmax value to what is associated uner the label
    # TODO could refernce the labe.txt file to get the label? Dictionary?
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
        
        
       # else:    
            # get_prediction() # *** remove and make an else statement in get prediction that if ++3 nothing seen to run again
        
    

# Function to get the prediction from what the camera is seeing    
def get_prediction():
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
    TIMER = int(1) 
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
                prediction = model.predict(data)
                # Prints what the prediction is. A number 0-3, where 0 = Rock, 1 = Paper, 2 =Scissor and 3 = Nothing 
                print(prediction)
                # Prints the numpy array prediction of what the camera is seeing. argmax returns the indices of the maximum values along an axis.
                print(np.argmax(prediction))
                # Calling the interpret_prediction function I added to print out what the prediction avctiually corresponds to (Rock, Paper, Scissor or Nothing)
                # user_choice = interpret_prediction(prediction)
                user_choice = interpret_prediction(prediction)
                # Press q to close the window using an if statement to break the True loop 
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                # Call get prediction again if nothing is seen, will loop until a valid input is seen
                elif user_choice == "Nothing is seen":
                    print("Nothing seen try again")
                    get_prediction()
                else:
                    user_choice = interpret_prediction(prediction)
                    print(f"You chose {user_choice}")
                    return user_choice
    
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()




# Function to ask the user for an input and return it. Calls the get prediction function to take a camera input.
def get_user_choice():
    user_choice = get_prediction() 
    return user_choice
# TODO remove? or get working as not feeding in line 248   


# Function to randomly pick an option between "Rock", "Paper", and "Scissors" and return the choice
def get_computer_choice():
    choice_list = ("Rock", "Paper", "Scissor")
    computer_choice =  random.choice(choice_list)
    print(f"The computer chose {computer_choice}") 
    return computer_choice           

def play_again():
    play_again_input = input("Play again? (y/n): ")
    if play_again_input.lower() == "n":
            exit()
    elif play_again_input.lower() == "y":
        play()
      
def play():
    computer_wins = 0
    user_wins = 0
    while computer_wins or user_wins <= 2:
        computer_choice = get_computer_choice()
        user_choice = get_prediction() #get_user_choice()  
        winner = get_winner(computer_choice, user_choice)
        if (winner == 1):
            user_wins += 1
            print('User wins the round!!!')
            print(f"The computer score is: {computer_wins} and the player score is: {user_wins}")
            if  computer_wins == 3:
                print('The computer won this match!')
                computer_wins = 0
                user_wins = 0
                play_again()
            elif user_wins == 3:
                print('You win the match!')
                computer_wins = 0
                user_wins = 0
                play_again()
        elif (winner == 2):
            computer_wins += 1
            print('Computer wins the round!!!')
            print(f"The computer score is: {computer_wins} and the player score is: {user_wins}") 
            if  computer_wins == 3:
                print('The computer won this match!')
                computer_wins = 0
                user_wins = 0
                play_again()
            elif user_wins == 3:
                print('You win the match!')
                computer_wins = 0
                user_wins = 0
                play_again()
   
    
play()
# %%