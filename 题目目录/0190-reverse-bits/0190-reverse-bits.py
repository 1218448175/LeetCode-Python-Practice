m0 = 0x55555555
m1 = 0x33333333
m2 = 0x0f0f0f0f
m3 = 0x00ff00ff
m4 = 0x0000ffff

class Solution:
    def reverseBits(self, n: int) -> int:
        n = n >> 1 & m0 | (n & m0) << 1
        n = n >> 2 & m1 | (n & m1) << 2
        n = n >> 4 & m2 | (n & m2) << 4
        n = n >> 8 & m3 | (n & m3) << 8
        return  n >> 16 | (n & m4) << 16
        