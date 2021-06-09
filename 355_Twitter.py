"""
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is able to see the
10 most recent tweets in the user's news feed. Your design should support the following methods:

1. postTweet(user_id, tweet_id): Compose a new tweet.
2. getNewsFeed(user_id): Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must
be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent
3. follow(follower_id, followee_id): Follower follows a follows_list.
4. unfollow(follower_id, followee_id): Follower unfollows a follows_list.
"""
import heapq
import itertools
from collections import defaultdict, deque
from typing import List, Deque, DefaultDict, Set, Tuple


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timer = itertools.count(step=-1)
        self.follows_list: DefaultDict[int, Set[int]] = defaultdict(set)
        self.tweets: DefaultDict[int, Deque[Tuple[int, int]]] = defaultdict(deque)
        self.max_n = 10

    def post_tweet(self, user_id: int, tweet_id: int) -> None:
        """
        user_id compose a new tweet, tweet_id

        :param user_id: user_id for the tweet
        :param tweet_id: tweet_id for the tweet
        """
        self.tweets[user_id].appendleft((next(self.timer), tweet_id))
        if len(self.tweets[user_id]) > self.max_n:
            self.tweets[user_id].pop()

    def get_news_feed(self, user_id: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by
        users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.

        :param user_id: news feed for user_id
        :return: 10 most recent tweets for user_id, tweets posted either by user or user_id that they follow
        """
        tweets_list = heapq.merge(*(self.tweets[u] for u in self.follows_list[user_id] | {user_id}))
        return [tweet_id for _, tweet_id in itertools.islice(tweets_list, self.max_n)]

    def follow(self, follower_id: int, followee_id: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.

        :param follower_id: follower_id follows followee_id
        :param followee_id: follower_id follows followee_id
        """
        self.follows_list[follower_id].add(followee_id)

    def unfollow(self, follower_id: int, followee_id: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.

        :param follower_id: follower_id unfollows followee_id
        :param followee_id: follower_id unfollows followee_id
        """
        self.follows_list[follower_id].discard(followee_id)


def run_simulation(instructions: List[str], parameters: List[List],
                   expected_output: List[List]) -> None:
    test_object = Twitter()
    for i in range(1, len(instructions)):
        next_instruction, next_parameter, expected_value = instructions[i], parameters[i], expected_output[i]
        if next_instruction == "postTweet":
            test_object.post_tweet(next_parameter[0], next_parameter[1])
        elif next_instruction == "getNewsFeed":
            assert test_object.get_news_feed(next_parameter[0]) == expected_value, expected_value
        elif next_instruction == "follow":
            test_object.follow(next_parameter[0], next_parameter[1])
        else:
            test_object.unfollow(next_parameter[0], next_parameter[1])


test_cases = [(["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"],
               [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]],
               [None, None, [5], None, None, [6, 5], None, [5]]),
              (["Twitter", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet",
                "postTweet", "postTweet", "getNewsFeed"],
               [[], [1, 5], [1, 3], [1, 101], [1, 13], [1, 10], [1, 2], [1, 94], [1, 505], [1, 333], [1]],
               [[], [], [], [], [], [], [], [], [], [], [333, 505, 94, 2, 10, 13, 101, 3, 5]]),
              ]
for test_instructions, test_parameters, test_expected_values in test_cases:
    run_simulation(test_instructions, test_parameters, test_expected_values)
