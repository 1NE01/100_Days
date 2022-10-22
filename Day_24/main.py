#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
with open("./Input/Letters/starting_letter.txt",mode="r") as data:
    Letter=data.read()
with open("./Input/Names/invited_names.txt",mode="r") as data1:
    Names=data1.read()
    Names_list=Names.split("\n")
for nama in Names_list:
    p_letter=Letter.replace("[name]",nama)
    with open(f"./Output/ReadyToSend/Letter_for_{nama}.txt",mode="w") as confident:
        confident.write(f"{p_letter}")



