#masthan reversenumber 05/09/22
def reverse(n):
    num = ""
    for i in n:
        num = i + num
    return num
n =  "-AD1947"                                                                                                                                                                         

print("The original number is : ", end="")
print(n)

print("The reversed number(using loops) is  : ", end="")
print(reverse(n))
