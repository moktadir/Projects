#Moktadir Shourav fa9444 CSC 1100 Sec 002/003
#Project 1 Completed 04/06/2013
#Work Completed: 100%

def encryption(): #Encryption function
    import string #Import string module
    cypher = {} #Create blank encryption dictionary
    line_list = [] #Empty list for acquiring iterated elements
    new_line = [] #Same as above
    i = -1 
    for letter in string.ascii_lowercase: #Encryption key for lowercase letters
        cypher.update({letter:string.ascii_uppercase[i]}) #Updated dictionary
        i -= 1
    i = -1
    for letter in string.ascii_uppercase: #Encryption for uppercase
        cypher.update({letter:string.ascii_lowercase[i]}) #Updated
        i -= 1
    i = -1
    for character in string.punctuation: #For punctuation
        cypher.update({character:string.punctuation[i]}) #Update
        i -= 1
    i = -1
    for digit in string.digits: #For digits
        cypher.update({digit:string.digits[i]}) #Update
        i -= 1
    i = -1
    for command in string.whitespace: #For command characters
        cypher.update({command:string.whitespace[i]})
        i -= 1
    i = 0
    while True: #Loop that requests a filename/location until a file is found.
        try:
            prompt = input("Enter name of file to encrypt: ")
            source = open(prompt,"r")
            break
        except:
            OSError
    encrypted_prompt = input("Enter name of encrypted file (remember '.txt'): ")
    encrypted = open(encrypted_prompt,"w") #Specify output file of encrypted code
    for line in source:
        line_list = list(line) #Splits file into lines, then splits the line
        for character in line_list: #Iterates for each character in line
            line_list[i] = cypher[character] #Replaces character with code.
            i += 1
        new_line = "".join(line_list) #Reconnects line.
        print(new_line, file = encrypted) #Writes line into output file.
        i = 0
    source.close() #File closure
    encrypted.close() #Closure.
    return


def decryption(): #Decryption function.
    import string
    decypher = {} #Blank decryption dictionary
    line_list = []
    new_line = []
    i = -1
    for letter in string.ascii_lowercase: #From here down is the decryption key.
        decypher.update({string.ascii_uppercase[i]:letter}) #Updates
        i -= 1
    i = -1
    for letter in string.ascii_uppercase:
        decypher.update({string.ascii_lowercase[i]:letter})
        i -= 1
    i = -1
    for character in string.punctuation:
        decypher.update({string.punctuation[i]:character})
        i -= 1
    i = -1
    for digit in string.digits:
        decypher.update({string.digits[i]:digit})
        i -= 1
    i = -1
    for command in string.whitespace:
        decypher.update({string.whitespace[i]:command})
        i -=1
    i = 0
    while True: #Loop to locate a valid file. Make sure it's the encoded one!
        try:
            prompt = input("Enter name of file to decrypt: ")
            source = open(prompt,"r")
            break
        except:
            OSError
    for line in source: #Same nested loops as encryption func., different dict.
        line_list = list(line)
        for character in line_list:
            line_list[i] = decypher[character]
            i += 1
        new_line = "".join(line_list)
        print(new_line) #Instead of written, the decoded message is displayed.
        i = 0
    source.close() #Closure
    return
