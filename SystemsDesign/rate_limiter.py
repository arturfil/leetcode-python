import time

class APIRateLimiter:
    def __init__(self, max_requesets_per_second=10):
        self.max_requesets_per_second = max_requesets_per_second
        self.window_size = 1 # second
        self.requests = []

    def allow_request(self):
        now = time.time()
        print("Request Now:", now)

        while self.requests and self.requests[0] < now - self.window_size: # is it withing a second
            self.requests.pop(0)

        if len(self.requests) < self.max_requesets_per_second:
            self.requests.append(now)
            return True
        else:
            return False

