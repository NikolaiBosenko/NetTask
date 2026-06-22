import IPv6

def isBinAdressCorrect(ipv6Adress: IPv6.IPv6, answer: str):
    return ipv6Adress() == answer

def isBinAdressCorrect1():
    if isBinAdressCorrect(IPv6.IPv6("4ffe:2900:5545:3210:2000:f8ff:fe21:67cf"),
                          "0100111111111110.0010100100000000.0101010101000101.0011001000010000.0010000000000000.1111100011111111.1111111000100001.0110011111001111"):
        print("Test 1 is passed!")
    else:
        print("Test 1 is failed!")

def isBinAdressCorrect2():
    if isBinAdressCorrect(IPv6.IPv6("2001:db80::ff:4200:8329"),
                          "0010000000000001.1101101110000000.0000000000000000.0000000000000000.0000000000000000.1111111100000000.0100001000000000.1000001100101001"):
        print("Test 2 is passed!")
    else:
        print("Test 2 is failed!")

def isBinAdressCorrect3():
    if isBinAdressCorrect(IPv6.IPv6("c0de::"),
                          "1100000011011110.0000000000000000.0000000000000000.0000000000000000.0000000000000000.0000000000000000.0000000000000000.0000000000000000"):
        print("Test 3 is passed!")
    else:
        print("Test 3 is failed!")

def isBinAdressCorrect4():
    if isBinAdressCorrect(IPv6.IPv6("::"),
                          "0000000000000000.0000000000000000.0000000000000000.0000000000000000.0000000000000000.0000000000000000.0000000000000000.0000000000000000"):
        print("Test 4 is passed!")
    else:
        print("Test 4 is failed!")

def isMinSubmaskCorrect(ip1: IPv6.IPv6, ip2: IPv6.IPv6, answ: int):
    return IPv6.findSmallestIPv6SubmaskLen(ip1, ip2) == answ

def isMinSubmaskEqualto16():
    ip1 = IPv6.IPv6("ffff::", 48)
    ip2 = IPv6.IPv6("ffff:1000::", 48)
    if isMinSubmaskCorrect(ip1, ip2, 16):
        print("Submask test 1 passed!")
    else:
        print("Submask test 1 passed!")


def isMinSubmaskEqualto32():
    ip1 = IPv6.IPv6("::", 32)
    ip2 = IPv6.IPv6("::", 32)
    if isMinSubmaskCorrect(ip1, ip2, 32):
         print("Submask test 2 passed!")
    else:
        print("Submask test 2 passed!")


def isMinSubmaskEqualto32_2():
    ip1 = IPv6.IPv6("ffff:1000:1000::", 48)
    ip2 = IPv6.IPv6("ffff:1000::", 48)
    if isMinSubmaskCorrect(ip1, ip2, 16):
        print("Submask test 3 passed!")
    else:
        print("Submask test 3 passed!")

def isMinSubmaskEqualto48():
    ip1 = IPv6.IPv6("ffff:1000:1010::", 64)
    ip2 = IPv6.IPv6("ffff:1000:1010:1100::", 64)
    if isMinSubmaskCorrect(ip1, ip2, 16):
        print("Submask test 4 passed!")
    else:
        print("Submask test 4 passed!")

def isMinSubmaskEqualto0():
    ip1 = IPv6.IPv6("0fff:1000:1010::", 64)
    ip2 = IPv6.IPv6("ffff:1000:1010:1100::", 64)
    if isMinSubmaskCorrect(ip1, ip2, 0):
        print("Submask test 5 passed!")
    else:
        print("Submask test 5 passed!")

def isMinSubmaskEqualto12():
    ip1 = IPv6.IPv6("ffff:1000:1010::", 12)
    ip2 = IPv6.IPv6("ffff:1000:1010:1100::", 16)
    if isMinSubmaskCorrect(ip1, ip2, 12):
        print("Submask test 6 passed!")
    else:
        print("Submask test 6 passed!")

