
from inquirer import Text, prompt, List,Checkbox
from re import match



class Player:
    SYMBOL = ["X","O"]

    def __init__(self) -> None:
        self.name :str = ""
        self.symbol: str = ""


    def ChooseName(self) :
        name = [
            Text('Name', message="What's your Name",
                        validate=lambda _, x: match('[A-Za-z]', x))
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
                                message="How long time do you wnat",
                                choices=Menu.TIME,
                                ),
            ]
            choice_itme = prompt(time)
            self.time = sum(choice_itme["Time"])

        print(self.time)




    def DisplayEndMenu(self):
        pass









class Board:
    def __init__(self,board:list) -> None:
        self.board = []

    def DisplayBoard(self):
        pass


    def ResetBoard(self):
        pass

    def UpdateBoard(self):
        pass










class Game:
    def __init__(self,board,players:list,menu,current_player:int) -> None:
        self.board = board
        self.players = []
        self.menu = menu
        self.current_player = current_player
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
test = Menu()
test.DisplayMainMenu()
