import IPv4

def isMinSubmaskCorrect(ip1: IPv4.IPv4, ip2: IPv4.IPv4, answer):

    return IPv4.findMinSubmaskLen(ip1, ip2) == answer

def isMaxSubmaskEqualTo31():
    ip1 = IPv4.IPv4("45.12.19.34", 31)
    ip2 = IPv4.IPv4("45.12.19.34", 31)

    if isMinSubmaskCorrect(ip1, ip2, 31):
        print("Submask test 1 is passed")
    else:
        print("Submask test 1 is failed!")

def isMinSubmaskEqualTo0():
    ip1 = IPv4.IPv4("128.255.255.255") #10000000.11111111.11111111.11111111
    ip2 = IPv4.IPv4("64.255.255.255" ) #01000000.11111111.11111111.11111111

    if isMinSubmaskCorrect(ip1, ip2, 0):
        print("Submask test 2 is passed")
    else:
        print("Submask test 2 is failed!")

def isSubmaskEqualTo8():
    ip1 = IPv4.IPv4("255.255.255.255") #11111111.11111111.11111111.11111111
    ip2 = IPv4.IPv4("255.64.255.255" ) #11111111.01000000.11111111.11111111

    if isMinSubmaskCorrect(ip1, ip2, 8):
        print("Submask test 3 is passed")
    else:
        print("Submask test 3 is failed!")

def isSubmaskEqualTo16():
    ip1 = IPv4.IPv4("255.255.255.255") #11111111.11111111.11111111.11111111
    ip2 = IPv4.IPv4("255.255.64.255" ) #11111111.11111111.01000000.11111111

    if isMinSubmaskCorrect(ip1, ip2, 16):
        print("Submask test 4 is passed")
    else:
        print("Submask test 4 is failed!")

def isSubmaskEqualTo24():
    ip1 = IPv4.IPv4("255.255.255.255") #11111111.11111111.11111111.11111111
    ip2 = IPv4.IPv4("255.255.255.64 ") #11111111.11111111.11111111.01000000

    if isMinSubmaskCorrect(ip1, ip2, 24):
        print("Submask test 5 is passed")
    else:
        print("Submask test 5 is failed!")