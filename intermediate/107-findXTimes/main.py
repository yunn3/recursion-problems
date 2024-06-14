def findXTimes(teams: list[str]) -> bool:
    match_count_map = {}

    for team in teams:
        if team not in match_count_map:
            match_count_map[team] = 1

        else:
            match_count_map[team] += 1

    for match_count in match_count_map.values():
        if match_count != match_count_map[teams[0]]:
            return False

    return True


print(findXTimes("babcddc"))  # False
