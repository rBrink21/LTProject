import math


class BillCalculator:
    def __init__(self, amount_in_cents):
        self.denominations = [100, 50, 20, 10, 5, 1, 0.25, 0.10, 0.05, 0.01]

        # Amount needs to be in cents/integer in order to avoid floating point math
        self.amountInCents = round(amount_in_cents * 100)

        self.bill_list = self.create_bill_list()
        self.bill_string_list = self.bill_list_to_string(self.bill_list)

    def calculate_bill_amount(self, amount, denomination):
        # Round down to nearest integer

        return math.floor(amount / denomination)

    def create_bill_list(self):
        bill_list = []
        amount_in_cents = self.amountInCents

        for denomination in self.denominations:
            denomination_in_cents = denomination * 100
            bill_amount = self.calculate_bill_amount(amount_in_cents, denomination_in_cents)
            bill_list.append(bill_amount)
            amount_in_cents = amount_in_cents % denomination_in_cents

        return bill_list

    def denomination_to_string(self, amount):
        # Normally i'd use a match statement here but for some reason I only have
        # python 3.6 on my home pc so this will have to do
        if amount >= 1:
            return f"${amount} bill"
        if amount == 0.25:
            return "quarter"
        elif amount == 0.1:
            return "dime"
        elif amount == 0.05:
            return "nickel"
        elif amount == 0.01:
            return "penny"
        else:
            return "none"
    def bill_list_to_string(self, bill_list):
        string_list = []
        for bill_amount, denomination in zip(bill_list, self.denominations):
            if bill_amount > 0:
                new_line = self.construct_line(bill_amount, denomination)
                string_list.append(new_line)
        return string_list

    def construct_line(self, bill_amount, denomination):
        denomination_string = self.denomination_to_string(denomination)
        if bill_amount > 1:
            if denomination_string == "penny":
                denomination_string = "pennies"
            else:
                denomination_string += "s"

        new_line = f"{bill_amount} - " + denomination_string
        return new_line

    def get_bill_list(self):
        return self.bill_string_list

    def print_out(self):
        for line in self.bill_string_list:
            print(line)
