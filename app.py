from cal_function import do_addition,do_substraction

def main():
    print("Welcome to the calculator app: ")
    print("Select a function \n 1. Add \n 2. Substract ")

    user_input = input("Select: ")
    if user_input == "1":
        a = int(input("Value of A: "))
        b = int(input("Value of B: "))
        result = do_addition(a,b)
    if user_input == "2":
        a = int(input("Value of A: "))
        b = int(input("Value of B: "))
        result = do_substraction(a,b)
    print(result)

if __name__ == "__main__":
    main()