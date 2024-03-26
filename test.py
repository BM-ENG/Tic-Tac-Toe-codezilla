        # help =  1
        # counter = 1
        # range_help = 3
        # for i in range(1,5):
        #     for _ in range(range_help):
        #         if (self.board.zone[str(help)]) == (self.board.zone[(str(help:= help+i))]) and (self.board.zone[(str(help))]) == (self.board.zone[(str(help:= help+i))]):
        #             return True
        #         help += counter
        #     help =  1
        #     counter += 1
        #     if i == 1 or i == 3:
        #         range_help = 1
        #         if i == 1:
        #             help = 3
        #         continue
        #     range_help = 3
# import requests
# def send_simple_message():
# 	return requests.post(
# 		"https://api.mailgun.net/v3/sandbox83af22e296c948fc8743528de2e45686.mailgun.org/messages",
# 		auth=("api", "9f441b5c8cf6b496396d3b8b06b450da-309b0ef4-e8ad8661"),
# 		data={"from": "m.bloul.inf@lagh-univ.dz",
# 			"to": "m.bloul.inf@lagh-univ.dz",
# 			"subject": "Hello Github Student",
# 			"template": "password",
# 			"html":"hey"})
#         # Send an email using your active template with the above snippet
#         # You can see a record of this email in your logs: https://app.mailgun.com/app/logs.
#         #


# import requests

# def send_email():
#     # Mailgun API parameters
#     api_key = '9f441b5c8cf6b496396d3b8b06b450da-309b0ef4-e8ad8661'

#     domain = 'sandbox83af22e296c948fc8743528de2e45686.mailgun.org'
#     sender = 'm.bloul.inf@lagh-univ.dz'
#     recipient = 'bloulmohamed2002@gmail.com'

#     # Email subject
#     subject = 'Your Subject Here'

#     # Email body (HTML content)
#     html_content = """
#     <html>
#     <head>
#         <title>Your Title Here</title>
#     </head>
#     <body>
#         <h1>Hello,</h1>
#         <p>This is a test email sent using Mailgun and Python.</p>
#         <p>You can edit this HTML content as per your requirements.</p>
#     </body>
#     </html>
#     """

#     # Mailgun API endpoint
#     mailgun_url = f"https://api.mailgun.net/v3/{domain}/messages"

#     # Mailgun request parameters
#     mailgun_params = {
#         'from': sender,
#         'to': recipient,
#         'subject': subject,
#         'html': html_content
#     }

#     # Mailgun API request headers
#     mailgun_headers = {
#         'Authorization': f'Basic {api_key}'
#     }

#     # Send email using Mailgun API
#     response = requests.post(mailgun_url, auth=('api', api_key), data=mailgun_params)

#     # Check if the request was successful
#     if response.status_code == 200:
#         print("Email sent successfully.")
#     else:
#         print("Failed to send email. Error:", response.text)

# # Call the function to send the email
# send_email()
# import the time module
# import firebase_admin
# from firebase_admin import credentials,firestore
# from google.cloud.firestore_v1 import collection
# from google.cloud.firestore_v1.base_query import FieldFilter
# cred = credentials.Certificate("/Users/HikoDz/Desktop/Tic-Tac-Toe-codezilla/backend/info_token_db.json")
# firebase_admin.initialize_app(cred,{'databaseURL':'https://tic-tac-toe-codezilla-default-rtdb.firebaseio.com/'})
# db = firestore.client()
# data = {}
# collection = db.collection("Players").where(filter=FieldFilter("UserName", "==", "ali")).get()
# for doc in docs:
#     print(f"{doc.id} => {doc.to_dict()}")
# import inquirer
# from inquirer.themes import GreenPassion
# import inquirer
# q = [
#     inquirer.Text("name", message="Whats your name?", default="No one"),
#     inquirer.List("jon", message="Does Jon Snow know?", choices=["yes", "no"], default="no"),
#     inquirer.Checkbox(
#         "kill_list", message="Who you want to kill?", choices=["Cersei", "Littlefinger", "The Mountain"]
#     ),
# ]

# inquirer.prompt(q, theme=GreenPassion())
devBio = {
  "name": "Ihechikara",
  "age": 500,
  "language": "Python"
}

tools = {
  "dev environment": "JupyterLab",
  "os": "Windows",
  "visualization": "Matplotlib"
}

merged_bio = { **devBio, **tools}

print(merged_bio)
# {'name': 'Ihechikara', 'age': 500, 'language': 'Python', 'dev environment': 'JupyterLab', 'os': 'Windows', 'visualization': 'Matplotlib'}
