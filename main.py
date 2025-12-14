print("<---Due amount calculator--->")

def actual_price():
    while True:
        try:
            original_price = input("\n Actual amount of the product :")
            original_price_int=float(original_price)
            if original_price_int > 0:
                return  original_price_int
            else:
                print("\n Original price cannot be zero or less :")
        except ValueError:
            print("\n please give proper input")

def down_payment(real_value):
    while True:

        try:
            down_payment_amount_str = input("\n Enter the down payment amount :")
            down_payment_amount=float(down_payment_amount_str)
            if down_payment_amount >= 0:
                if down_payment_amount < real_value:
                    return down_payment_amount
                else :
                    print("\n Down payment cannot be greater than actual price :")

            else:
                print("\n Down payment cannot be a negative number")
        except ValueError:
            print("\n please enter proper Natural number as value")

def months():
    while True:
        try:
            months_str = input("\n total numbers of month :")
            months_int = int(months_str)
            if months_int > 0:
                return months_int

            else:
                print("\nmonths cannot be zero or less")
        except (TypeError, ValueError):
            print("\n months   should be a natural number")

def due_amount(real_value):
    while True:
        try:
            due_amt = input("\n Due amount per month :")
            due_amt_pm=float(due_amt)
            if due_amt_pm > 0:
                if due_amt_pm < real_value:
                    return due_amt_pm
                else:
                    print("\n Due amount per month cannot exceed or equal the actual price")
            else :
                print("\n Due amount cannot be a zero or less")
        except ValueError:
            print("\n Due amount only be natural numbers")

def executions():
    real_value = actual_price()
    d_payment = down_payment(real_value)
    time_period = months()
    pay_per_month = due_amount(real_value)

    due_total = time_period * pay_per_month

    sum_of_all_payment = due_total + d_payment

    print(f"\n The amount of total due in {time_period} months is  :{due_total}")
    print(f"\n The amount you pay with down payment +  due in total is  :{sum_of_all_payment}")
    print(f"\n you pay extra  of  in {time_period} months :", sum_of_all_payment - real_value)





executions()





