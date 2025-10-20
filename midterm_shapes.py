import math
# def rectangle(n):
#     result = ""

#     for i in range (n):
#         result += "*" * n + "\n"

#     print(result)

#     return result.rstrip()
# rectangle(5)

###################################################

# def triangle_rectangle(n):
#     result = ""

#     for row in range (1, n+1):
#             result += "*" * row + "\n"

#     print(result)

#     return result.rstrip()
# triangle_rectangle(10)

##################################################

# def triangle(n):fbfg
#     result = ""
#     for i in range (1, n+1):
#             result += " " * (n-i) + "*" * (2*i-1) + "\n"

#     print(result)

#     return result.rstrip()
# triangle(8)

###################################################

def diamond(n):
    result = ""
    for i in range (1,n):
         result += " " * (n-i) + "*" * (2*i-1) + "\n"

    for i in range (n-1,0,-1): #start at n-1 uptil 0, with increments of -1
         result += " " * (n-i) + "*" * (2*i-1) + "\n"
         
    print(result)

    return result.rstrip()
diamond(5)

#different way of doing it

def diamond(n):
    result = ""
    
    for i in range (1,n):
        star = "*" * (2*i-1)
        space = " " * (n-1)
        result += space + star + "\n"

    for i in range (n-1,0,-1): #start at n-1 uptil 0, with increments of -1
        star = "*" * (2*i-1)
        space = " " * (n-1)
        result += space + star + "\n"
        
         
    print(result)

    return result.rstrip()
diamond(5)