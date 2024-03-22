
import types
from inquirer import Text, prompt, List,Checkbox
from re import match

intro:str ="""


▀█▀ █ █▀▀   ▀█▀ ▄▀█ █▀▀   ▀█▀ █▀█ █▀▀
░█░ █ █▄▄   ░█░ █▀█ █▄▄   ░█░ █▄█ ██▄



"""

class Player:
    SYMBOL:list[str] = ["✘","⭕"]

    def __init__(self) -> None:
        self.name :str = ""
        self.symbol: str = ""


    def ChooseName(self) :
        name = [
            Text('Name', message="What's your Name",
                        validate=lambda _, x: match('^[a-zA-Z]+$', x))
                    ]

        self.name = prompt(name)['Name']

    def ChooseSymbol(self) :
        symbol = [
          List('symbol',
                        message="What symbol do you need?",
                        choices=self.SYMBOL,
                    ),
        ]
        self.symbol = prompt(symbol)['symbol']










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
    def __init__(self) -> None:
        self.zone: dict[str,str] = {
                      "1":"","2":"✘","3":"",
                      "4":"✘","5":"","6":"",
                      "7":"","8":"✘","9":""
                     }
        self.board:str ="""
                     ⁣1 ❕2 ❕3
                     ➖➕➖➕➖
                     6 ❕⁣5 ❕4
                     ➖➕➖➕➖
                     7 ❕8 ❕9
                     """

    def UpdateBoard(self):
        for position,symbol in self.zone.items():
            if symbol:
                self.board=self.board.replace(position,symbol)




    def ResetBoard(self):
        self.zone = {
                      "1":"","2":"","3":"",
                      "4":"","5":"","6":"",
                      "7":"","8":"","9":""
                     }
        self.board = self.BOARD


    def DisplayBoard(self):
        return self.board










class Game:
    def __init__(self) -> None:
        self.board = "board"
        self.players = []
        self.menu = "menu"
        self.current_player = "current_player"
    def StarGame(self):
        pass

    def PlayTurn(self):
        pass

    def CheckWin(self):
        pass

    def CheckDraw(self):
        pass

    def RestartGame(self):
        pass

    def QuitGame(self):
        pass
test_palayer = Player()
test_Board = Board()
test_menu = Menu()
test_Game = Game()

print(test_Board.DisplayBoard())

print(test_Board.DisplayBoard())
