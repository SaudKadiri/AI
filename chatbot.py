# This short python program will train and make a chatbot!
# Installations:
#       pip install chatterbot 
#   * To train the chatbot
#       pip install chatterbot_corpus
#
# Reference: https://www.edureka.co/blog/how-to-make-a-chatbot-in-python/

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
 
# Create an instance of the Chatbox class
chatbot = ChatBot('My Chatbot')
trainer = ListTrainer(chatbot)
# training the chatbot with responses to be given
trainer.train(["You will be singled out for promotion in your work.",
               "Your society will be sought by people of taste and refinement.",
               "Today is the first day of the rest of the mess."])
 
# getting a response from the chatbot
response = chatbot.get_response("Tell me my fortune")

# print the response
print(response)
