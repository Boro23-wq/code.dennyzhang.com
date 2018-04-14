# Leetcode: Logger Rate Limiter     :BLOG:Basic:


---

Logger Rate Limiter  

---

Similar Problems:  
-   [Design Hit Counter](https://code.dennyzhang.com/design-hit-counter)
-   [Review: Object-Oriented Design Problems](https://code.dennyzhang.com/review-oodesign)
-   Tag: [oodesign](https://code.dennyzhang.com/tag/oodesign)

---

Design a logger system that receive stream of messages along with its timestamps, each message should be printed if and only if it is not printed in the last 10 seconds.  

Given a message and a timestamp (in seconds granularity), return true if the message should be printed in the given timestamp, otherwise returns false.  

It is possible that several messages arrive roughly at the same time.  

Example:  

    Logger logger = new Logger();
    
    // logging string "foo" at timestamp 1
    logger.shouldPrintMessage(1, "foo"); returns true; 
    
    // logging string "bar" at timestamp 2
    logger.shouldPrintMessage(2,"bar"); returns true;
    
    // logging string "foo" at timestamp 3
    logger.shouldPrintMessage(3,"foo"); returns false;
    
    // logging string "bar" at timestamp 8
    logger.shouldPrintMessage(8,"bar"); returns false;
    
    // logging string "foo" at timestamp 10
    logger.shouldPrintMessage(10,"foo"); returns false;
    
    // logging string "foo" at timestamp 11
    logger.shouldPrintMessage(11,"foo"); returns true;

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/logger-rate-limiter)  

Credits To: [leetcode.com](https://leetcode.com/problems/logger-rate-limiter/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/logger-rate-limiter
    ## Basic Ideas: hasmap: message -> timestamp
    ##
    ## Complexity: Time O(1), Space O(n)
    class Logger(object):
    
        def __init__(self):
            """
            Initialize your data structure here.
            """
            self.d = {}
    
        def shouldPrintMessage(self, timestamp, message):
            """
            Returns true if the message should be printed in the given timestamp, otherwise returns false.
            If this method returns false, the message will not be printed.
            The timestamp is in seconds granularity.
            :type timestamp: int
            :type message: str
            :rtype: bool
            """
            if message not in self.d:
                self.d[message] = timestamp
                return True
    
            if timestamp - self.d[message] < 10:
                return False
            else:
                self.d[message] = timestamp
                return True
    
    # Your Logger object will be instantiated and called as such:
    # obj = Logger()
    # param_1 = obj.shouldPrintMessage(timestamp,message)