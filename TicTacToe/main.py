from time import sleep
from rich.traceback import install
from rich.console import Console
from board_model import Board

install()
console = Console()
board = Board()


  
def play_again():
  print()
  answer = input('Do you want to play again? (y/n): ').lower()
  if answer == 'y':
    for num in range(9):
      board.position_display[num] = '-'
    print()
    main()
  elif not answer.isalpha() and len(answer) != 1:
    console.print('\nInvalid input! Enter y or n.', style='bold red')
    play_again()
  
        
 
def main():
  # .........................................Game Welcome Text.........................................
  console.print('\n----------------------------- TIC TAC TOE ----------------------------\n', style='bold red')
  
  board.game_board()
  player = input('Enter your name: ').title()
  player_symbol = 'X'
  computer_symbol = 'O'
  
  console.print()
   
  try: 
    while '-' in Board.position_display:
      console.print(f'{player} thinking...\n', style='bold yellow')
      board.player_turn(player_symbol)
      if board.player_wins():
        sleep(0.5)
        console.print(f'\n{player} wins🎉 Congratulations🎉', '\nGame over...')
        break
    
      board.computer_turn(computer_symbol=computer_symbol)
      if board.computer_wins():
        sleep(0.5)
        console.print(f'\nComputer wins🎉', '\nGame over...')
        break
        
  except RecursionError:
    if '-' not in Board.position_display:
      if not board.player_wins() and not board.computer_wins():
        sleep(0.5)
        console.print(f"It's a Draw.\nGame over...")
      
  play_again()
   
   
if __name__ == '__main__':
  main()
  
                                  
  