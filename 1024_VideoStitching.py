"""
You are given a series of video clips from a sporting event that lasted t seconds.  These video clips can be overlapping
 with each other and have varied lengths.

Each video clip clips[i] is an interval: it starts at time clips[i][0] and ends at time clips[i][1].  We can cut these
clips into segments freely: for example, a clip [0, 7] can be cut into segments [0, 1] + [1, 3] + [3, 7].

Return the minimum number of clips needed so that we can cut the clips into segments that cover the entire sporting
event ([0, t]).  If the task is impossible, return -1.
"""
from typing import List


def video_stitching(clips: List[List[int]], t: int) -> int:
    """
    :param clips: time interval of the ith clip starts at clips[i][0] and ends at clips[i][1]
    :param t: target time period [0, t]
    :return: min number of clips needed to reconstruct [0, t]
    """
    stitches_cover_without_last_clip, latest_all_clips, min_count = -1, 0, 0

    # Greedy algorithm: at every step takes the clip that extends the stitches furthest
    # sort videos by start time, and then end time
    # i.e. order videos with same start time by video length in reverse order
    for clip_i_start, clip_i_end in sorted(clips):
        if latest_all_clips >= t or clip_i_start > latest_all_clips:
            # have covered [0, t] or a gap cannot be filled by any clip
            break
        elif stitches_cover_without_last_clip < clip_i_start:
            # - else statement guarantees  clip_i_start <= latest_all_clips
            # - stitches_cover_without_last_clip < clip_i_start means this is the first clip that doesn't cover
            # [stitches_cover_without_last_clip, clip_i_start - 1], cannot be used for previous round last clip
            # - greedily takes in any clip that can extends stitch length
            # - replace with longer clips in next iterations
            min_count, stitches_cover_without_last_clip = min_count + 1, latest_all_clips
        # else:
        # replace last clip with longer clips
        # maintain stitches_cover_without_last_clip, and extend latest_all_clips

        latest_all_clips = max(latest_all_clips, clip_i_end)

    return min_count if latest_all_clips >= t else -1


test_cases = [([[1, 9], [1, 5], [0, 4]], 6, 2),
              ([[4, 9], [3, 5], [0, 4]], 6, 2),
              ([[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]], 10, 3),
              ([[0, 1], [1, 2]], 5, -1),
              ([[0, 1], [6, 8], [0, 2], [5, 6], [0, 4], [0, 3], [6, 7], [1, 3], [4, 7], [1, 4], [2, 5], [2, 6], [3, 4],
                [4, 5], [5, 7], [6, 9]], 9, 3),
              ([[0, 4], [2, 8]], 5, 2),
              ([[1, 13], [7, 9], [14, 17], [12, 15], [16, 18], [10, 11], [0, 8], [3, 16]], 30, -1), ]
for test_clips, test_t, expected_output in test_cases:
    assert video_stitching(test_clips, test_t) == expected_output
