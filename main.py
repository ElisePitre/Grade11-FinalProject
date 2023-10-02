# Author: Elise Pitre
# The user can choose a mini game to play.

# Imports.
import time
import random
# Controls the random numbers for tests.
random.seed(1)

# The user chooses which game they want to play from a list.
print("Please enter the corresponding number to the game you want to play.")
print("1. Mastermind")
print("2. Snake Game")
print("3. Tic-Tac-Toe")
done = False
while not done:
  try:
    game = input("Enter your number: ")
    if game != "1" and game != "2" and game != "3":
      print("Please choose a game from the list above.")
    else:
      done = True
  except:
    print("Please choose a game from the list above.")

# Mastermind
while game == "1":
# The code is a msatermind game with a three digit code.
# Explains the game to the user.
  print("Welcome to Mastermind.")
  print("")
  time.sleep(1)
  print("In this game you are trying to guess a 3 digits number in the least amount of guesses as possible.")
  time.sleep(3)
  print("Be aware that digits may repeat in the number.")
  time.sleep(2)
  print("After each guess, an X will indicate that the digit is correct, an O will indicate that the digit is in the code but not in that location and a _ will indicate that the digit is not in the code.")
  print("")
  time.sleep(4)

# Generates a code.
  code = random.randint(100, 999)
  code_string = str(code)
  print("The code has been generated.")

# Sets variables to zero
  guess_code = 0
  score = 0

# User guesses until they get it correct.
  while guess_code != code:
    try:
# User makes a guess which is saved as and integer and as a string.
      guess_code = int(input("Please enter your guess: "))
      guess_string = str(guess_code)
# Prints out statement if the guess is not valid.
      if guess_code > 999 or guess_code < 100:
        print("Please enter a THREE digit guess.")
# Runs code if the guess is correct.
      elif guess_code == code:
        print("You guessed the code!")
        score = score + 1
# Runs code if the guess is incorrect but legitimate.
      else:
        for i in range(0, 3):
          if guess_string[i] == code_string[i]:
            print("X", end="")
          elif guess_string[i] in code_string:
            print("O", end="")
          else:
            print("_", end="")
# Keeps track of guesses and goes to a new line.
        print("")
        score = score + 1
# Prints out statement if the guess isn't a number.
    except:
      print("Guesses must be numbers.")



# Prints out the user's score.
  print("Your score is ", score, ".", sep="")
  print("If you would like to play again press 1 if not, press q.")
  game = input("Enter here: ")

# Snake game
while game == "2":
# Explanation of game.

#  print("Welcome to the snake game.")
#  time.sleep(1)
# print("The goal of this game is to grow your snake as long as possible.")
#  time.sleep(3)
 # print("Your snake will grow when it eats the red food dots.")
  #time.sleep(3)
  #print("Use the arrow keys to move your snake.")
  #time.sleep(3)
  #print("The game will end if your snake hits the edge or any part of its body.")
  #time.sleep(4)
  #print("It's time to play, press on the screen when it shows up.")
  #time.sleep(4)


# Imports
  import pygame
  import sys
  pygame.init()

# Setting colour Values.
  black = (0, 0, 0)
  red = (255, 0, 0)
  background_colour = (50, 130, 200)

# Setting coordinate values.
  x_coordinate = 250
  y_coordinate = 150
  x_change = 0
  y_change = 0

# Setting other values.
  snake_square = 10
  score = 0
  length_of_snake = 1
  snake_list = []
  game_over = False
  clock = pygame.time.Clock()

# Creates function for drawing snake at different lengths.
  def our_snake(snake_block, snake_list):
    for x in snake_list:
      pygame.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block])

# Food coordinates
  food_x = int(random.randrange(0, 500, snake_square))
  food_y = int(random.randrange(0, 300, snake_square))

# Creating fonts.
  font = pygame.font.Font('freesansbold.ttf', 32)
  text = font.render("Game over", True, red)
  textRect = text.get_rect()
  textRect.center = (250, 150)

# Creating the screen.
  (width, height) = (500, 300)
  pygame.display.set_caption("Snake Game")
  screen = pygame.display.set_mode((width, height))

