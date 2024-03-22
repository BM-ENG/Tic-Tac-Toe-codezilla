class Player:
    def __init__(self,name:str,symbol:str) -> None:
        self.name = name
        self.symbol = symbol


    def ChooseName(self):
        pass

    def ChooseSymbol(self):
        pass








class Menu:
    def DisplayMainMenu(self):
        pass

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
