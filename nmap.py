import socket
import sys
from colorama import init, Style, Fore
import time
import re

print(Fore.CYAN + Style.BRIGHT + """
 PPPPP  OOO  RRRRR  TTTTT   SSSSS  CCCC  AAAAA  N   N  N   N  EEEEE  RRRRR
 P   P O   O R   R    T     S      C     A   A  NN  N  NN  N  E      R   R
 PPPPP O   O RRRRR    T     SSSSS  C     AAAAA  N N N  N N N  EEEE   RRRRR
 P     O   O R  R     T         S  C     A   A  N  NN  N  NN  E      R  R
 P      OOO  R   R    T     SSSSS  CCCC  A   A  N   N  N   N  EEEEE  R   R

                                   -PORT SCANNER
    """)

print(Fore.RED + Style.BRIGHT + "Port Scanner - By Faijas")
print(Fore.YELLOW + "----------------------------------------------------")


def is_valid_ip(target):

    regex = r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$'
    domain_regex = r'^(?!-)[A-Za-z0-9-]{1,63}(?<!-)(?:\.[A-Za-z]{2,6})+$'
    return bool(re.match(regex, target) or re.match(domain_regex,target))


def port_scan(target, port):

    try:

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.settimeout(2)

        result = sock.connect_ex((target, port))

        if result == 0:
            print(Fore.WHITE + f"Port {port} " + Fore.GREEN + " is open")
        else:
            print(Fore.WHITE + f"Port {port} " + Fore.RED + " is not open")
        sock.close()

    except socket.error as err:
        print(Fore.RED+ f"{err}")
        return


def get_target(target):
    dot = [".", "..", "...", "....", "....."]
    for _ in range(6):
        for symbol in dot:
            sys.stdout.write(
                 Fore.WHITE + "\rScanning target: "+Fore.RED + f"{target}" + Fore.WHITE + f" {symbol}")
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write("\r" + " " * 50 + "\r")
    print(Fore.WHITE + "Scan complete!\n")

    common_ports = [22, 80, 443, 8080, 21, 25, 53, 110, 3306, 5432]

    for port in common_ports:
        port_scan(target, port)


target = input(Fore.WHITE + "Enter the target IP address or domain name: ")
valid_input = is_valid_ip(target)

if valid_input:
    get_target(target)
else:
    print(Fore.RED + "\nInvalid Target IP! Please restart the program with a valid IP.")
