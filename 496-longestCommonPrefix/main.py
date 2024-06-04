def longestCommonPrefix(strArr: list) -> str:
    def _helper(start: int, end: int) -> str:
        if start == end:
            return strArr[end]
        mid = (start + end) // 2
        left_prefix = _helper(start, mid)
        right_prefix = _helper(mid + 1, end)

        return common_prefix(left_prefix, right_prefix)

    return _helper(0, len(strArr) - 1)


def common_prefix(s1: str, s2: str) -> str:
    if s1 == "" or s2 == "":
        return ""
    min_length = min(len(s1), len(s2))

    def _helper(index: int) -> str:
        if index >= min_length or s1[index] != s2[index]:
            return s1[:index]

        return _helper(index + 1)

    return _helper(0)


print(longestCommonPrefix(["divide", "divided", "diand", "diconquer"]))
