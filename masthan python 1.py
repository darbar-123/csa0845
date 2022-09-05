#masthan reversestring1 05/09/22
def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
s =  "1245"                                                                                                                                                                         

print("The original string is : ", end="")
print(s)

print("The reversed string(using loops) is  : ", end="")
print(reverse(s))