# Running the game.
  while not game_over:
# Snake moves on "grid space" when user presses arrow keys.
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -snake_square
                y_change = 0
            elif event.key == pygame.K_RIGHT:
                x_change = snake_square
                y_change = 0
            elif event.key == pygame.K_UP:
                y_change = -snake_square
                x_change = 0
            elif event.key == pygame.K_DOWN:
                y_change = snake_square
                x_change = 0
    x_coordinate += x_change
    y_coordinate += y_change
# Game ends if snake goes off the screen.
    if x_coordinate > 490 or x_coordinate < 0 or y_coordinate > 290 or y_coordinate < 0:
        game_over = True
# Draws the snake.
    screen.fill(background_colour)
    pygame.draw.rect(screen, black, [x_coordinate, y_coordinate, snake_square, snake_square])
    pygame.display.update()
# Draws the food.
    screen.fill(background_colour)
    pygame.draw.rect(screen, red, [food_x, food_y, snake_square, snake_square])
    pygame.display.update()
# Adds length to snake when needed.
    snake_head = []
    snake_head.append(x_coordinate)
    snake_head.append(y_coordinate)
    snake_list.append(snake_head)
    if len(snake_list) > length_of_snake:
      del snake_list[0]
    our_snake(snake_square, snake_list)
    pygame.display.update()
# Game ends if the snake head hits any part of the snake body.
    for x in snake_list[:-1]:
      if x == snake_head:
        game_over = True
# If the snake eats the food then a new peice of food shows up.
    if x_coordinate == food_x and y_coordinate == food_y:
      food_x = round(random.randrange(0, 500, snake_square))
      food_y = round(random.randrange(0, 300, snake_square))
# The score and the length of the snake increases when the snake eats food
      score += 1
      length_of_snake += 1

    pygame.display.update()
    clock.tick(14)

# Tells the user that their game is over.
  screen.fill(black)
  screen.blit(text, textRect)
  pygame.display.update()
# Tells the user what their score is.
  print("Your score is", score)
# Gives the user the option to play again.
  print("If you would like to play again press 2 if not, press q.")
  game = input("Enter here: ")
  if game == "q":
    exit()
    sys.exit()

# Tic-Tac-Toe
while game == "3":
# Imports what is needed for Tic-tac-toe.
  import pygame
  pygame.init()
# Gives the user instructions on how to play.
  print("Welcome to Tic-Tac-Toe.")
  time.sleep(1)
  print("The goal of Tic-Tac-Toe is to get three in a row.")
  time.sleep(3)
  print("You will be playing against an AI.")
  time.sleep(2)
  print("You will go first, on your turn, click the space where you want to play.")
  time.sleep(3)
  print("The game is starting now.")
# Creates colours needed for tic-tac-toe.
  black = (0, 0, 0)
  blue = (0, 0, 225)
  red = (255, 0, 0)
  white = (255, 255, 255)

# Draws the screen.
  (width, height) = (525, 300)
  pygame.display.set_caption("Tic-tac-toe")
  screen = pygame.display.set_mode((width, height))
  screen.fill(white)

# Draws the tic-tac-toe board.
  pygame.draw.rect(screen, black, [175, 5, 5, 290])
  pygame.draw.rect(screen, black, [350, 5, 5, 290])
  pygame.draw.rect(screen, black, [5, 100, 515, 5])
  pygame.draw.rect(screen, black, [5, 200, 515, 5])
  pygame.display.update()

# Sets the values for coordinates for drawing x's and o's.
  coodinate_values_x = {0: 87.5, 1: 262.5, 2: 437.5}
  coodinate_values_y = {0: 50, 1: 150, 2: 250}

# Sets variables to zero, empty, and false.
  game_done = False
  list_of_coordinates = []
  circle_coordinates = []
  square_coordinates = []
  plays = 0
  board = [["", "", ""], ["", "", ""], ["", "", ""]]
  winner = ""

# Sets the values for the coordninates of the diagonals.
  left_diagonal_coordinates = [(0, 0), (1, 1), (2, 2)]
  right_diagonal_coordinates = [(2, 0), (1, 1), (0, 2)]

