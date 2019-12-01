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

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.tweets[userId].appendleft((next(self.timer), tweetId))
        if len(self.tweets[userId]) > self.maxN:
            self.tweets[userId].pop()

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by
        users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        tweets_list = merge(*(self.tweets[u] for u in self.followee[userId] | {userId}))
        return [t for _, t in islice(tweets_list, self.maxN)]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.followee[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        self.followee[followerId].discard(followeeId)


test = Twitter()
test.postTweet(1, 5)
assert test.getNewsFeed(1) == [5]
test.follow(1, 2)
test.postTweet(2, 6)
assert test.getNewsFeed(1) == [6, 5]
test.unfollow(1, 2)
assert test.getNewsFeed(1) == [5]