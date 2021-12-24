import pyfiglet
# import sys
# import socket
# from datetime import datetime
import time
from socket import *

"""
YOU CANNOT ENTER INTERNET PROTOCOL VERSION 6 (IPv6)
USE WISELY
"""

ASCII_BANNER_16473234 = pyfiglet.figlet_format("CONSOLE   PORT SCANNER")
print(ASCII_BANNER_16473234)
print("Scan 450 Ports Quick Starting From Port 50. Usually takes about 17 mins to scan 450 ports.\n")

try:
    STARTING_TIME_685462907 = time.time()
    if __name__ == '__main__':
        TARGETING_ON_21374123 = input('Enter the IP address (host) to scan: ')
        INTERNET_PROTOCOL_CONNECTION_418271420 = gethostbyname(TARGETING_ON_21374123)
        print('SCANNING HOST: ', INTERNET_PROTOCOL_CONNECTION_418271420)

        for SCANNING_PORTS_7251730 in range(50, 500):
            SOCKET_CONNECTION_037401388 = socket(AF_INET, SOCK_STREAM)
            CONNECTING_2301243374 = SOCKET_CONNECTION_037401388.connect_ex((INTERNET_PROTOCOL_CONNECTION_418271420, SCANNING_PORTS_7251730))
            print("Scanning on port: ", SCANNING_PORTS_7251730, "| FILTERING")
            if CONNECTING_2301243374 == 0:
                print('PORT FOUND! (%d): OPEN' % (SCANNING_PORTS_7251730,))
            SOCKET_CONNECTION_037401388.close()
    print('Scan completed in:', time.time() - STARTING_TIME_685462907)

except KeyboardInterrupt:
    print("Exiting... Keyboard Interrupt.")

except AttributeError:
    print("An error occurred while handling errors. Exiting...")