def is_mobile_number(number):
    if len(number) != 10:
        return False
    else:
        if number[0] != "0":
            return False
        else:
            if number[1] != "6" and number[1] != "8" and number[1] != "9":
                return False
            else:
                return True


number = input()
if is_mobile_number(number):
    print("Mobile number")
else:
    print("Not a mobile number")
