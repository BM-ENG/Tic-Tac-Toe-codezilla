import sys
from app import Game
import firebase_admin
from firebase_admin import credentials,firestore
from random import choices, randint
from tqdm import tqdm
from inquirer import Text, prompt, List,Checkbox
from re import match
from simple_chalk import chalk



cred = credentials.Certificate("/Users/HikoDz/Desktop/Tic-Tac-Toe-codezilla/backend/info_token_db.json")
firebase_admin.initialize_app(cred,{'databaseURL':'https://tic-tac-toe-codezilla-default-rtdb.firebaseio.com/'})
db = firestore.client()
class Main:
    def __init__(self) -> None:
        self.signup = SignUp()
        self.lognin = LognIn()
        self.game = Game()


    def MainGame(self):
        self.game.Sound('intro')
        while True:
            choice = [
            List('symbol',
                            message=f"What choice do you need?",
                            choices=["Logn In","Sign Up","Guest (Try Game!)","Quit"],
                        ),
            ]

            choice = prompt(choice)
            if choice["symbol"] == "Sign Up":
                self.signup.Sign_up()

            elif choice["symbol"] == "Logn In":
                self.signup.Sign_up()
            elif choice["symbol"] == "Guest (Try Game!)":
                self.game.Sound('intro',stop=True)
                self.game.StarGame()
            else:
                self.game.WaitAWhiel("Terminate the game active")
                return




class SignUp:
    def Sign_up(self):


        info = [
            Text('FullName', message="Please enter full name",validate=lambda _, x: match(r'^[a-zA-Z]+$', x)),
            Text('UserName', message="Please enter username",validate=lambda _, x: match(r'^[a-zA-Z0-9]+$', x)),
            Text('Email', message="Please enter your email",validate=lambda _, x: match(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', x)),
            Text('Password', message="Please enter password",validate=lambda _, x: match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$', x))
                    ]
        info = prompt(info)
        self.UploadData(info)
        print(f"{chalk.green("Registered successfuly you can now")} {chalk.yellow("login")}!")


    def SendMail(self):
        pass
    def UploadData(self,data):
        db.collection("Players").document(data['UserName']).set(data)




class LognIn:
    def Logn_in(self):
        info = [
            Text('UserName', message="Please enter username",validate=lambda _, x: match('^[a-zA-Z0-9]+$', x)),
            Text('Password', message="Please enter password",validate=lambda _, x: match('^[a-zA-Z0-9]{8}+$', x)),

                    ]
        info = prompt(info)
    def SearchPlayer(self):
        pass
test_Main  = Main()
test_Main.MainGame()
