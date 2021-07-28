# 按照要求来就行，比较复杂的是有掩码的情况，可以去牛客看看
class Solution:
    def validIPAddress(self, IP: str) -> str:
        a = IP.split(".")
        b = IP.split(":")
        if len(a) == 4:
            for byte in a:
                if not byte:
                    return "Neither"
                if byte != '0' and byte[0] == '0':
                    return "Neither"
                else:
                    for bit in byte:
                        if not bit.isdigit():
                            return "Neither"
                    num = int(byte)
                    if num > 255:
                        return "Neither"
            return "IPv4"
        if len(b) == 8:
            for byte in b:
                if not byte:
                    return "Neither"
                if len(byte) > 4:
                    return "Neither"
                else:
                    for bit in byte:
                        if not (bit.isdigit() or bit.isalpha()):
                            return "Neither"
                        if bit.isalpha():
                            if bit.lower() > 'f':
                                return "Neither"
            return "IPv6"
        return "Neither"
                    
