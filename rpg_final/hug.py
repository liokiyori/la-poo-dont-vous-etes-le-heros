from hugchat import hugchat
from hugchat.login import Login



def repondre():

    sign = Login(email='garamas197@gmail.com', passwd='Isen0000!')
    cookies = sign.login()

    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())

    return chatbot.chat("Generate a very short description, 3 ligns maximum, of a fantasy dungeon")