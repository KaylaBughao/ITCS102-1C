
from getpass import getpass

username = 'kayla'
pword = 'kyl1085'

u = input("USERNAME --> ")
p = getpass("PASSWORD --> ")

if (u == username) and (p == pword) :

         print("Account Granted")
else:
         print("Account Denied")