######################################################
#                                                    #
# Tic tac toe, displayed in the command line to be   #
# played by 2 players                                #                  
#                                                    #
######################################################

# Display the board
def display_board(board_values):
  print(f'\n     |     |     ')
  print(f'  {board_values[0][0]}  |  {board_values[0][1]}  |  {board_values[0][2]}  ')
  print(f'_____|_____|_____')
  print(f'     |     |     ')
  print(f'  {board_values[1][0]}  |  {board_values[1][1]}  |  {board_values[1][2]}  ')
  print(f'_____|_____|_____')
  print(f'     |     |     ')
  print(f'  {board_values[2][0]}  |  {board_values[2][1]}  |  {board_values[2][2]}  ')
  print(f'     |     |     \n')

# Get user character choice
def get_character_choice():
  choice = ''
  while choice not in ['X', 'O']:
    choice = input("Player 1 select your character 'X' or 'O' ")

  if choice == 'X':
    print("Player 1 chose 'X' they will go first\n")
    return { 'X': "Player 1", 'O': "Player 2" }
  else:
    print("Player 1 chose 'O', Player 2 will go first\n")
    return { 'O': "Player 1", 'X': "Player 2" }

# Get users position choice
def get_position_choice(board_values):
  #Placeholder value
  valid_position = False
  board_positions = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
  
  while not valid_position:
    user_input = input("Select a space (1 - 9): ")

    # Check if position is already taken and if is in range
    if user_input in board_positions:
      integer_input = int(user_input)
      # Convert input into row and column indexes
      if 0 < integer_input < 4:
        row = 0
      elif 3 < integer_input < 7:
        row = 1
      else: 
        row = 2
      
      if integer_input in [1, 4, 7]:
        col = 0
      elif integer_input in [2, 5, 8]:
        col = 1
      else:
        col = 2

      if board_values[row][col] == '-':
        valid_position = True
        # Return index position to be used for board updating
        return (row, col)
      else:
        print("Oops that space is already taken!")

    else:
      print("That number isn't on the board! Please select a number between 1 and 9\n")

# Update board
def update_board(position, player_character, board_values):
  board_values[position[0]][position[1]] = player_character
  return board_values

def reset_board(board_values):
  for i, row in enumerate(board_values):
      for j, item in enumerate(row):
        board_values[i][j] = '-'
  
  return board_values

# Check if game is won 
def game_over(board_values, move_count):
    result = ''
    if move_count == 8:
      result = 'Draw'
    
    # Loop over board to check if it matches, only need to add if for index 1 as that must be filled in for possible winner
    for i, row in enumerate(board_values):
      for j, item in enumerate(row):
        if i == 1:
          if board_values[i - 1][j] == board_values[i + 1][j] == board_values[i][j] != '-':
            result = 'Win'
        if j == 1:
          if board_values[i][j - 1] == board_values[i][j + 1] == board_values[i][j] != '-':
            result = 'Win'
    
    # Check for only 2 possible diagonal solutions
    if board_values[0][0] == board_values[1][1] == board_values[2][2] != '-' or board_values[2][0] == board_values[1][1] == board_values[0][2] != '-':
      result = 'Win'

    return result

# Decide whether to play again
def play_again():
  choice = ''
  while choice not in ['Y', 'N']:
    choice = input("Would you like to play again 'Y' Yes or 'N' No: ")

  return choice == 'Y'

# Main game loop

# Used to measure game length
move_count = 0

# Create initial 2D list of values for the board
board_values = []
for i in range(0, 3):
  board_values.append(['-']*3)

game_playing = True

# X will always go first
current_player = 'X'

# Choose character X or O, swap current player if needed
player_characters = get_character_choice()

while game_playing:
  # Gather choice, display updated board
  position = get_position_choice(board_values)
  update_board(position, current_player, board_values)
  display_board(board_values)
  
  # Check if game over
  result = game_over(board_values, move_count)
  if result in ['Win', 'Draw']:
    game_playing = False
    if result == 'Draw':
      print("This game was draw...")
    else:
      print(f"{player_characters[current_player]} IS THE WINNER")
    
    # Check if want to play agian
    if play_again():
      # Reset player, board and playing boolean
      board_values = reset_board(board_values)
      player_characters = get_character_choice()
      current_player = 'X'
      game_playing = True
    else:
      break
    
  else:
      # Switch player
    if current_player == 'X':
      current_player = 'O'
    elif current_player == 'O':
      current_player = 'X'

    move_count += 1






