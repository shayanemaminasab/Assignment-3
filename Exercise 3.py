import math

sin=math.sin
cos=math.cos
tan=math.tan
fac=math.factorial
sqrt=math.sqrt

a= int(input("Enter a number: "))
op= input("Enter op: ")

if op=="sin" or op=="cos" or op=="tan" or op=="fac" or op=="sqrt" or op=="cot":
    if op == "sin":
        r=sin(a)

    if op == "cos":
        r=cos(a)

    if op == "tan":
        r=tan(a)

    if op == "cot":
        o=tan(a)
        r=1/o

    if op == "fac":
        if a<0:
            r="Error"
        else:
            r=fac(a)

    if op == "sqrt":
        r=sqrt(a)
else:
    b=int(input("Enter a number: "))

    if op == "+":
        r=a+b

    if op == "-":
        r=a-b

    if op == "*":
        r=a*b

    if op == "/":
        if b == 0:
            r = "Error"
        else:
            r=a/b

print(r)