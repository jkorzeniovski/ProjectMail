# do korzystania z aplikacji potrzebne jest połączenie z API gmaila, oraz wygenerowanie tokenu
# autoryzacji OAuth2 połączonego z kontem maila nadającego
# https://developers.google.com/gmail/api/quickstart/python/

import ezgmail
# import argparse
#
# parser = argparse.ArgumentParser()
# # add the -s and --send flags
# parser.add_argument("-s", "--send", help="send data", action="store_true")
# # add the -r and --read flags
# parser.add_argument("-r", "--read", help="read data", action="store_true")
# args = parser.parse_args()
# # check if the -s or --send flag was passed
# if args.send:
#     print("Sending email...")
# # check if the -r or --read flag was passed
# if args.read:
#     print("Reading data...")

# pobranie nieodczytanych maili
unreadmails = ezgmail.unread(maxResults=100)
# ilosc nieodczytanych wiadomosci
liczbaUnread = len(unreadmails)

print(f"\033[91mUnread emails stack at 100 positions\033[0m")
print(f"\033[92mYou have {liczbaUnread} unread mails\033[0m")

print("1. Send email")
print("2. Read email")
print("3. what's my mail")

# wybor dzialania
choice = int(input("\033[92mwhat do you want to do?: \033[0m")) #\033[92m dla lepszej przejrzystości
# wyslanie maila
if choice == 1:
    dest = input("insert receiver's email: ") #odbiorca
    subj = input("what's the email subject: ") #tytuł/temat
    text = input("insert message to send: ") #treść maila
    attach = input("\033[92mDo you want to add an attachment? (max 1): [y/n]\033[0m").lower().strip() #lower i strip w przypadku użycia dużej litery i spacji przed bądź po
    if attach == "y":
        attachpath = input("Add a path to your attachment: ") # ścieżka do załącznika
        ezgmail.send(dest, subj, text, attachpath)
    elif attach == "n":
        ezgmail.send(dest, subj, text)
    else:
        print("Attachment is a yes or no question.") # przypadek podania innej wartości niż y lub n
# dodanie informacji kursywą
    print("\033[1;3m" + "Sending email..." + '\033[0m')
elif choice == 2:
# wyprintuj liste nieprzeczytanych maili
    for i in range(0, liczbaUnread):
        print(f"{i+1}. {unreadmails[i].messages[0].subject} \033[91mFROM\033[0m  {unreadmails[i].messages[0].sender}")
# wybierz maila do odczytu
    mailToRead = int(input("\033[92mwhich email do you want to read? \033[0m"))
    print(unreadmails[mailToRead-1].messages[0].body)
    if len(unreadmails[mailToRead-1].messages[0].attachments) >= 1: #sprawdzenie czy istnieje załącznik
        downloadpath = input("\033[92mwhere do you want to download the attachments?: \033[0m")
        unreadmails[mailToRead-1].messages[0].downloadAllAttachments(downloadFolder=downloadpath)
elif choice == 3:
    print(ezgmail.EMAIL_ADDRESS)

else:
    print(f"There is no such option as {choice}")