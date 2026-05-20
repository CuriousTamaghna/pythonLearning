#May 20 Password Generator Using modules 11:56

import random 
#random library for random behaviour , random_number , random_chrachter, random_choice
import string
#string contains letters , digits , symbols

def password_generate(length):
    all_characters = (string.ascii_letters+string.digits+string.punctuation)


    password=""

    for i in range(length):
        password +=random.choice(all_characters)

    return password

while True:
    print("Create password automatically!")
    length = int(input("Please enter password length: "))

    result = password_generate(length)

    print(f"The password is : {result}")
    break

