# Program:      Email Validator 
# Programmer:   Douglas Rosenfield 
# Date:         03/15/2019
# Purpose:      To validate emails, checking for syntax

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
             "' or 1=1 '==",
             "abc@xyz.$%",
             "abc@xyz.()",
             "abc'@xyz.com",
             "aaaaa@aaaaa",
             "abc @ xyz.com",
             ".abc@xyz.com",
             "abc@xyz.c"]

doNotInclude = """ " ' ! # $ % ^ & * ( ) _ - + = [ ] { } : ; ` ~ | \ / ? > < """.split()
doNotInclude.append(" ")
errorList = ["----- errors -----"]

# Main program. Runs email through each check function and returns false if any fail.
def emailChecker(emailSet):

    global errorList 
    for email in emailSet:
            
        validEmail = True

# Each check called here. Errors are not defined here, they are defined within each function.

        if not check01_length(email):
            validEmail = False

        if not check02_atsign(email):
            validEmail = False

        if not check03_dot(email):
            validEmail = False

        if not check04_characters(email):
            validEmail = False
        
        if validEmail:
            print("VALID - {}".format(email))
            print()
        else:
            print("INVALID - {}".format(email))
            print(*errorList, sep = "\n")
            print("------------------")
            print()
    
        errorList = ["----- errors -----"]

# -------------------------------------------------- 
# define functions below

# Checks that length is valid
def check01_length(email):
    global errorList

    if 7 <= len(email) <= 40:
        return True
    else:
        errorList.append("error11: invalid length")

# Checks that @ count and placement is valid
def check02_atsign(email): 
    global errorList

    # makes sure at least one @ in email
    if "@" not in email:
        errorList.append("error21: @ sign missing")
        return False

    atIndex = 0         # keeps track of index of @
    atCounter = 0       # keeps track of how many @ in email

    # accumulates @ count
    for index in range(len(email)):
        if email[index] == "@":
            atIndex = index
            atCounter += 1
    
    # makes sure only 1 @
    if atCounter > 1:
        errorList.append("error22: multiple @ signs")
        return False

    # checks position of @
    if 1 < atIndex < len(email) - 5:
        return True
    else:
        errorList.append("error23: invalid @ sign placement")
        return False

    # Some notes about check02 vs check03:
    # check02 uses a variable to store index of @, but check03 checks position while looping.
    # I feel both of these are valid methods of checking position (although check03 may be cleaner)
    # check02 was easier to wrap my head around at the time.
    # If adding true polish, I would rewrite check02 to get rid of atIndex in favor of check03 style validation.
    # This would also allow for error22 and error23 to occur simultaneously since would remove returns

# checks each character. If ".", check for valid condition and check for @ signs as neighbors. Fails if either are true.
def check03_dot(email):
    global errorList
    validData = True 
    
    # make sure at least one . is included in email
    if "." not in email:
        errorList.append("error31: missing dot")
        validData = False
   
    # loop through chars in email, check neighboring characters of each . for invalid characters
    for index in range(len(email)):
        if email[index] == ".":

            if email[index+1] == ".":
                validData = False
                errorList.append("error32: sequential dots")

            if index == 0 or index >= len(email) - 2:
                validData = False
                errorList.append("error33: dots in forbidden areas")

            if email[index+1] == "@" or email[index-1] == "@":
                validData = False
                errorList.append("error34: dot neighboring @ sign")

    return validData


# checks each character in email. If character is included in doNotInclude list, fail and give error.
def check04_characters(email):
    global errorList
    badChars = []           # list of all offending characters in email
    validData = True
    
    # Loop through each char in email. If char is in doNotInclude, validData = False,
    # and append offending characters to badChars.
    for index in range(len(email)):
        if email[index] in doNotInclude:
            if not email[index] in badChars:
                if email[index] == " " and "<SPACE>" not in badChars:
                    badChars.append("<SPACE>")
                else:
                    badChars.append(email[index])
            validData = False

    # If email fails check, send error code with all offending characters.
    if validData == False:
        badCharsString = "".join(badChars)
        errorList.append("error41: forbidden character(s) {}".format(badCharsString))

    return validData

emailChecker(emailList)
