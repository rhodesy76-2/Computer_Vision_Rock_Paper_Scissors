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
Placeholder
### Usage


```python
# placeholder
```