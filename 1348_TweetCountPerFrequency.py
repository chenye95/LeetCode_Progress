"""
A social media company is trying to monitor activity on their site by analyzing the number of tweets that occur in
 select periods of time. These periods can be partitioned into smaller time chunks based on a certain frequency (every
 minute, hour, or day).

For example, the period [10, 10000] (in seconds) would be partitioned into the following time chunks with these
    frequencies:
- Every minute (60-second chunks): [10,69], [70,129], [130,189], ..., [9970,10000]
- Every hour (3600-second chunks): [10,3609], [3610,7209], [7210,10000]
- Every day (86400-second chunks): [10,10000]

Notice that the last chunk may be shorter than the specified frequency's chunk size and will always end with the end
 time of the period (10000 in the above example).

Design and implement an API to help the company with their analysis.

Implement the TweetCounts class:
- TweetCounts() Initializes the TweetCounts object.
- void recordTweet(String tweetName, int time) Stores the tweetName at the recorded time (in seconds).
- List<Integer> getTweetCountsPerFrequency(String freq, String tweetName, int startTime, int endTime) Returns a list of
 integers representing the number of tweets with tweetName in each time chunk for the given period of time [startTime,
 endTime] (in seconds) and frequency freq.
    - freq is one of "minute", "hour", or "day" representing a frequency of every minute, hour, or day respectively.
"""
import bisect
from collections import defaultdict
from typing import List, DefaultDict, Optional


class TweetCounts:
    def __init__(self):
        self.tweets: DefaultDict[str, List[int]] = defaultdict(list)

    def record_tweet(self, tweet_handle: str, time: int) -> None:
        """
        :param tweet_handle: key to retrieve tweet counts
        :param time: timestamp in seconds, 0 <= time <= 10**9
        :return: record tweet_handle tweeted at timestamp time
        """
        bisect.insort(self.tweets[tweet_handle], time)

    def get_tweet_counts_per_frequency(self, freq: str, tweet_handle: str, start_time: int, end_time: int) -> List[int]:
        """
        :param freq: one of ["minute", "hour", "day"]
        :param tweet_handle: key to retrieve tweet counts
        :param start_time: start of query window, 0 <= start_time <= 10**9
        :param end_time: end of query window, 0 <= end_time <= 10**9 and 0 <= end_time - start_time <= 10000
        :return: tweet count for each freq window
        """
        delta = 60 if freq == "minute" else 3600 if freq == "hour" else 86400
        tweets_by = self.tweets[tweet_handle]
        tweet_count = []
        for window_start in range(start_time, end_time + 1, delta):
            window_end = min(window_start + delta, end_time + 1)
            tweet_count.append(bisect.bisect_left(tweets_by, window_end) - bisect.bisect_left(tweets_by, window_start))
        return tweet_count


def run_simulation(instructions: List[str], parameters: List[List],
                   expected_output: List[Optional[List]]) -> None:
    test_object = TweetCounts()
    for i in range(1, len(instructions)):
        next_instruction, next_parameter, expected_value = instructions[i], parameters[i], expected_output[i]
        if next_instruction == "recordTweet":
            test_object.record_tweet(next_parameter[0], next_parameter[1])
        else:
            assert test_object.get_tweet_counts_per_frequency(next_parameter[0], next_parameter[1],
                                                              next_parameter[2], next_parameter[3]) == expected_value


test_cases = [(["TweetCounts", "recordTweet", "recordTweet", "recordTweet", "getTweetCountsPerFrequency",
                "getTweetCountsPerFrequency", "recordTweet", "getTweetCountsPerFrequency"],
               [[], ["tweet3", 0], ["tweet3", 60], ["tweet3", 10], ["minute", "tweet3", 0, 59],
                ["minute", "tweet3", 0, 60], ["tweet3", 120], ["hour", "tweet3", 0, 210]],
               [None, None, None, None, [2], [2, 1], None, [4]]),
              (["TweetCounts", "recordTweet", "recordTweet", "recordTweet", "recordTweet", "recordTweet", "recordTweet",
                "getTweetCountsPerFrequency", "getTweetCountsPerFrequency"],
               [[], ["tweet0", 13], ["tweet1", 16], ["tweet2", 12], ["tweet3", 18], ["tweet4", 82], ["tweet3", 89],
                ["day", "tweet0", 89, 9471], ["hour", "tweet3", 13, 4024]],
               [None, None, None, None, None, None, None, [0], [2, 0]]),
              (["TweetCounts", "recordTweet", "recordTweet", "recordTweet", "recordTweet", "recordTweet",
                "getTweetCountsPerFrequency", "getTweetCountsPerFrequency", "getTweetCountsPerFrequency",
                "getTweetCountsPerFrequency"],
               [[], ["tweet0", 857105800], ["tweet1", 255428777], ["tweet2", 13881700], ["tweet3", 82366032],
                ["tweet4", 334311127], ["minute", "tweet0", 255428777, 255438544],
                ["day", "tweet2", 857105800, 857108372], ["minute", "tweet4", 334311127, 334316350],
                ["hour", "tweet3", 82366032, 82370980]],
               [None, None, None, None, None, None,
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0]]), ]
for test_instructions, test_parameters, test_expected_values in test_cases:
    run_simulation(test_instructions, test_parameters, test_expected_values)
