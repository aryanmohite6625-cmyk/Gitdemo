kyc_document={}
def check_balance():
    print(f"Your account balance is: {balance}")
    print("=================================")

def deposit(amount):
    global balance
    if amount>=0:
       balance += amount
    else :
       print("Cannot deposit negative amount !!")
       print("=================================")

def withdraw(amount):
    global balance
    if amount<=0:
        print("Cannot withdraw amount!!!")
        print("=================================")
    elif amount > balance :
        print("Cannot withdraw amount , insufficient balance!")
        print("=================================")
    else:
        balance -= amount
def update_kyc_document(docs):
    global kyc_document
    kyc_document.update(docs)

def check_kyc():
    if len(kyc_document) == 0:
        print("KYC NOT DONE!!")
    else:

        for docs in kyc_document:
            print(f"{docs}:{kyc_document[docs]}")

balance = 0.0
if __name__ == "__main__":
    print("=================================")
    print("Welcome to our XYZ Bank!!!")
    print("=================================")

    while True:
         print("=================================")
         print("1. Check Balance")
         print("2. Deposit")
         print("3. Withdraw")
         print("4. check kyc document")
         print("5. update kyc document")
         print("6. Exit")
         choice=input("Enter your choice(1-6): ")
         print("=================================")

         if choice == "1":
            check_balance()
         elif choice == "2":
            amt=float(input("Enter amount to deposit: "))
            deposit(amt)
            print(f"Amount {amt} Successfully deposited.")
         elif choice == "3":
            amt2=float(input("Enter amount to withdraw: "))
            withdraw(amt2)
            print(f"Amount {amt2} Successfully withdrawn. ")
         elif choice == "4":
            check_kyc()
         elif choice == "5":
             kyc_docs={}
             n_document =int(input("Enter the no of documents you want to update: "))
             for i in range(n_document):
                 key = input("Enter the document type: ")
                 value = input("The document number: ")
                 kyc_docs[key]=value
             update_kyc_document(kyc_docs)
             print(f"KYC updated!!")
         elif choice == "6":
            print("Quiting")
            break
         else :
            print("Invalid choice")
    print("===================================")
    print("Thank you for using our XYZ Bank!!!")