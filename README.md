# TicTacToe-With-AI
The program is implementation of famous TicTacToe board game in console.

Having multiple difficulties, the hardest mode uses minimax recursive algorithm.


## Launching the game
To launch the program type `python run.py` in project's root direcotry.

The program will prompt you for command.
  the main commands are: `start` and `exit`
  1. if `exit` is specified the program terminates
  2. if `start` is specified you will need two additional arguments for X player and O player, 
  available arguments are `user, esay, medium, hard`
  
  For instance, if you'd like to play as X against hardest difficulty, you input:
  
  `start user hard`
  
  If you'd like to play as users only:
  
   `start user user`
   
   and so on...
  
  

## Description
The game has three difficulties
<ul>
  <li> Easy - the machine chooses random available cell from the board </li>
  <li> Medium - if there are rows, columns or diagonals that are one symbol away from game being finished, medium will try to win or not to loose, in that order </li>
  <li> Hard - machine uses minimax algorithm </li>
</ul>

## dependencies and installation
The project uses python built-in modules only.
