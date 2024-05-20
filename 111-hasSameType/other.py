def hasSameType(user1: str, user2: str) -> bool:
    # 長さが異なる場合は即座にFalseを返す
    if len(user1) != len(user2):
        return False

    mapping = {}  # user1とuser2の文字のマッピング
    mapping_values = set()  # mappingで格納済みの値のセット

    for type1, type2 in zip(user1, user2):
        if type1 not in mapping:
            # type1はマッピングしていないのに、type2はマッピング済みの場合Falseを返す
            if type2 in mapping_values:
                return False
            mapping[type1] = type2
            mapping_values.add(type2)

        # マッピングが異なる場合はFalseを返す
        elif mapping[type1] != type2:
            return False

    return True


test_data = [
    {
        "input": ("aaabbbccc", "xxxyyyzzz"),
        "correct": True,
        "description": "同じ構造すべて違う文字",
    },
    {
        "input": ("aaabbbccc", "aaabbbccc"),
        "correct": True,
        "description": "同じ構造すべて同じ文字",
    },
    {
        "input": ("aaabbbccc", "cccaaabbb"),
        "correct": True,
        "description": "同じ構造すべて同じ文字だが配置が違う",
    },
    {
        "input": ("aaabbbccc", "aaacccbbb"),
        "correct": True,
        "description": "同じ構造すべて同じ文字だが部分的に配置が異なる",
    },
    {
        "input": ("aaabbbccc", "xxxyyyxyz"),
        "correct": False,
        "description": "異なる構造すべて違う文字",
    },
    {
        "input": ("aaabbbccc", "abcabcabc"),
        "correct": False,
        "description": "異なる構造すべて同じ文字がばらばら",
    },
    {
        "input": ("aaabbbccc", "aaababccc"),
        "correct": False,
        "description": "異なる構造すべて同じ文字部分的に配置が異なる",
    },
    {
        "input": ("aaabbbccc", "xxxbbbycc"),
        "correct": False,
        "description": "異なる構造部分的に異なる文字",
    },
]

for data in test_data:
    result = hasSameType(data["input"][0], data["input"][1])

    if result == data["correct"]:
        print("OK", data, result)
    else:
        print("NG", data, result)
