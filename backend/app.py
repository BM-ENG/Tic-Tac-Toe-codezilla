
from os import name, system
from posix import remove
import types
from typing_extensions import Counter
from inquirer import Text, prompt, List,Checkbox
from re import match
from tqdm import tqdm
from time import sleep

intro:str ="""


▀█▀ █ █▀▀   ▀█▀ ▄▀█ █▀▀   ▀█▀ █▀█ █▀▀
░█░ █ █▄▄   ░█░ █▀█ █▄▄   ░█░ █▄█ ██▄



"""

class Player:
    SYMBOL:list[str] = ["✘","⭕","💣","🔲","🌀"]

    def __init__(self) -> None:
        self.name :str = ""
        self.symbol: str = ""


    def ChooseName(self) -> str:
        name = [
            Text('Name', message="What's your Name",
                        validate=lambda _, x: match('^[a-zA-Z]+$', x))
                    ]

        self.name = prompt(name)['Name']
        return self.name

    def ChooseSymbol(self,name_player="Unknow") -> str:
        symbol = [
          List('symbol',
                        message=f"What symbol do you need {name_player} ?",
                        choices=self.SYMBOL,
                    ),
        ]
        self.symbol = prompt(symbol)['symbol']
        return self.symbol











class Menu:
    TIME = [5,10,15]
    def __init__(self) -> None:
        self.time = 5

    def DisplayMainMenu(self):
        main = [
          List('main',
                        message="Welcome in game TIC TAC TOE",
                        choices=["Start Game","Setting Time","Quit Game"],
                    )
                ]
        choice = prompt(main)
        if choice["main"] == "Setting Time":
            time = [
              Checkbox('Time',
                                message="Enter space to choose time long in game",
                                choices=Menu.TIME,
                                ),
            ]
            choice_itme = prompt(time)
            self.time = sum(choice_itme["Time"])
            return prompt(main)['main']
        return choice['main']







    def DisplayEndMenu(self):
        main = [
          List('main',
                        message="Game Over",
                        choices=["Restart Game","Quit Game"],
                    )
                ]
        return  prompt(main)["main"]









class Board:
    BOARD:str = """

                 ⁣1 ❕2 ❕3
                 ➖➕➖➕➖
                 6 ❕⁣5 ❕4
                 ➖➕➖➕➖
                 7 ❕8 ❕9

    """
    #
    def __init__(self) -> None:
        self.zone: dict[str,str] = {
                      "1":"","2":"","3":"",
                      "4":"","5":"","6":"",
                      "7":"","8":"","9":""
                     }
        self.board:str =self.BOARD
    #
    def UpdateBoard(self,symbol:str,name_player:str)-> None:

        choice = [
            List('position',
                message=f"What position do you need {name_player}?",
                choices=[position for position,symbol in self.zone.items() if not symbol],
            ),
        ]
        position = prompt(choice)["position"]
        self.zone[position]= symbol

        for position,symbol in self.zone.items():
            if symbol:
                self.board=self.board.replace(position,symbol)


    #
    def ResetBoard(self)-> None:
        self.zone = {str(i):"" for i in range(1,10)}
        self.board = self.BOARD

    #
    def DisplayBoard(self)-> None:
        print(self.board)










class Game:
    def __init__(self) -> None:
        self.board = Board()
        self.players = [Player(),Player()]
        self.menu = Menu()
        self.current_player = 0
    def StarGame(self):
        symbol_new = Player().SYMBOL
        while True:

                self.intro(intro)
                choice =  self.menu.DisplayMainMenu()
                self.clear()
                if choice == "Start Game":
                    for player in self.players:
                        self.intro(intro)
                        name_player = player.ChooseName()
                        symbol_player = player.ChooseSymbol(name_player)
                        self.players[1].SYMBOL.remove(symbol_player)
                        self.clear()
                    self.WaitAWhiel("Initializing")
                    self.PlayTurn()
                else:
                    return self.WaitAWhiel("Terminate the game active")
                while True:
                    choice_after = self.menu.DisplayEndMenu()
                    if choice_after == "Restart Game":
                        self.clear()
                        self.WaitAWhiel("Initializing")
                        self.board.ResetBoard()
                        self.PlayTurn()
                    else:
                        self.board.ResetBoard()
                        for player in self.players:
                            player.SYMBOL = ["✘","⭕","💣","🔲","🌀"]
                        break




    def PlayTurn(self):
        for _ in range(9):
            self.clear()
            self.intro(intro)
            self.board.DisplayBoard()
            self.board.UpdateBoard(self.players[self.current_player].symbol,self.players[self.current_player].name)
            self.current_player = 1 - self.current_player
            # if self.CheckWin():
            #     return self.WaitAWhiel("Found Winner")
            if self.CheckDraw():
                self.board.DisplayBoard()
                return self.WaitAWhiel("Game Over and No Winner (Draw)")




    def CheckWin(self):
        help =  1
        counter = 1
        range_help = 3
        for i in range(1,5):
            for _ in range(range_help):
                if (self.board.zone[str(help)]) == (self.board.zone[(str(help:= help+i))]) and (self.board.zone[(str(help))]) == (self.board.zone[(str(help:= help+i))]):
                    return True
                help += counter
            help =  1
            counter += 1
            if i == 1 or i == 3:
                range_help = 1
                if i == 1:
                    help = 3
                continue
            range_help = 3




    def CheckDraw(self) -> bool:
        for position, symbol in self.board.zone.items():
            if not symbol:
                return False
        return True

    def RestartGame(self):
        return self.menu.DisplayMainMenu()

    def QuitGame(self):
        return self.menu.DisplayMainMenu()

    def WaitAWhiel(self, message:str):
        print(message)
        return [sleep(0.01) for _ in tqdm(range(1,100))]
    def clear(self)-> None:
        system("cls") if name=="nt" else system("clear")
    def intro(self,intro_ascii:str):
        print(intro_ascii)
test_palayer = Player()
test_Board = Board()
test_menu = Menu()
test_Game = Game()
test_Game.StarGame()
