#Armstrong number

def armstrong(value):

    sum = 0
    str_value = str(value)

    for numb in str(value):
        numb = int(numb) ** len(str_value)
        sum += numb

    if sum == value:
        return True
    else:
        return False
