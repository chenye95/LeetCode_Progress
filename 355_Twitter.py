"""
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is able to see the
10 most recent tweets in the user's news feed. Your design should support the following methods:

1. postTweet(user_id, tweet_id): Compose a new tweet.
2. getNewsFeed(user_id): Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must
be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent
3. follow(follower_id, followee_id): Follower follows a followee.
4. unfollow(follower_id, followee_id): Follower unfollows a followee.
"""
from collections import defaultdict, deque
from heapq import merge
from itertools import count, islice
from typing import List


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timer = count(step=-1)
        self.followee = defaultdict(set)
        self.tweets = defaultdict(deque)
        self.maxN = 10

    def post_tweet(self, user_id: int, tweet_id: int) -> None:
        """
        user_id compose a new tweet, tweet_id

        :param user_id: user_id for the tweet
        :param tweet_id: tweet_id for the tweet
        """
        self.tweets[user_id].appendleft((next(self.timer), tweet_id))
        if len(self.tweets[user_id]) > self.maxN:
            self.tweets[user_id].pop()

    def get_news_feed(self, user_id: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by
        users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.

        :param user_id: news feed for user_id
        :return: 10 most recent tweets for user_id, tweets posted either by user or user_id that they follow
        """
        tweets_list = merge(*(self.tweets[u] for u in self.followee[user_id] | {user_id}))
        return [tweet_id for _, tweet_id in islice(tweets_list, self.maxN)]

    def follow(self, follower_id: int, followee_id: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.

        :param follower_id: follower_id follows followee_id
        :param followee_id: follower_id follows followee_id
        """
        self.followee[follower_id].add(followee_id)

    def unfollow(self, follower_id: int, followee_id: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.

        :param follower_id: follower_id unfollows followee_id
        :param followee_id: follower_id unfollows followee_id
        """
        self.followee[follower_id].discard(followee_id)


test = Twitter()
test.post_tweet(1, 5)
assert test.get_news_feed(1) == [5]
test.follow(1, 2)
test.post_tweet(2, 6)
assert test.get_news_feed(1) == [6, 5]
test.unfollow(1, 2)
assert test.get_news_feed(1) == [5]
