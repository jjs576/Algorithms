class SegTree:
    def __init__(self, _n, _input):
        self.n = _n
        self.data = [0] * _n
        self.data += _input
        i = _n - 1
        while i > 0:
            self.data[i] = self.data[i << 1] + self.data[i << 1 | 1]
            i -=1

    def query(self, left, right):
        answer = 0
        left += self.n
        right += self.n
        while left < right:
            if left & 1:
                answer += self.data[left]
                left += 1
            if right & 1:
                right -= 1
                answer += self.data[right]
            left >>= 1
            right >>= 1
        return answer
    
    def update(self, pos, val):
        pos += self.n
        self.data[pos] = val
        while pos > 1:
            self.data[pos >> 1] = self.data[pos] + self.data[pos ^ 1]
            pos >>= 1

