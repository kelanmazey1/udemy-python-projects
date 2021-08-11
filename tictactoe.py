######################################################
#                                                    #
# Tic tac toe, displayed in the command line to be   #
# played by 2 players                                #                  
#                                                    #
######################################################

# Display the board
def display_board(board_values):
  print(f'\n     |     |     ')
  print(f'  {board_values[0]}  |  {board_values[1]}  |  {board_values[2]}  ')
  print(f'_____|_____|_____')
  print(f'     |     |     ')
  print(f'  {board_values[3]}  |  {board_values[4]}  |  {board_values[5]}  ')
  print(f'_____|_____|_____')
  print(f'     |     |     ')
  print(f'  {board_values[6]}  |  {board_values[7]}  |  {board_values[8]}  ')
  print(f'     |     |     \n')

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
      
      if board_values[integer_input - 1] == '-':
        valid_position = True
        # Return index position to be used for board updating
        return integer_input - 1
      else:
        print("Oops that space is already taken!")

    else:
      print("That number isn't on the board! Please select a number between 1 and 9\n")

# Update board
def update_board(position_index, player_character, board_values):
  board_values[position_index] = player_character
  return board_values


# Check if game is won 


# Decide whether to play again


# Main game loop
# Create initial list of values for the board
board_values = ['-'] * 9
get_position_choice(board_values)
display_board(board_values)
# Choose X or O

# Gather choice, display updated board

# Check if game won

# Check if want to play agian