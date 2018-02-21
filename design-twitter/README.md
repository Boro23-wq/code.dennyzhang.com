# Leetcode: Design Twitter     :BLOG:Medium:


---

Design Twitter  

---

Similar Problems:  

-   Tag: [#oodesign](https://brain.dennyzhang.com/tag/oodesign)

---

Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is able to see the 10 most recent tweets in the user's news feed. Your design should support the following methods:  

1.  postTweet(userId, tweetId): Compose a new tweet.
2.  getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
3.  follow(followerId, followeeId): Follower follows a followee.
4.  unfollow(followerId, followeeId): Follower unfollows a followee.

Example:  

    Twitter twitter = new Twitter();
    
    // User 1 posts a new tweet (id = 5).
    twitter.postTweet(1, 5);
    
    // User 1's news feed should return a list with 1 tweet id -> [5].
    twitter.getNewsFeed(1);
    
    // User 1 follows user 2.
    twitter.follow(1, 2);
    
    // User 2 posts a new tweet (id = 6).
    twitter.postTweet(2, 6);
    
    // User 1's news feed should return a list with 2 tweet ids -> [6, 5].
    // Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
    twitter.getNewsFeed(1);
    
    // User 1 unfollows user 2.
    twitter.unfollow(1, 2);
    
    // User 1's news feed should return a list with 1 tweet id -> [5],
    // since user 1 is no longer following user 2.
    twitter.getNewsFeed(1);

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/design-twitter)  

Credits To: [leetcode.com](https://leetcode.com/problems/design-twitter/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/design-twitter
    ## Basic Ideas: Two hashmap
    ##     tweet_dict. id -> tweet_list
    ##     follow_dict: id -> id set
    ##
    ## Notice: people may follow themselves
    ##
    ## Assumption: people tweet with post id always grows
    ##
    ## Complexity: getNewsFeed
    ##       Time O(n*log(n)) Space O(n). n = total tweets involved
    import collections, copy
    class Twitter:
    
        def __init__(self):
            """
            Initialize your data structure here.
            """
            self.id = 0
            self.tweet_dict = collections.defaultdict(lambda: )
            self.follow_dict = collections.defaultdict(lambda: set())
    
        def postTweet(self, userId, tweetId):
            """
            Compose a new tweet.
            :type userId: int
            :type tweetId: int
            :rtype: void
            """
            self.tweet_dict[userId].append((self.id, tweetId))
            self.id += 1
    
        def getNewsFeed(self, userId):
            """
            Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
            :type userId: int
            :rtype: List[int]
            """
            l = copy.deepcopy(self.tweet_dict[userId])
            for followee in self.follow_dict[userId]:
                l += self.tweet_dict[followee]
            l.sort(reverse=True)
            res = 
            for (id, tweetId) in l[0:10]: res.append(tweetId)
            return res
    
        def follow(self, followerId, followeeId):
            """
            Follower follows a followee. If the operation is invalid, it should be a no-op.
            :type followerId: int
            :type followeeId: int
            :rtype: void
            """
            if followerId == followeeId: return
            if followeeId not in self.follow_dict[followerId]:
                self.follow_dict[followerId].add(followeeId)
    
        def unfollow(self, followerId, followeeId):
            """
            Follower unfollows a followee. If the operation is invalid, it should be a no-op.
            :type followerId: int
            :type followeeId: int
            :rtype: void
            """
            if followerId == followeeId: return
            if followeeId in self.follow_dict[followerId]:
                self.follow_dict[followerId].remove(followeeId)
    
    
    # Your Twitter object will be instantiated and called as such:
    # obj = Twitter()
    # obj.postTweet(userId,tweetId)
    # param_2 = obj.getNewsFeed(userId)
    # obj.follow(followerId,followeeId)
    # obj.unfollow(followerId,followeeId)