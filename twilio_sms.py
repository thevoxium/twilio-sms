from twilio.rest import Client

ssid = input("enter your Account SID: ")
token=input("enter your Auth Token: ")
client = Client(ssid, token)

def sent(you_num, rec_num):
    client.messages.create(to=rec_num, from_=you_num, body="this is anshul sharma")

you_num=input("enter your twilio number: ")
rec_num=input("enter the revceiver's number: ")

pre = input("do you have premium account(y/n): ")
if pre=="y":
    sent(you_num, rec_num)
else :
    verify=input("is the rec_num verified(y/n): ")
    if verify=="y":
        sent(you_num, rec_num)
    else:
        print("trial accounts can't send message to unverified numbers. Verify the number first!!")
