from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

#creando instancia del bot y agragando funcionalidades desde una base de datos
chatbot = ChatBot('Mololo Bot', storage_adapter='chatterbot.storage.SQLStorageAdapter', logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch'
        ],
        database_uri='sqlite:///database.db')

#entregando el bit
trainer = ChatterBotCorpusTrainer(chatbot)
#indicando en que lenguaje se va a comunicar y cuales corvesaciones va a cargar
trainer.train("chatterbot.corpus.spanish")

while True:
    user = input("User: ")
    response = chatbot.get_response(user)
    print("Mololo Bot: " + str(response))

