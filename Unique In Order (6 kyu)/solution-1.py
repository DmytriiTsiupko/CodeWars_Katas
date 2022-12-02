
def unique_in_order(iterable):

    unique_items = []

    if len(iterable) >= 1:

        unique_items.append(iterable[0])

        for item in iterable:

            if item != unique_items[-1]:
                unique_items.append(item)
    else:
        return unique_items

    return unique_items