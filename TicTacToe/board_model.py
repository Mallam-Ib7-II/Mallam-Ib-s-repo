from rich.console import Console
from time import sleep
from random import randint



console = Console()

class Board:
    
    position_display = [
        '-', '-', '-',
        '-', '-', '-',
        '-', '-', '-',
    ]
    
    def __init__(self):
        pass
        

    def game_board(self) -> None:
        console.print(self.position_display[0], self.position_display[1], self.position_display[2], sep=' | ', style='bold green')
        console.print('----------', style='bold yellow')
        console.print(self.position_display[3], self.position_display[4], self.position_display[5], sep=' | ', style='bold red')
        console.print('----------', style='bold yellow')
        console.print(self.position_display[6], self.position_display[7], self.position_display[8], sep=' | ', style='bold blue')
        console.print()
  
  
    def player_turn(self, player_symbol):
        player_position = input('Enter a position (1 - 9): ')
        if player_position.isdigit() and 0 < int(player_position) < 10 and len(player_position) == 1:
            player_position = int(player_position)
            player_position -= 1
            if Board.position_display[player_position] != player_symbol and Board.position_display[player_position] == '-':
                Board.position_display[player_position] = player_symbol
                sleep(0.5)
                console.print()
                self.game_board()
                
            else:
                console.print('\nOops! Position already occupied.\n', style='bold red')
                self.player_turn(player_symbol)
        else:
            console.print('\nInvalid input!!!\n', style='bold red')
            self.player_turn(player_symbol)
    
    
    def computer_turn(self, computer_symbol):
        computer_pos = randint(0, 8)
        if self.position_display[computer_pos] == '-':
            self.position_display[computer_pos] = computer_symbol
            sleep(0.5)
            console.print('Computer thinking...\n', style='bold yellow')
            sleep(0.5)
            self.game_board()
        else:
            self.computer_turn(computer_symbol)
    
    
    def player_wins(self) -> bool:
        if self.position_display[0] == self.position_display[1] == self.position_display[2] == 'X':
            return True
        elif self.position_display[3] == self.position_display[4] == self.position_display[5] == 'X':
            return True
        elif self.position_display[6] == self.position_display[7] == self.position_display[8] == 'X':
            return True
        elif self.position_display[3] == self.position_display[0] == self.position_display[6] == 'X':
            return True
        elif self.position_display[1] == self.position_display[4] == self.position_display[7] == 'X':
            return True
        elif self.position_display[2] == self.position_display[8] == self.position_display[5] == 'X':
            return True
        elif self.position_display[0] == self.position_display[4] == self.position_display[8] == 'X':
            return True
        elif self.position_display[2] == self.position_display[4] == self.position_display[6] == 'X':
            return True
       
        
    def computer_wins(self) -> bool:
        if self.position_display[0] == self.position_display[1] == self.position_display[2] == 'O':
            return True
        elif self.position_display[3] == self.position_display[4] == self.position_display[5] == 'O':
            return True
        elif self.position_display[6] == self.position_display[7] == self.position_display[8] == 'O':
            return True
        elif self.position_display[3] == self.position_display[0] == self.position_display[6] == 'O':
            return True
        elif self.position_display[1] == self.position_display[4] == self.position_display[7] == 'O':
            return True
        elif self.position_display[2] == self.position_display[8] == self.position_display[5] == 'O':
            return True
        elif self.position_display[0] == self.position_display[4] == self.position_display[8] == 'O':
            return True
        elif self.position_display[2] == self.position_display[4] == self.position_display[6] == 'O':
            return True

        
   