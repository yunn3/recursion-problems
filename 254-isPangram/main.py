def isPangram(string):
    cache = [False] * 26
    lower_string = string.lower()

    for character in lower_string:
        if not ("a" <= character <= "z"):
            continue

        if not cache[ord(character) - 97]:
            cache[ord(character) - 97] = True

    return False not in cache
