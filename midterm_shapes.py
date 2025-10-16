import math
# def rectangle(n):
#     result = ""

#     for i in range (n):
#         result += "*" * n + "\n"

#     print(result)

#     return result.rstrip()
# rectangle(5)


# def triangle_rectangle(n):
#     result = ""

#     for row in range (1, n+1):
#             result += "*" * row + "\n"

#     print(result)

#     return result.rstrip()
# triangle_rectangle(10)

def triangle(n):
    result = ""
    spaces = ""
    for i in range (1, n+1):
            spaces = " "
            result += spaces +"*" * row + spaces + "\n"

    print(result)

    return result.rstrip()
triangle(10)