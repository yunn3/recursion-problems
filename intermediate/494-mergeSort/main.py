from math import inf as INF


def mergeSort(arr: list) -> list:

    def _helper(start: int, end: int) -> list:
        if start == end:
            return [arr[start]]

        mid = (start + end) // 2
        # 配列要素が２個以上あるときは分割しておく
        left_arr = _helper(start, mid)
        right_arr = _helper(mid + 1, end)

        return _merge_list(left_arr, right_arr)

    def _merge_list(left_arr: list, right_arr: list) -> list:

        left_arr.append(INF)
        right_arr.append(INF)

        combined_arr = []
        l_max = len(left_arr) - 1
        r_max = len(right_arr) - 1
        l_index = 0
        r_index = 0

        # 左右の[ソート済み]配列すべての要素が結合されるまで繰り返す
        while l_index < l_max or r_index < r_max:
            # 左の要素のほうが小さい、または等しいのであれば左の要素を結合する
            if left_arr[l_index] <= right_arr[r_index]:
                combined_arr.append(left_arr[l_index])
                l_index += 1
            # 右の要素のほうが小さいのであれば右の要素を結合する
            else:
                combined_arr.append(right_arr[r_index])
                r_index += 1

        return combined_arr

    return _helper(0, len(arr) - 1)


mergeSort([11, 45, 32, 75, 88, 15, 15])
