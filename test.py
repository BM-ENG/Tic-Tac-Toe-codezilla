import inquirer
questions = [
  inquirer.Checkbox('interests',
                    message="What are you interested in?",
                    choices=['Computers', 'Books', 'Science', 'Nature', 'Fantasy', 'History'],
                    ),
]
answers = inquirer.prompt(questions)
print(answers)
