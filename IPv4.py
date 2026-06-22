
class InvalidIPv4Format: Exception

class InvalidIPv4SubmaskFormat: Exception

class IPv4:
    __IPv4Adress: list
    __submask: int
    def __init__(self, iPv4Adress: str, submaskLenghth: int = 24):
        if submaskLenghth <= 0 or submaskLenghth > 32:
            raise InvalidIPv4SubmaskFormat("Invalid IPv4 submask format")
        self.__submask = submaskLenghth

        self.__IPv4Adress = iPv4Adress.split(".")
        if len(self.__IPv4Adress) != 4:
            raise InvalidIPv4Format("Invalid IPv4 format")
        for octed in self.__IPv4Adress:
            if int(octed) < 0 or int(octed) > 255:
                raise ("incorrect IPv4 adress format")

    def __iter__(self):
        return self.__IPv4Adress.__iter__()

    def __call__(self):
        IPv4AdressBin: str = ""
        maxLeadingZerros: int = 8
        for i in range(3):
            leadingZeros = "0" * (maxLeadingZerros - len(bin(int(self.__IPv4Adress[i]))[2::]))
            IPv4AdressBin += (leadingZeros + bin(int(self.__IPv4Adress[i]))[2::])
            IPv4AdressBin += "."
        leadingZeros = "0" * (maxLeadingZerros - len(bin(int(self.__IPv4Adress[3]))[2::]))
        IPv4AdressBin += (leadingZeros + bin(int(self.__IPv4Adress[3]))[2::])
        return IPv4AdressBin

    def __str__(self):
        ipAdress: str = (self.__IPv4Adress[0] + "." +
        self.__IPv4Adress[1] + "." +
        self.__IPv4Adress[2] + "." +
        self.__IPv4Adress[3]
        )
        return ipAdress


    def __len__(self):
        return self.__submask

def findMinSubmaskLen(IP1: IPv4, IP2: IPv4):

    firstIPAdress = IP1().replace(".", "")
    secondIPAdress = IP2().replace(".", "")

    submaskLen: int = 0

    maxSubmaskLen = min(len(IP1), len(IP2))

    for i in range(maxSubmaskLen):
        if firstIPAdress[i] == secondIPAdress[i]:
            submaskLen += 1
        else:
            break
    return submaskLen


ip1 = IPv4("45.78.3.100")
ip2 = IPv4("45.56.2.4")

print(ip1)
print(len(ip1))

ip1()
ip2()

print(ip1())
print(ip2())

print(findMinSubmaskLen(ip1, ip2))

ip3 = IPv4("255.56.3.4")
ip4 = IPv4("64.3.4.5")

print(findMinSubmaskLen(ip3, ip4))


ip5 = IPv4("45.34.23.12")
ip6 = IPv4("45.34.23.12")

print(findMinSubmaskLen(ip5, ip6))
