class Message:
    """this class is for app chat"""
    def __init__(self, sender_name, recever_name, message, date):
        self.sender_name = sender_name
        self.recever_name = recever_name
        self.message = message
        self.date = date

sender_name = input("What is you name: ").capitalize()
recever_name = input("Please Enter the name of the recever: ").capitalize()
message = input("please enter your message: ")
date = input("please enter your current date: ")
user = Message(sender_name, recever_name, message, date)
print(f"hello my name is {user.sender_name} i write for you this message {user.message}, my friend {user.recever_name} at {user.date}")



