
def main():
    while True:
        userChoice = choice()

        if userChoice == 'PR':
            Prime()
        elif userChoice == 'A':
            Armstrong()
        elif userChoice == 'PA':
            Palindrome()
        elif userChoice == 'FI':
            Fibonacci()
        elif userChoice == 'FA':
            Factorial()
        elif userChoice == 'Q':
            exit()
        else:
            print("Error Message: You can only select any of the above given options")



def Prime():
    try:
        userChoice = int(input("Enter the Number: "))
        count = 1
        sum = 0
        while count <= userChoice:
            if userChoice % count == 0:
                sum = sum + 1
            count = count + 1
        if sum == 2:
            print("Number is Prime")
        else:
            print("Number is not Prime")

    except ValueError:
        print("Error Message: You can only enter number")


def Armstrong():
    userChoice = int(input("Enter the Number: "))
    try:
        sum = 0
        num = 0
        temp = userChoice
        while temp > 0:
            num = temp % 10
            sum = sum + num * num * num
            temp = int(temp / 10)
        if sum == userChoice:
            print("armstrong")
        else:
            print("Not armstrong")
    except ValueError:
        print("Error Message: You can only enter number")



def Palindrome():
    try:
        userChoice = input("Enter the Number: ")
        for element in range(len(userChoice)):
            count = 0
            if userChoice[element] != userChoice[len(userChoice)-1 - element]:
                count = 1

        if count == 1:
            print("Not palindrome")
        else:
            print("palindrome")

    except ValueError:
        print("Error Message: You can only enter number")


def Fibonacci():
    try:
        userChoice = int(input("Enter the Number upto which you want to print the series: "))
        a = 0
        b = 1
        sum = 1
        while sum <= userChoice:
            print("fibbonacci", sum)
            sum = a + b
            a = b
            b = sum
    except ValueError:
        print("Error Message: You can only enter number")



def Factorial():
    try:
        userChoice = int(input("Enter the Number: "))
        count = 0
        prod = 1
        while count < userChoice:
            prod = prod * userChoice
            userChoice = userChoice - 1
        print("factorial :", prod)

    except ValueError:
        print("Error Message: You can only enter number")





def choice():
    print()
    print("List of Functions")
    print()
    print(" 'PR' :  Prime ")
    print(" 'A'  :  ArmStrong ")
    print(" 'PA' :  Palindrome ")
    print(" 'FI' :  Fibonacci Series")
    print(" 'FA' :  Factorial")
    print(" 'Q'  :  Quit")
    print()

    userChoice = input("Which function do you want to call: ")

    userChoice = userChoice.upper()

    return userChoice



main()




