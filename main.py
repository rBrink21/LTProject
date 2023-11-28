
from BillCalculator import BillCalculator


def main():
    while True:
        user_input = take_input()
        bills = BillCalculator(user_input)
        bills.print_out()

def take_input():
    user_choice = input("Enter an amount to see the change or 0 to exit \n")
    if user_choice == "0":
        exit(0)
    else:
        try:
            amount = float(user_choice)
            amount = round(amount,2)
            return amount
        except:
            print("Not a number!")



if __name__ == '__main__':
    main()

