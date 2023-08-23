import os
import time
import pyfiglet

def send_custom_command(command, repetitions):
    for i in range(2, repetitions + 1):
        command_with_repetition = f"{command} now-{i}"
        os.system(command_with_repetition)
        print("Will start downloading the next day...")
        for count in range(3, 0, -1):
            print(count)
            time.sleep(1)
        print("STARTING THE DOWNLOAD!")
        print(" ")
        print(" ")
        time.sleep(2)

def print_banner(message):
    banner = pyfiglet.figlet_format(message, font="slant")
    print(banner)

def wait_for_user_input():
    input("Press Enter to end the program...")

if __name__ == "__main__":
    print("Hi ! I can help you re-download data from the last few days.")
  # Replace "your-generic-command-here" to your command!
    user_command = r"your-generic-command-here"  
    try:
        repetitions = int(input("Enter how many last days I should download data (minimum value (days) : 2 ) : "))
        if repetitions < 2:
            print("Error: The number of repetitions must be greater than or equal to 2.")
        else:
            send_custom_command(user_command, repetitions)
            print_banner("DONE!!!")
            print("ALL DATA HAS BEEN DOWNLOADED")
            print(" ")
            print(" ")
            wait_for_user_input()
    except ValueError:
        print("Error: Number of repeats must be an integer greater than or equal to 2.")
