import math

def main():
        options()
        inputf()


def options():
    print("********************* CALCULATOR *********************")
    print("Choose an operator {for Quit -> 0} :")
    print(" (+) - ADDITION")
    print(" (-) - SUBTRACTION")
    print(" (*) - MULTIPLICATION")
    print(" (/) - DIVISION")
    print(" (^) - EXPONENT")
    print(" (#) - SQUARE ROOT")

def inputf():
    while True:
            operator = str(input("> "))
            if operator in ["+","-","*","/","^","#","0"] :
                if operator != "0" and operator != "#":
                    num1 = int(input("N#1: "))
                    num2 = int(input("N#2: "))
                break
    
    final = True
    match operator :
        case "+" :
            result = (num1 + num2)
        case "-" :
            result = (num1 - num2)
        case "*" :
            result = (num1 * num2)
        case "/" :
            if num1 == num2 == 0 :
                print("ERROR")
                final = False
            else :
                result = (num1 / num2)
        case "^" :
            result = (num1 ** num2)
            final = False
        case "#" :
            try :
                sqrnum = int(input("Type a number to take square root: "))
                sqrresult = math.sqrt(sqrnum)
            except ValueError :
                print("Invalid number")
            final = False


        case "0" :
            print("EXITTING...")
            final = False
        

    if final == True:
        print(f"{num1} {operator} {num2} = {result}") 
    elif operator == "#" :
        print(f"Square root of {sqrnum} = {sqrresult}")
    elif operator == "^" :
        print(f"{num1} ^ {num2} = {result}")
    # again sec
    if operator != "0" :
        main()

main()
print("******************************************************")
