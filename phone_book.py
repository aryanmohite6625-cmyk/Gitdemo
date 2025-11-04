class Contact:
    phone_directory = []

    def __init__(self,name,phone_no):
        Contact.phone_directory.append(self)
        self.name = name
        self.phone = phone_no



    def show_contacts(self):
        return f"Name: {self.name}, Contact number: {self.phone}"

    @classmethod
    def show_all_contacts(cls):
        if len(cls.phone_directory) == 0:
            print("No phone numbers found!!")
        else:
            print("All contacts from the directory!! ==>")
            for contact in cls.phone_directory:
                print(contact.show_contacts())


    @classmethod
    def search_contact(cls, search_name):
        for contact in cls.phone_directory:
            if  contact.name.lower() == search_name.lower():
                return contact.phone
            return f"Phone number not found: {search_name}"

    @staticmethod
    def validate_phone_number(number):
        if len(number) >= 8 and number.isdigit():
            return True
        else:
            return False

n_contacts=int(input("How many phone numbers would you like?: "))
for i in range(n_contacts):
    name=input("Enter the name of the person: ")
    phone_number=input("Enter the phone number: ")
    if Contact.validate_phone_number(phone_number):
         Contact(name, phone_number )
    else:
        print(f"Invalid phone number for {name} the phone number must be 8 digits")

Contact.show_all_contacts()
'''
c1=Contact("Ryan",6789543267)
c2=Contact("Jon",6523893674)
c3=Contact("Bryan",7777777777)
'''
#print(Contact.phone_directory)
#print(c1.show_contacts())
#print(c2.show_contacts())
#Contact.show_all_contacts()
#c1.show_all_contacts()
#print(Contact.search_contact("Ryan"))
#print(Contact.search_contact("Mark"))