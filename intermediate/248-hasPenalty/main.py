def hasPenalty(records: list[int]) -> bool:
    before_record = records[0]

    for record in records[1:]:
        if record < before_record:
            return True
        else:
            before_record = record
    return False


print(hasPenalty(([100, 200, 200, 200, 300, 400])))
