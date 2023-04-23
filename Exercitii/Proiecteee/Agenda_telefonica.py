
class Contact:
    
    def __init__(self) -> None:
        
        self.details = {}


    

   
    
    def add_contact(self):

        """This method adds a new contact"""

        contact_list = self.details

        
        

        while True:
            
                choose_name = str(input("Insert a name: "))
                #choose_number = int(input("Insert the phone number: "))

                if choose_name in contact_list:
                     print("This username already exists, please type a new name")
                     continue
                
                if not choose_name.isalpha():
                    print("Only text is accepted, no numbers or symbols allowed. Please try again.")
                
                

                else:
                    break

            

        while True:
            
                choose_number = str(input("Insert the phone number: "))
                
                if not choose_number.isdigit():
                    print("Only digits are allowed here. Try again.")

                else:
                    break

            
            
        
        contact_list[choose_name] = choose_number

        while True:
            self.additional_contact = str(input("Would you like to add another contact? "))

            if self.additional_contact not in ["yes", "no"]:
                print("Please type yes or no")

            if self.additional_contact == "yes":
                self.add_contact()
                break

            if self.additional_contact == "no":
                break
    
        return contact_list
    

    
                
    def search_contact(self):
        
        """ This method allows the user to find contacts based on strings or numbers"""
        

        while True:
            user_prompt = str(input("Search: "))
            
            if not user_prompt.isalpha() and not user_prompt.isdigit():
                print("Please use only alphabetical characters, no numbers or symbols allowed.")

            else:
                break
        
        if user_prompt.isalpha():

            for name in sorted(self.details):
                if user_prompt in name and not user_prompt.isdigit():
                    print(name)
            
                else:
                    print("This user does not exist.")
                    break

        if user_prompt.isdigit():

            reversed_list = {numbers: names for names, numbers in self.details.items()}

            if user_prompt in reversed_list:
                print("Nume: " + reversed_list[user_prompt] + "\n" + "Telefon: " + user_prompt)

            else:
                print("There is no contact registered with this phone number.")

        


    def delete_contact(self):

        while True:
            name_selection = str(input("Type the user that you want to delete: "))

            if not name_selection.isalpha():

                print("Only alphabetical characters allowed here.")

            else:
                break

        if name_selection in self.details:
            self.details.__delitem__(name_selection)

        else:
            print("The user cannot be found in the contact list")

            self.run_menu()

    
    
    def run_menu(self):
        """ This method runs the main menu"""

        

        print("1.Add contact(press 1)\n2.Search contact(press 2)\n3.Delete contact(press 3)\n4.Return to main menu(press 0)")
        while True:
            try:
                self.user_choice = int(input("Choose an action: "))
                if self.user_choice < 0 or self.user_choice > 3:
                    print("There is no available option for the selected number, please use only 1, 2 or 3.")
                    continue
                else:
                    break

            except ValueError:
                print("Please use only positive integers.")

        while True:
            if self.user_choice == 1:
                self.add_contact()
                if self.additional_contact == "no":
                    self.run_menu()

            if self.user_choice == 2:
                
                self.search_contact()
                self.run_menu()
            
            if self.user_choice == 3:
                self.delete_contact()
                break

            if self.user_choice == 0:
                self.run_menu()
            
        
        
    

my_obj = Contact()

my_obj.run_menu()


