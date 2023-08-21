from compress import compress_file
from decompress import decompress_file
import decompress
import os


print("\t\tWelcome to File Compression & Decompression Application\n")


def main_function():

    check = True
    while check:
        choice = input(
            "Menu:\n1) Compress a file\n2) Decompress a file\n3) Exit Application\n Enter Your Choice= ").lower()
    # choice = input("Enter Your Choice = ").lower()
        if choice == "1" or choice == "compress":
            file_path = input(
                "Enter File Path (e.g# C:/Users/babrak/Desktop/Projects/raw.txt)= ")
            if os.path.exists(file_path):
                print("File Existed!")
                compress_file(file_path)
            else:
                print("File Not Existed !")

            check = False
            main_function()

        elif choice == "2" or choice == "decompress" or choice == "de compress":
            file_path = input(
                "Enter File Path (e.g# C:/Users/babrak/Desktop/Projects/raw.txt)= ")
            if os.path.exists(file_path):
                print("File Existed!")
                decompress_file(file_path)
            else:
                print("File Not Existed !")

            check = False
            main_function()

        elif choice == "3" or choice == "exit":
            print("Thanks For Using the Application !")
            return

        else:
            print("\nInvalid number or character! Select From Menu\n ")
            # main_function()


main_function()
