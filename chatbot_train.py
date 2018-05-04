from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('Bot')
bot.set_trainer(ListTrainer)

for files in os.listdir('E:\anwesha\Sem\explore\chatterbot-corpus-master\chatterbot_corpus\data\english'):
         data = open('E:\anwesha\Sem\explore\chatterbot-corpus-master\chatterbot_corpus\data\english'+files,'r').readLines()
         bot.train(data)

while True:
      message = input('You:')
  if message.strip() == 'Bye' :
      reply = bot.get_response(message)
      print('Chatbot:',reply)
  if message.strip() == 'Bye' :
       print('Chatbot : Bye')
       break
