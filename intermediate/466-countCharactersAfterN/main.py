def countCharactersAfterN(arr):

    after_n = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    count = 0

    for sentence in arr:
        for character in sentence:
            if character in after_n:
                count += 1

    return count
