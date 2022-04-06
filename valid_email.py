import re

def valid(email):
    
    temp = re.search(".+[@][A-Z|a-z]+\.[(com)|(co.in)]", email)
    try:
        email = temp.string
        print(email)
    except:
        mail = input("Enter the valid email address: ")
        email = valid(mail)
    return email
mail = input("Please enter your email address to send the scores: ")
email = valid(mail)