# Creates a function to see if someone has won.
  def has_someone_won(coordinates_for_shape):
    game_finished = False
    for i in coordinates_for_shape:
      occurances_x = 0
      occurances_y = 0
      for j in coordinates_for_shape:
        if i[0] == j[0]:
          occurances_x += 1
        if i[1] == j[1]:
          occurances_y += 1
        if occurances_x >= 3:
          game_finished = True
        if occurances_y >= 3:
          game_finished = True
    if (0, 0) in coordinates_for_shape and (1, 1) in coordinates_for_shape and (2, 2) in coordinates_for_shape:
      game_finished = True
    if (0, 2) in coordinates_for_shape and (1, 1) in coordinates_for_shape and (2, 0) in coordinates_for_shape:
      game_finished = True
    return game_finished

# Creates a function for AI strategic movement.
  def ai_movement():
# Sets variables to empty and False.
    x_coordinate_of_ai = ""
    y_coordinate_of_ai = ""
    y_has_value = False
    x_has_value = False
# AI takes the win if it can.
# Checks if AI can win in rows and columns.
    for i in range(3):
      total_column = 0
      spaces_column = 0
      total_row = 0
      spaces_row = 0
      for j in range(3):
        if board[j][i] == "x":
          total_column += 1
        if board[j][i] == "":
          spaces_column += 1
        if board[i][j] == "x":
          total_row += 1
        if board[i][j] == "":
          spaces_row += 1
      if total_column == 2 and spaces_column == 1:
        x_coordinate_of_ai = i
        x_has_value = True
      if not x_has_value:
        if total_row == 2 and spaces_row == 1:
            y_coordinate_of_ai = i
            y_has_value = True
# Checks if AI can win in diagonals.
    if not x_has_value and not y_has_value:
      left_diagonal = 0
      right_diagonal = 0
      spot_1 = ""
      spot_2 = ""
      for i in left_diagonal_coordinates:
        if board[i[1]][i[0]] == "x":
          left_diagonal += 1
        if board[i[1]][i[0]] == "":
          spot_1 = i
      for i in right_diagonal_coordinates:
        if board[i[1]][i[0]] == "x":
          right_diagonal += 1
        if board[i[1]][i[0]] == "":
          spot_2 = i
      try:
        if left_diagonal == 2 and spot_1 == "":
          x_coordinate_of_ai = spot_1[0]
          y_coordinate_of_ai = spot_1[1]
          x_has_value = True
          y_has_value = True
        elif right_diagonal == 2 and spot_2 == "":
          x_coordinate_of_ai = spot_2[0]
          y_coordinate_of_ai = spot_2[1]
          x_has_value = True
          y_has_value = True
      except:
        pass
# AI blocks the player if the player will win next turn.
# Checks rows and columns to see if the player can win.
    if not x_has_value and not y_has_value:
      for i in range(3):
        total_column = 0
        spaces_column = 0
        total_row = 0
        spaces_row = 0
        for j in range(3):
          if board[j][i] == "o":
            total_column += 1
          if board[j][i] == "":
            spaces_column += 1
          if board[i][j] == "o":
            total_row += 1
          if board[i][j] == "":
            spaces_row += 1
        if total_column == 2 and spaces_column == 1:
          x_coordinate_of_ai = i
          x_has_value = True
        if not x_has_value and not y_has_value:
          if total_row == 2 and spaces_row == 1:
            y_coordinate_of_ai = i
            y_has_value = True
# Checks the diagonals to see if the player can win.
    if not x_has_value and not y_has_value:
      left_diagonal_block = 0
      right_diagonal_block = 0
      spot_1_block = ""
      spot_2_block = ""
      for i in left_diagonal_coordinates:
        if board[i[1]][i[0]] == "o":
          left_diagonal_block += 1
        if board[i[1]][i[0]] == "":
          spot_1_block = i
      for i in right_diagonal_coordinates:
        if board[i[1]][i[0]] == "o":
          right_diagonal_block += 1
        if board[i[1]][i[0]] == "":
          spot_2_block = i
      try:
        if left_diagonal_block == 2 and spot_1_block != "":
          x_coordinate_of_ai = spot_1_block[0]
          y_coordinate_of_ai = spot_1_block[1]
          x_has_value = True
          y_has_value = True
        elif right_diagonal_block == 2 and spot_2_block != "":
          x_coordinate_of_ai = spot_2_block[0]
          y_coordinate_of_ai = spot_2_block[1]
          x_has_value = True
          y_has_value = True
      except:
        pass
