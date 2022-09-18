class Question:
    def __init__(self, questionText, answer, multipleChoiceOptions=None, alternateAnswers=None):
        self.questionText = questionText
        self.answer = answer
        self.multipleChoiceOptions = multipleChoiceOptions
        self.alternateAnswers = alternateAnswers
 
    def __repr__(self):
        return '{'+ self.questionText +', '+ self.answer +', '+ str(self.multipleChoiceOptions) +', '+ str(self.alternateAnswers) +'}'

for question in quizQuestions:
    print(f"{question.questionText}?")
    userInput = input()
    if (userInput.lower() == question.answer.lower()):
        print("That is correct!")
    elif (question.alternateAnswers != None and userInput.lower() in question.alternateAnswers):
        print("That is correct!")
    else:
        print(f"Sorry, the correct answer is {question.answer}.")


quizQuestions = [
    #...
    Question("Question 5. What hemisphere is Japan located in", "Northern Hemisphere", [], ["north", "northern"]),
]