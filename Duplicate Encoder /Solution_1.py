
def duplicate_encode(word):

    word = word.lower()
    encode_string = ""
    count_char = {}

    for char in word:
        if char not in count_char:
            count_char[char] = 1
        else:
            count_char[char] += 1

    for char in word:
        if count_char[char] == 1:
            encode_string += "("
        else:
            encode_string += ")"

    return encode_string



