# add the square root and exponent

def main():
    titlescreen()
    inputf()


def titlescreen():
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
            userinput = str(input("> "))
            if userinput in ["+","-","*","/","^","#","0"] :
                if userinput != "0" and userinput != "#" and userinput != "^":
                    num1 = int(input("N#1: "))
                    num2 = int(input("N#2: "))
                break
    

    match userinput :
        case "+" :
            result = (num1 + num2)
        case "-" :
            result = (num1 - num2)
        case "*" :
            result = (num1 * num2)
        case "/" :
            result = (num1 / num2)
        case "^" :
            print("unavailable")
        case "#" :
            print("unavailable")
            """
            try :
                sqrnum = int(input("Type a number to square root: "))
                sqrresult = "idk"
            except ValueError :
                print("Invalid number")
            """


        case "0" :
            print("Exitting...")
        

    if userinput != "0" and userinput != "#" and userinput != "^":
        print(f"{num1} {userinput} {num2} = {result}")  
    # elif userinput == "#" :
        # print(f"Square root of {sqrnum} = {sqrresult}")
        

main()