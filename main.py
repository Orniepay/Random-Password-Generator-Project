import string 
import random 

print("")
print("Random Password Generator: ")
print("")

characters = list(string.ascii_letters + string.digits + "!@#$%&")

def generate_password():
    """
    Generates and prints a random password.

    This function prompts the user for the desired length of the password,
    then generates a random password of that length. The password is composed
    of a mix of ASCII letters (both uppercase and lowercase), digits, and 
    special characters '!@#$%&'. The characters are randomly shuffled before
    selection to enhance randomness.

    Parameters:
    None

    Returns:
    None: The function prints the generated password and does not return a value.
    """
    
    password_length = int(input("Please enter the desired length for your password: "))
    random.shuffle(characters)
    password = []
    for x in range(password_length):
        password.append(random.choice(characters))
    random.shuffle(password)
    password = "".join(password)
    print("")
    print("Random Password: " + password)

option = input("Do you want to generate a password? (Yes/No): ")

if option == "Yes":
    generate_password()
    print("")
elif option.lower() == "No":
    print("Program Ended")
    print("")
    quit()
else:
    print("Invalid command. Please try again!")
    print("")
    quit()