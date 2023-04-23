import random
import string

def get_length():

        """ This functions checks the length desired by the user"""

        global pwd_length

        while True:

                try:
                        pwd_length = int(input("How many characters your password should have? Type here:   "))
                        

                        if pwd_length <= 0:
                                raise("You must only use positive integers. Try again")


                        break
                
                        
                except:
                        print("Please try again. You must only use positive integers")
       

def get_digits():

        """ This functions checks if the user wants his password to contain digits"""

        global digits_validation               

        while True:

                try:
                        digits_validation = str(input("Would you like to have digits?Type here:  "))
                        
                        

                        if digits_validation.lower() not in ["yes", "no"]:
                                raise("You must only use positive integers. Try again")


                        break
                
                        
                except:
                        print("Please try again. You must only use yes or no. Be careful not to have Caps Lock active")
        
        
def get_symbols():

        """ This functions checks if the user wants his password to contain symbols"""

        global symbols_validation

        while True:

                try:
                        
                        
                        symbols_validation = str(input("Would you like to have symbols? Type here:   "))

                        if symbols_validation.lower() not in ["yes", "no"]:
                                raise("You must only use positive integers. Try again")


                        break
                
                        
                except:
                        print("Please try again. You must only use yes or no. Be careful not to have Caps Lock active")





def generate_password():
        filtering = set()
        
        iterations = pwd_length

        while True:
                if digits_validation == "yes" and symbols_validation == "no":
                        num = random.randint(0,9)
                        filtering.add(str((num)))
                elif digits_validation == "no" and symbols_validation == "yes":
                        char = random.choice(string.punctuation)
                        filtering.add(char)
                elif digits_validation == "yes" and symbols_validation == "yes":
                        choice = random.choice([0,1,2])
                        if choice == 0:
                                num = random.randint(0,9)
                                filtering.add(str((num)))
                        elif choice == 1:
                                char = random.choice(string.punctuation)
                                filtering.add(char)
                        else:
                                letter = random.choice(string.ascii_letters)
                                filtering.add(letter)

                elif digits_validation == "no" and symbols_validation == "no":
                        print("Cannot generate a password without any choice")
                        break

                if len(filtering) == iterations:
                        break
        real_password = ''.join(filtering)
        return real_password
        
        
get_length()
get_digits()
get_symbols()
print(f"Your password is {generate_password()}")