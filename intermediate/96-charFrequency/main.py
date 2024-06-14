def charFrequency(message: str) -> list:
    hash_map = {}

    for character in message:
        if character in hash_map:
            hash_map[character] = hash_map[character] + 1

        elif "a" <= character <= "z":
            hash_map[character] = 1

    return sorted(f"{character} : {count}" for character, count in hash_map.items())
