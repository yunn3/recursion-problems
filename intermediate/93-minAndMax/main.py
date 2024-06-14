def minAndMax(intArr: list) -> list:

    result = []

    sorted_list = sorted(intArr)
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
