# Program:      Email Validator 
# Programmer:   Douglas Rosenfield
# Date:         03/12/2019
# Purpose:      To validate emails, checking for syntax
# NOTES - This script is WIP. It is currrently not in a working state!!

validCharacters = () #enter all valid characters here!
emailList = ["abc@xyz.com",
             "abc@@xyz.com",
             "@xyz.com",
             "abc.xyz.com",
             "abc@x.yz",
             "abc@xyz.c",
             "a@b.c",
             "abc@xyz..com",
             "abc.@xyz.com",
             "abc@.xyz.com",
             "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa@aaaaaa.aaaaa",
             "' or 1=1 '==",# Wow that's a hard one
             "abc@xyz.$%",
             "abc@xyz.()",
             "abc'@xyz.com",
             "aaaaa@aaaaa",
             "abc @ xyz.com",
             ".abc@xyz.com",
             "abc@xyz.c"]


def emailChecker(emailSet):
    for c in range(len(emailSet)):
        if check01_length(emailSet[c]) == True:                     # email length validation
            if check02_atsign(emailSet[c]) == True:                 # email @ validation
                if check03_dot(emailSet[c]) == True:
                    print ("VALID -- {}".format(emailSet[c]))
                else:
                    print ("VOID -- {}".format(emailSet[c]))
        else:
            print ("VOID -- {}".format(emailSet[c]))

# Checks that length is valid
def check01_length(email):
    if 7 <= len(email) <= 40:
        return True

# Checkss that @ count and placement is valid
def check02_atsign(email):
    atCounter = 0
    proceed = False
    positionCheck = False
    for c in range(len(email)):
        if email[c] == "@":
            atCounter += 1
            if 1 < c < len(email)-2:
                positionCheck = True
    if atCounter == 1:
        if positionCheck == True:
            return True


def check03_dot(email):
    validData = True
    for c in range(len(email)):
        dotCounter = 0
        if email[c] == ".":
            if c == 0 or c <= len(email) - 2:
                validData = False
            if email[c+1] == ".":
                validData == False
        if validData == True:
            return True
        else:
            return False



emailChecker(emailList)
