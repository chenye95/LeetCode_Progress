"""
You are given a series of video clips from a sporting event that lasted T seconds.  These video clips can be overlapping
 with each other and have varied lengths.

Each video clip clips[i] is an interval: it starts at time clips[i][0] and ends at time clips[i][1].  We can cut these
clips into segments freely: for example, a clip [0, 7] can be cut into segments [0, 1] + [1, 3] + [3, 7].

Return the minimum number of clips needed so that we can cut the clips into segments that cover the entire sporting
event ([0, T]).  If the task is impossible, return -1.
"""
from typing import List


def video_stitching(clips: List[List[int]], T: int) -> int:
    """
    :param clips: time interval of the ith clip starts at clips[i][0] and ends at clips[i][1]
    :param T: target time period [0, T]
    :return: min number of clips needed to reconstruct [0, T]
    """
    stitches_cover_without_last_clip, latest_all_clips, min_count = -1, 0, 0

    # Greedy algorithm: at every step takes the clip that extends the stitches furthest
    # sort videos by start time, and then end time
    # i.e. order videos with same start time by video length in reverse order
    for clip_i_start, clip_i_end in sorted(clips):
        if latest_all_clips >= T or clip_i_start > latest_all_clips:
            # have covered [0, T] or a gap cannot be filled by any clip
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

    return min_count if latest_all_clips >= T else -1


assert 2 == video_stitching(clips=[[1, 9], [1, 5], [0, 4]], T=6)
assert 2 == video_stitching(clips=[[4, 9], [3, 5], [0, 4]], T=6)
assert 3 == video_stitching(clips=[[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]], T=10)
assert -1 == video_stitching(clips=[[0, 1], [1, 2]], T=5)
assert 3 == video_stitching(
    clips=[[0, 1], [6, 8], [0, 2], [5, 6], [0, 4], [0, 3], [6, 7], [1, 3], [4, 7], [1, 4], [2, 5], [2, 6], [3, 4],
           [4, 5],
           [5, 7], [6, 9]],
    T=9)
assert 2 == video_stitching(clips=[[0, 4], [2, 8]], T=5)
