
def get_amount():
    while True:
     input_value = input("Enter the amount: ")
     if (input_value.isdecimal() != True or int(input_value) < 0):
        print("Invalid amount")
     return input_value

while True:
    input_value = get_amount()

    currency_value = input("Source currency (USD/CAD/EUR)")
    data = {"USD": 1, "EUR": 0.74, "CAD": 1.27}
    if currency_value not in data:
        print("Invalid currency")
    else:
        target_currency = input("Target currency (USD/CAD/EUR)")
        if target_currency not in data:
            print("Invalid currency")
        else:
            if target_currency == "USD":
                print("Converted amount: ", int(input_value) * data["USD"])
                break
            elif target_currency == "CAD":
                print("Converted amount: ", int(input_value) * data["CAD"])
                break
            else:
                print("Converted amount: ", int(input_value) * data["EUR"])
                break