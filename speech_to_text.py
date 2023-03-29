import os
from offline_method import offline_file_option
from online_google_method import online_file_option, online_speech_to_text_option

print("This App support WAV file as of now..\n")
color="\033[1;32m"

def options():
    while True:
        print("----Convert Audio File----\n")
        print("Please select an option:\n")
        print(f"{color}1. Convert Audio File Online")
        print(f"{color}2. Convert Audio File Offline")
        print(f"{color}3. Real Time Online\n")
    
        option = input("\033[0mEnter your choice (1 - 2 - 3): ")

        if option == "1":
            print("You selected Option 1")
            # perform action for option 1
            online_file_option()
            break
        elif option == "2":
            print("You selected Option 2")
            # perform action for option 2
            offline_file_option()
            break
        elif option == "3":
            print("You selected Option 3")
            # perform action for option 3
            online_speech_to_text_option()
            break
        else:
            print("Invalid option, please try again.")

# Ask user for diff options
# options()