# Function returns a list of important values.
    return[x_coordinate_of_ai, y_coordinate_of_ai, x_has_value, y_has_value]

# Runs through the game loop.
  while not game_done:
# Runs through the player's turn.
    for event in pygame.event.get():
# Sets the coordinates for drawing the o if it's valid.
      if event.type == pygame.MOUSEBUTTONDOWN:
        valid = False
        if pygame.mouse.get_pressed()[0]:
          position = pygame.mouse.get_pos()
          x_coordinate = position[0] // 175
          y_coordinate = position[1] // 100
          if (x_coordinate, y_coordinate) not in list_of_coordinates:
            valid = True
        if valid:
          x_coordinate_of_o = coodinate_values_x[x_coordinate]
          y_coordinate_of_o = coodinate_values_y[y_coordinate]
# Draws the o and adds it's coordinates to lists.
          pygame.draw.circle(screen, red, [x_coordinate_of_o, y_coordinate_of_o], 38)
          pygame.draw.circle(screen, white, [x_coordinate_of_o, y_coordinate_of_o], 32)
          coordinates = (x_coordinate, y_coordinate)
          list_of_coordinates.append(coordinates)
          circle_coordinates.append(coordinates)
# Updates screen, the number of plays and the board.
          pygame.display.update()
          plays += 1
          board[y_coordinate][x_coordinate] = "o"
# Checks if the player has won.
          game_done = has_someone_won(circle_coordinates)
          if game_done:
            winner = "You are"
# Checks if the board is full.
          if plays >= 9 and winner == "":
              game_done = True
              winner = "Tie"
          time.sleep(0.25)
# Runs through the AI's turn.
          if not game_done:
            ai_coordinates = list_of_coordinates[0]
            while ai_coordinates in list_of_coordinates:
# AI takes the spot to block or win if possible.
              list_of_values = ai_movement()
              x_coordinate_of_ai = list_of_values[0]
              y_coordinate_of_ai = list_of_values[1]
              x_has_value = list_of_values[2]
              y_has_value = list_of_values[3]
# Generates a random value if AI couldn't win or block.
              if not x_has_value:
                x_coordinate_of_ai = int(random.randrange(0, 3))
              if not y_has_value:
                y_coordinate_of_ai = int(random.randrange(0, 3))
# Makes the coordninates into a set.
              ai_coordinates = (x_coordinate_of_ai, y_coordinate_of_ai)
# Adds the final coordinates to lists.
            list_of_coordinates.append(ai_coordinates)
            square_coordinates.append(ai_coordinates)
# Generates the coordinates for the x on the screen.
            x_coordinate_square = (coodinate_values_x[x_coordinate_of_ai]) - 15
            y_coordinate_square = (coodinate_values_y[y_coordinate_of_ai]) - 15
# Draws the left diagonal of the x.
            pygame.draw.line(screen, blue, (x_coordinate_square - 20, y_coordinate_square - 20), (x_coordinate_square + 50, y_coordinate_square + 50), 8)
# Draws the right diagonal of the x.
            pygame.draw.line(screen, blue, (x_coordinate_square + 50, y_coordinate_square - 20), (x_coordinate_square - 20, y_coordinate_square + 50), 8)
# Updates the screen, the number of plays and the board.
            pygame.display.update()
            plays += 1
            board[y_coordinate_of_ai][x_coordinate_of_ai] = "x"
# Checks if the AI has won.
            game_done = has_someone_won(square_coordinates)
            if game_done:
              winner = "The computer is"

# Tells the user that the game is over and who won.
  print("Game Over")
  if winner == "Tie":
    print("The game was a tie.")
  else:
    print(winner, "the winner.")


# Asks user if they want to play again.
  print("If you would like to play again press 3 if not, press q.")
  game = input("Enter here: ")
