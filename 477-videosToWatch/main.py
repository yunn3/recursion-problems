def videosToWatch(time: list[int], dailyGoal: int) -> int:
    total = 0
    for video_num in range(len(time)):
        total += time[video_num]
        if total >= dailyGoal:
            return video_num + 1

    return -1
