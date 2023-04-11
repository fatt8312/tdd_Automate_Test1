from test_motorcycle_payment import calculate_monthly_payment

def main():
    # Prompt the user to input the motorcycle price and down payment
    while True:
        try:
            motorcycle_price = float(input("Enter the motorcycle price: "))
            if motorcycle_price <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a positive number.")
    while True:
        try:
            down_payment = float(input("Enter the down payment: "))
            if down_payment <= 0 or down_payment < motorcycle_price * 0.2:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a positive number.")
            print("Down payment must be at least 20% of the motorcycle price.")

    # Calculate the monthly payment using the calculate_monthly_payment function
    monthly_payment = calculate_monthly_payment(motorcycle_price, down_payment)

    # Display the monthly payment to the user
    print("Monthly payment: {:.2f} baht".format(monthly_payment))

if __name__ == '__main__':
    main()
