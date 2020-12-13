import collections

class RecentCounter:
    def __init__(self):
        self.que = collections.deque()

    def ping(self, t: int) -> int:
        while self.que and self.que[0] < t - 3000:
            self.que.popleft()
        self.que.append(t)
        return len(self.que)
        

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

t = [1, 100, 3001, 3002]

r = RecentCounter()
for i in t:
  print(r.ping(i))