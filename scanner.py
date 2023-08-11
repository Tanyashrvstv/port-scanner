import pyfiglet
import socket
import sys
from colorama import init, Fore

init()
GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX

#Defining banner
text = pyfiglet.figlet_format("TANYA SCANNER")
print(text)
print("-"  * 50)
target = input("Enter target: ")

host = socket.gethostbyname(target)

try:

    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = s.connect_ex((target, port))
        if result == 0:
            print(f"{GREEN}[+] {host}:{port} is open      {RESET}")
        else:
            print(f"{GRAY}[!] {host}:{port} is closed    {RESET}", end="\r")

        s.close()

except KeyboardInterrupt:
    print("\n Exiting")
    sys.exit()

except socket.gaierror:
    print("\n Could not resolve hotname")
    sys.exit()

except socket.error:
    print("\n Server not responding")
    sys.exit()