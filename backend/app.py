
import sys
from os import name, system,listdir,environ
environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"


from inquirer.render.console import Path
from pygame import mixer
from datetime import datetime
from inquirer import Text, prompt, List,Checkbox
from re import match
from tqdm import tqdm
from time import sleep
from simple_chalk import chalk
from random import choice

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

    def DisplayMainMenu(self,active=False):
        if active:
            main = [
            List('main',
                            message="Welcome in game TIC TAC TOE",
                            choices=["Start Game","Setting Time","Show information","Show archive","Board saved","Logout"],
                        )
                    ]
        else:

            main = [
            List('main',
                            message="Welcome in game TIC TAC TOE",
                            choices=["Start Game","Setting Time","Back"],
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

    def ShowInformation(self,data):
        for type, data in (data[0]).items():
            print(f"{chalk.green(type)}:{chalk.white(len(data) if (type == "GameArchive" or type == "BoardArchive") else data)} ")

    def ShowArchive(self,data):
            if data[0]["GameArchive"]:
                for time, data in (data[0]["GameArchive"]).items():
                    print(f"{chalk.green(time)}:{chalk.white(data)}")
            else:
                print(chalk.red("You haven't played games yet!!"))











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

                 ⁣1 ❕ 2 ❕3
                 ➖➕➖➕➖
                 6 ❕⁣ 5 ❕4
                 ➖➕➖➕➖
                 7 ❕ 8 ❕9

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


    def TimerGame(self,t):
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(chalk.green(timer))
            sleep(1)
            t -= 1













class Game:
    def __init__(self) -> None:
        self.board = Board()
        self.players = [Player(),Player()]
        self.menu = Menu()
        self.current_player = 0
        self.record_game = {}
        self.data = None




    def StarGame(self,active=False,data=False):

        self.data = data

        symbol_new = Player().SYMBOL
        while True:
                self.intro(intro)
                choice =  self.menu.DisplayMainMenu(active)
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
                elif choice == "Show information":
                    self.menu.ShowInformation(data)
                    continue

                elif choice == "Show archive":
                    self.menu.ShowArchive(self.data)
                    continue

                elif choice == "Board saved":
                    print(chalk.red("this feature in not yet available !!"))
                    continue

                else:
                     self.WaitAWhiel("Back to start menu active")
                     return self.data
                while True:
                    choice_after = self.menu.DisplayEndMenu()
                    if choice_after == "Restart Game":
                        self.clear()
                        self.WaitAWhiel("Initializing")
                        self.board.ResetBoard()
                        self.PlayTurn()
                    else:
                        self.data[0]["GameArchive"]= {**self.data[0]["GameArchive"],**self.record_game}
                        self.record_game = {}
                        self.board.ResetBoard()
                        for player in self.players:
                            player.SYMBOL = ["✘","⭕","💣","🔲","🌀"]
                        break




    def PlayTurn(self):

        for _ in range(9):

            self.clear()
            self.intro(intro)
            self.board.DisplayBoard()
            self.board.UpdateBoard(symbol=self.players[self.current_player].symbol,name_player=self.players[self.current_player].name)

            if (self.CheckWin(self.players[self.current_player].name)):
                self.RocordGame(winner=self.players[self.current_player].name,loser=self.players[1 - self.current_player].name,draw=False)
                return
            self.current_player = 1 - self.current_player

            if self.CheckDraw():
                self.RocordGame(winner=self.players[0].name,loser=self.players[1].name,draw=True)
                self.board.DisplayBoard()
                return self.WaitAWhiel("Game Over and No Winner (Draw)")




    def CheckWin(self,turn:str):
        wins = [
               ["1","2","3"],["4","5","6"],["7","8","9"],
               ["1","6","7"],["2","5","8"],["3","4","9"],
               ["1","5","9"],["3","5","7"]
        ]

        for win in wins:
            if ((self.board.zone[win[0]] == self.board.zone[win[1]] and self.board.zone[win[1]] == self.board.zone[win[2]]) and (self.board.zone[win[0]] != "")):
                self.WaitAWhiel(f"Congratulations {turn} you are a hero ")
                for position,symbol in self.board.zone.items():
                    if position in win:
                        self.board.zone.update({position:"🎉"})
                self.board.board = self.board.BOARD
                for position,symbol in self.board.zone.items():
                    if symbol:
                        self.board.board=self.board.board.replace(position,symbol)
                print(self.board.board)
                return True
        return False






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

    def Sound(self,sound:str,volume:float=0.5,time:int=True,star=True,stop=False,loop:int=-1)-> None:
        mixer.init()
        if stop:
            mixer.music.stop()
            return
        if star:

            path = "/Users/HikoDz/Desktop/Tic-Tac-Toe-codezilla/backend/sound"
            random_sound = choice(listdir(f"{path}/{sound}"))
            mixer.music.load(f'{path}/{sound}/{random_sound}',namehint="mp3")
            mixer.music.set_volume(volume)
            mixer.music.play(loop)

    def RocordGame(self,winner,loser,draw=False):
        now = datetime.now()
        if draw:
            self.record_game[now.strftime("%d/%m/%Y %H:%M:%S")] = f"A tie between  {winner} and {loser}"
        else:

            self.record_game[now.strftime("%d/%m/%Y %H:%M:%S")] = f"the winner was {winner} and the loser {loser}"
