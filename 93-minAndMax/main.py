def minAndMax(intArr: list) -> list:

    result = []

    intlist = intArr
    sorted_list = sorted(intlist)
    except_min_list = sorted_list[1:]
    except_max_list = sorted_list[:-1]

    highest_price = calcTotalPrice(except_min_list)
    lowest_price = calcTotalPrice(except_max_list)

    result.append(lowest_price)
    result.append(highest_price)

    return result


def calcTotalPrice(purchase_list: list) -> int:

    total_price = 0

    for price in purchase_list:
        total_price += price

    return total_price


print(minAndMax([5, 3, 2, 3, 4]))
