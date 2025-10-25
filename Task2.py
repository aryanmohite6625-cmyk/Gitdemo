text_write=input("Enter the text to be printed in the file: ")
with open("output.txt","w") as file:
    file.write(text_write +"\n")
    print("Data successfully written to output.txt\n")

text_append=input("Enter the text to be appended in the file: ")
with open("output.txt","a") as file:
    file.write(text_append +"\n")
    print("Data successfully appended to output.txt\n")
print("Final content of the file output.txt:")
with open("output.txt","r") as file:
    content=file.read()
    print(content)
