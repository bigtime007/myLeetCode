def gcdOfStrings(str1, str2):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    if str1 + str2 != str2 + str1:
        return ""
    return str1[:gcd(len(str1), len(str2))]

# Example usage
str1 = "ABCABC"
str2 = "ABC"
print(gcdOfStrings(str1, str2))  # Output: "ABC"
