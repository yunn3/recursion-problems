def hasSameType(user1: str, user2: str) -> bool:

    if len(user1) != len(user2):
        return False

    user_map = {}
    for user1_input, user2_input in zip(user1, user2):
        # 初めて見つけたら、マッピングする
        if user1_input not in user_map and user2_input not in user_map.values():
            user_map[user1_input] = user2_input

        # elif user2_input not in user_map.values():
        #     return False

        # elif user1_input not in user_map:
        #     return False

        elif user_map.get(user1_input) != user2_input:
            return False

    return True


# fmt: off
test_data = [
    ("aaabbbccc", "xxxyyyzzz", True, "同じ構造すべて違う文字"),
    ("aaabbbccc", "aaabbbccc", True, "同じ構造すべて同じ文字"),
    ("aaabbbccc", "cccaaabbb", True, "同じ構造すべて同じ文字だが配置がちがう"),
    ("aaabbbccc","aaacccbbb",True,"同じ構造すべて同じ文字だが、部分的に配置が異なる"),
    ("aaabbbccc", "xxxyyyxyz", False, "異なる構造すべて違う文字"),
    ("aaabbbccc", "abcabcabc", False, "異なる構造すべて同じ文字がばらばら"),
    ("aaabbbccc", "aaababccc", False, "異なる構造すべて同じ文字部分的に異なる"),
    ("aaabbbccc", "xxxbbbycc", False, "異なる構造部分的に異なる文字"),
]
# fmt: on

for data in test_data:
    result = hasSameType(data[0], data[1])
    if result == data[2]:
        print("OK", result)
    else:
        print("NG", data[3], data[0], data[1], result)
