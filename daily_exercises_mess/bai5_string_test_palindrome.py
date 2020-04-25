# s1 = input("Enter string: ")
# s2 = s1[::-1]
# if (s1 == s2):
#     print (True)
# else:
#     print(False)

def reverse(s):
    return s1[::-1]
def isPalindrome(s1):
    s2 = reverse(s1)
    if (s1 == s2):
        print (True)
    else:
        print(False)
s1 = input("Enter string: ")
dapan = isPalindrome(s1)
