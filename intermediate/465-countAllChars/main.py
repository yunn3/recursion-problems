def countAllChars(arr):

    count = 0

    for sentence in arr:
        count += len(sentence)

    return count
