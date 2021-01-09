from os import system
from getpass import getuser
from datetime import datetime
from time import gmtime, strftime


# Your sudo_password is required to execute sudo-level commands, such as apt update
sudo_password = ''

print(f"Hello {getuser()}! Executing the house keep commands. It might take a while!\n\n\n")

system(f'echo {sudo_password} | sudo -S apt update -y && sudo apt upgrade -y && sudo apt autoremove -y && sudo apt clean')

# Day name ( 'Monday', 'Wednesday', ... )
day_name =  datetime.today().strftime('%A')

# Date string is just the sum of information about the current date and time
date_string  = f"Today is {day_name}, {strftime('%Y-%m-%d', gmtime())} and right now are {strftime('%H:%M', gmtime())}"

print(f"\n\n\n The script has finished updating your System. Everything is up to date. {date_string}. Have a fantastic day!")

'''
    * Uncomment this line in case you want to specify a custom trash folder
    
    * Note:
        * The sudo apt clean already does that automatically, but if you want to specify something else, uncomment the line.
'''
# system(f'echo {sudo_password} | sudo -S rm -rf /home/{getuser}/.local/share/Trash')
