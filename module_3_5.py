def get_multiplied_digits(number):
    str_number = (str(number))
    first_ = (int(str_number[0]))
    if len(str_number) > 1:
        return first_ * get_multiplied_digits(int(str_number[1:]))
    elif len(str_number) <= 1:
        return first_
result = get_multiplied_digits(40203)
print(result)


