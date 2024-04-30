run = True
name = input("What is your name? ")
while run:
    num = int(input("Please enter an integer between 1 and 100 "))
    if num < 1 or num > 100:
        print(f' {name}, the number {num}, is not valid.')
        break
    if num % 2 == 1:  # checking if the number is odd
        if num < 60:
            print(f' {name}, your number {num}, is Odd and less than 60.' )
        else:
            print(f' {name}, your number {num}, is Odd and greater than 60.')

    else:    #catches numbers that are even
        if num >=2 and num <= 24:
            print(f'Even and less than 25. {name}')
        elif num <= 60:
            print(f' {name}, your number is even and between 26 and 60 inclusive.')
        else:
            print(f' {name}, your number is even and greater than 60.')
    keepRun = input(f' Do you to continue running the program, {name}?(y/n)')
    if keepRun == "y":
        run = True
    else:
        run = False