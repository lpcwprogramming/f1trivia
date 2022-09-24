import random

class Question:
    def __init__(self, questionText, answer, alternateAnswers=None):
        self.questionText = questionText
        self.answer = answer
        self.alternateAnswers = alternateAnswers
 
    def __repr__(self):
        return '{'+ self.questionText +', '+ self.answer +', '+ str(self.alternateAnswers) +'}'


quizQuestions = [
    #...
    Question("Who won the championship in 2000", "Michael Schumacher"),
    Question("Who won the championship in 2001", "Michael Schumacher"),
    Question("Who won the championship in 2002", "Michael Schumacher"),
    Question("Who won the championship in 2003", "Michael Schumacher"),
    Question("Who won the championship in 2004", "Michael Schumacher"),
    Question("Who won the championship in 2005", "Fernando Alonso"),
    Question("Who won the championship in 2006", "Fernando Alonso"),
    Question("Who won the championship in 2007", "Kimi Räikkönen"),
    Question("Who won the championship in 2008", "Lewis Hamilton"),
    Question("Who won the championship in 2009", "Jenson Button"),
    Question("Who won the championship in 2010", "Sebastian Vettel"),
    Question("Who won the championship in 2011", "Sebastian Vettel"),
    Question("Who won the championship in 2012", "Sebastian Vettel"),
    Question("Who won the championship in 2013", "Sebastian Vettel"),
    Question("Who won the championship in 2014", "Lewis Hamilton"),
    Question("Who won the championship in 2015", "Lewis Hamilton"),
    Question("Who won the championship in 2016", "Nico Rosberg"),
    Question("Who won the championship in 2017", "Lewis Hamilton"),
    Question("Who won the championship in 2018", "Lewis Hamilton"),
    Question("Who won the championship in 2019", "Lewis Hamilton"),
    Question("Who won the championship in 2020", "Lewis Hamilton"),
    Question("Who won the championship in 2021", "Max Verstappen"),
]

user_play = "y"

while user_play == "y":

    for question in quizQuestions:
        random.shuffle(quizQuestions)
        print(f"{question.questionText}?")
        userInput = input()

        if (userInput.lower() == question.answer.lower()):
            print("That is correct!")

        else:
            print(f"Sorry, the correct answer is {question.answer}.")
    
            user_play = input("Answer another question: (y)es or (n)o? ")