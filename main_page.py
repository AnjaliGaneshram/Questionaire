import json, testmail, re
options = ['A','B','C','D']
score = 0
i = 0
def valid1(email):
    temp = re.search("[A-Z|a-z|0-9]+[@][A-Z|a-z|0-9]+\.[(com)|(co.in)]", email)
    try:
        email = temp.string
    except:
        mail = input("Enter the valid email address: ")
        email = valid1(mail)
    return email
def valid(n):
    try:
        n = int(input("Enter only numbers: "))
    except:
        n = valid(n)
    return n
fd = open("sample1.json","r")
Question_dict = json.loads(fd.read())
fd.close()
name = input("Please enter your name: ")
try:
    no_quest = int(input("Enter the no of questions you would like to answer(minimum 5 questions out of 25): "))
except:
    no_quest = valid(no_quest)
    while no_quest not in range(5,26):
        try:
            no_quest = int(input("Enter the number of questions in the range of 5 to 25: "))
        except:
            no_quest = valid(no_quest)
for key, val in Question_dict.items():
    if i < no_quest:
        print(key,"\n")
        j = 0
        for key1,val1 in val.items():
            if j < 5:
                print(key1, val1)
                j=j+1
        answer = input("Enter your option(Either A or B or C or D): ")
        answer = answer.upper()
        while answer not in options:
            answer = input("Enter your option(Either A or B or C or D): ")
            answer = answer.upper()
        if answer == val["Correct_answer: "]:
            print("Correct Answer.")
            score = score + 1
        else:
            print("Wrong Answer. Correct Answer is option {}".format(val["Correct_answer: "]))
        i = i + 1
print(score)
mail = input("Please enter your email address to send the scores: ")
email = valid1(mail)
sub = "Quiz Result"
mess = "Hi {0}! Your score for the quiz is {1}. Thank you for taking the quiz.".format(name, score)
testmail.sending_mail(email,sub,mess)


            
        
