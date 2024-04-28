def maxOfPairSum(arr1: list, arr2: list, x: int) -> str:
    largest_number = None
    for index1 in range(len(arr1)):
        for index2 in range(len(arr2)):
            total = arr1[index1] + arr2[index2]
            if (
                largest_number is None
                and total < x
                or largest_number is not None
                and total < x
                and largest_number < total
            ):
                largest_number = total

    if largest_number is None:
        return "no pair"

    return str(largest_number)
