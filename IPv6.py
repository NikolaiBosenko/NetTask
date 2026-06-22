
class IPv6:
    __IPv6Adress: list
    __submask: int
    def __init__(self, iPv6Adress: str, submaskLen: int = 64):
        self.__submask = submaskLen
        if self.__submask <= 0 or self.__submask >= 128:
            raise ("Invalid IPv6 submask len format")
        iPv6Adress = iPv6Adress.replace("::", "*")
        if iPv6Adress.count("*") > 1:
            raise ("Invalid IPv6 submask len format")
        reproducedZerros: str = ""
        if iPv6Adress[0] == "*" and len(iPv6Adress) == 1:
            numberReducedOcteds: int = 7
            reproducedZerros: str = numberReducedOcteds * "0:" + "0"
        elif iPv6Adress[-1] == "*":
            numberReducedOcteds: int = 8 - (iPv6Adress.count(":") + 1)
            reproducedZerros: str = numberReducedOcteds * ":0"
        elif iPv6Adress[0] == "*":
            numberReducedOcteds: int = 8 - (iPv6Adress.count(":") + 1)
            reproducedZerros: str = numberReducedOcteds * "0:"
        else:
            numberReducedOcteds: int = 8 - (iPv6Adress.count(":") + 2)
            reproducedZerros: str = numberReducedOcteds * ":0" + ":"
        iPv6Adress = iPv6Adress.replace("*", reproducedZerros)

        self.__IPv6Adress = iPv6Adress.split(":")
        if len(self.__IPv6Adress) != 8:
            raise("Invalid IPv6 adress format")

        for octed in self.__IPv6Adress:
            if int(octed, 16) < 0 or int(octed, 16) >= 65536:
                raise("Invalid IPv6 adress format")

    def __str__(self):
        iPv6Adress: str = ""
        for i in range(len(self.__IPv6Adress) - 1):
            iPv6Adress += (self.__IPv6Adress[i] + ":")
        iPv6Adress += self.__IPv6Adress[-1]
        return iPv6Adress

    def __call__(self):
        leadingZerros: str = ""
        ommitedZerros: str = ""
        iPv6AdressBin: str = ""
        for octed in range(len(self.__IPv6Adress) - 1):
            for digit in self.__IPv6Adress[octed]:
                binDigit = bin(int(digit, 16))[2::]
                leadingZerros = "0" * (4 - len(binDigit))
                iPv6AdressBin += (leadingZerros + binDigit)
            ommitedZerros: str = "0000" * (4 - len(self.__IPv6Adress[octed]))
            iPv6AdressBin += ommitedZerros
            iPv6AdressBin += "."
        for digit in self.__IPv6Adress[-1]:
            binDigit = bin(int(digit, 16))[2::]
            leadingZerros = "0" * (4 - len(binDigit))
            iPv6AdressBin += (leadingZerros + binDigit)
        ommitedZerros: str = "0000" * (4 - len(self.__IPv6Adress[-1]))
        iPv6AdressBin += ommitedZerros
        return iPv6AdressBin

    def __iter__(self):
        return self.__IPv6Adress.__iter__()

    def __len__(self):
        return self.__submask

def findSmallestIPv6SubmaskLen(ip1: IPv6, ip2: IPv6):
    ipv6Adress1: str = ip1()
    ipv6Adress2: str = ip2()

    SmallestInitSubmask: int = min(len(ip1), len(ip2))

    SmallestIpv6SubmaskLen: int = 0

    for i in range(SmallestInitSubmask):
        if ipv6Adress1[i] == ipv6Adress2[i]:
            SmallestIpv6SubmaskLen += 1
        else:
            break

    return SmallestIpv6SubmaskLen

ip1 = IPv6("f2c6:e19b:da60:52ad:2cef:62fe:0279:af3f", 32)
ip2 = IPv6("f2c6:e19b:da60:52ad::0279:af3f", 48)
ip3 = IPv6("f2c6:e19b:da60:52ad:0279:af3f::", 48)
ip4 = IPv6("::f2c6:e19b:da60:52ad:0279:af3f", 48)

print(ip1)
print(ip2)
print(ip3)
print(ip4)

submask1: int = findSmallestIPv6SubmaskLen(ip1, ip2)
print(submask1)

