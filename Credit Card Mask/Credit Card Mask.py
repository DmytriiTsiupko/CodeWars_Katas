#return masked string

def maskify_n1(string):

    if string == '':
        return string
    elif len(string) <= 4:
        return string
    else:
        masked_str = ''
        count = 0
        while count < len(string) - 4:
            masked_str += '#'
            count += 1
        masked_str += string[-4::]
        return masked_str




def maskify_n2(str):

    return '#' * (len(str) - 4) + str[-4:]


