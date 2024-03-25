
from datetime import datetime
import sys
from time import sleep
from simple_chalk.src.utils.join import join
from backend.app import Game
import firebase_admin
from firebase_admin import credentials,firestore
from google.cloud.firestore_v1.base_query import FieldFilter
from random import choices, randint
from tqdm import tqdm
from inquirer import Text, prompt, List,Checkbox
from re import match
from simple_chalk import chalk
from random import choice
from string import punctuation ,ascii_letters ,digits




cred = credentials.Certificate("/Users/HikoDz/Desktop/Tic-Tac-Toe-codezilla/backend/info_token_db.json")
firebase_admin.initialize_app(cred,{'databaseURL':'https://tic-tac-toe-codezilla-default-rtdb.firebaseio.com/'})
db = firestore.client()
class Main:
    def __init__(self) -> None:
        self.signup = SignUp()
        self.lognin = LognIn()
        self.game = Game()
        self.information = {}



    def MainGame(self):


        while True:

            choice = [
            List('choice',
                            message=f"What choice do you need?",
                            choices=["Logn In","Sign Up","Guest (Try Game!)","Quit"],
                        ),
            ]

            choice = prompt(choice)
            self.game.clear()
            if choice["choice"] == "Sign Up":
                self.signup.Sign_up()

            elif choice["choice"] == "Logn In":
                status_login = self.lognin.Logn_in()
                if status_login:
                    print(chalk.green(f'Welcome Back {status_login[0]["UserName"]}'))
                    self.information = status_login
                    self.game.StarGame(active=True,data = self.information)
                    self.information = None
                    continue
                print(chalk.red("Please check your username or password"))



            elif choice["choice"] == "Guest (Try Game!)":

                self.game.StarGame()
            else:
                self.game.WaitAWhiel("Terminate the game active")
                return






    def ArchiveUpdate(self,winner,loser,draw=False):
        now = datetime.now()
        if draw:
            self.information[0]["GameArchive"][now.strftime("%d/%m/%Y %H:%M:%S")] = f"A tie between  {winner} and {loser}"
        else:

            self.information[0]["GameArchive"][now.strftime("%d/%m/%Y %H:%M:%S")] = f"the winner was {winner} and the loser {loser}"

        db.collection("Players").document(self.information[0]['UserName']).set(self.information[0])


class SignUp:
    def Sign_up(self):


        info = [
            Text('FullName', message="Please enter full name",validate=lambda _, x: match(r'^[a-zA-Z]+$', x)),
            Text('UserName', message="Please enter username",validate=lambda _, x: match(r'^[a-zA-Z0-9]+$', x)),
            Text('Email', message="Please enter your email",validate=lambda _, x: match(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', x),default="example@gmail.com"),
            Text('Password', message="Please enter password",validate=lambda _, x: match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$', x),default=self.RandomPassword())
                    ]
        info = prompt(info)
        self.UploadData(info)
        print(f"{chalk.green("Registered successfuly you can now")} {chalk.yellow("login")}!")


    def SendMail(self):
        pass
    def UploadData(self,data):
        db.collection("Players").document(data['UserName']).set(data)
        db.collection("Players").document(data['UserName']).set({"GameArchive":{},"BoardArchive":{}},merge=True)

    def RandomPassword(self)-> str:
        return "".join([choice(ascii_letters + digits) for _ in range(10)])




class LognIn:
    def Logn_in(self):


                info = [
                Text('UserName', message="Please enter username"),
                Text('Password', message="Please enter password"),

                            ]

                info = prompt(info)
                status_search =self.SearchPlayer(info=info['UserName'],password=info['Password'])

                if status_search:
                    return status_search
                return False


    def SearchPlayer(self,info:str,password:str):
        collection = db.collection("Players")
        status = collection.where(filter=FieldFilter("UserName", "==", info)).get()
        convert_data = [data.to_dict()  for data in status ]
        if convert_data:
            if convert_data[0]["Password"] == password:
                return convert_data
        return False
