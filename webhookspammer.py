
import requests
from os import system


x = 0

WEBHOOK_URL = str(input(" webhook you wanna spam : "))
WEBHOOK_USERNAME = str(input("\nname of the webhook : "))
WEBHOOK_AVATAR = str(input("\navatar of webhook : "))
WEBHOOK_CONTENT = str(input("\nwhat you want to say : "))
SPAM = int(input("\nEnter the number of messages : "))

while x < SPAM:
    try:
        payload = {"content":WEBHOOK_CONTENT,"username":WEBHOOK_USERNAME,"avatar_url":WEBHOOK_AVATAR}
        r = requests.post(WEBHOOK_URL,data=payload)
        x +=1
        print("[+] It is Done my good sir")
    except:
        print("[-] Request not sent")
        pass
print("\n[+] It is Done my good sir")
